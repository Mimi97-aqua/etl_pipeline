from datetime import datetime


def set_hours(contract_type: str) -> int:
    """
    Determines the weekly working hours based on the contract type.

    :param contract_type: A string indicating the type of contract. 
                          Expected values are "Full-time", "Part-time", or "Freelance"
    :return: An integer representing the number of working hours per week. 
             Returns 40 for "Full-time", 20 for "Part-time", and 0 for any other contract type.
    """
    if contract_type == "Full-time":
        return 40
    elif contract_type == "Part-time":
        return 20
    else:
        return 0


def calculate_age(date_of_birth: datetime) -> int:
    """
    Gets the age of an employee given their date of birth

    :param date_of_birth: The employee's date of birth
    :return: Employee's age
    """
    today = datetime.today()
    return today.year - date_of_birth.year
