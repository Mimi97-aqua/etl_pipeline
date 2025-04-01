import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv

from helper import *

load_dotenv()
db_url = os.getenv('DB_URL')


class ETLPipeline:
    def __init__(self, db_url) -> None:
        self.db_url = db_url

    def extract(self, file_path: str) -> pd.DataFrame:
        """
        Extracts data from a data source file and loads it into a Pandas DataFrame.
    
        :param file_path: The file path of the data source (Excel format) to be read.
        :return: A Pandas DataFrame containing the data from the source file.
        :raises FileNotFoundError: If the specified file path does not exist.
        :raises pd.errors.EmptyDataError: If the file is empty or contains no data.
        """
        try:
            df = pd.read_excel(file_path)
            print('Data extracted successfully.')
            return df
        except FileNotFoundError:
            print(f'File not found: {file_path}')
        except pd.errors.EmptyDataError:
            print(f'Data in {file_path} is empty or contains no data.')
            return None

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This method applies transformations to the input Pandas DataFrame to prepare 
        it for loading into the database. The transformations include cleaning data, 
        renaming columns, handling missing values, and other data normalization tasks.
        
        :param df: A Pandas DataFrame containing the data extracted from the source file.
        :return: A transformed Pandas DataFrame that is ready for loading into the database.
        :raises ValueError: If the input DataFrame is empty or invalid.
        :raises KeyError: If required columns are not found in the input DataFrame.
        :raises TypeError: If the input data contains incompatible types for transformation.
        """
        try:
            # Remove duplicates
            df = df.drop_duplicates("ID", keep="first")

            # Drop columns
            columns_to_drop = ["Place of Birth", "Emergency Contact ID", "Email", "Phone"]
            df = df.drop(columns=columns_to_drop)

            # Add columns
            df["Work Hours"] = df["Contract Type"].apply(set_hours)
            df["Age"] = df["Date of Birth"].apply(calculate_age)
            df["Month of Birth"] = df["Date of Birth"].dt.month_name()

            # Rename columns
            df = df.rename(columns={"Address": "City"})

            # Replace data in cells
            replacements = {"IT": "Information Technology", "USA": "United States of America"}
            df = df.replace(replacements)

            # Data validation
            df["First Name"] = df["First Name"].astype(str)
            df["Last Name"] = df["Last Name"].astype(str)
            df["Department"] = df["Department"].astype(str)
            df["City"] = df["City"].astype("category")
            df["Country"] = df["Country"].astype("category")
            df["Contract Type"] = df["Contract Type"].astype("category")
            df["Gender"] = df["Gender"].astype("category")
            df["Month of Birth"] = df["Month of Birth"].astype(str)

            print('Data successfully transformed.')
            return df
        except ValueError:
            print('Invalid input DataFrame.')
        except KeyError:
            print('Required columns not found in the input DataFrame.')
        except TypeError:
            print('Data contains incompatible types for transformation.')
            return None

    def load(self, df, table_name):
        """
        Load data from a DataFrame into a specified database table.

        This method takes a DataFrame and writes its data into a table within the
        configured database.

        :param df: The DataFrame containing the data to load into the database table
        :type df: pandas.DataFrame
        :param table_name: The name of the database table where data will be loaded
        :type table_name: str
        :return: None
        :rtype: NoneType
        """
        try:
            engine = create_engine(self.db_url)
            df.to_sql(table_name, engine, if_exists='replace', index=False)
            print(f'Data loaded successfully into {table_name} table.')
        except Exception as e:
            print(f'Error loading data into {table_name} table: {e}')

    def run_pipeline(self, file_path, table_name):
        """
        Executes the pipeline process by loading data from a specified file and inserting it
        into the given database table. The method processes the data and ensures it is correctly
        transferred and stored.

        :param file_path: Path to the file containing the data to be processed.
        :type file_path: str
        :param table_name: Name of the table in the database where the data will be inserted.
        :type table_name: str
        :return: None
        :rtype: None
        """
        df = self.extract(file_path)
        if df is not None:
            df = self.transform(df)
            if df is not None:
                self.load(df, table_name)
            else:
                print('Data transformation failed.')
        else:
            print('Data extraction failed.')


if __name__ == "__main__":
    etl = ETLPipeline(db_url)
    etl.run_pipeline('employees_db.xlsx', 'employees')