import pandas as pd


def extract(file_path: str) -> pd.DataFrame:
    """
    Extracts data from data source and loads it into pandas dataframe.
    :param file_path: The file name or file location of the data source.
    :return: Dataframe containing data from data source.
    """
    df = pd.read_csv(file_path)
    return df
