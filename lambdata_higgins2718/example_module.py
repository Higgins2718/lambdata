from datetime import datetime
import pandas as pd

x = 2


def split_datetime(columnName: str, dataframe: pd.DataFrame):
    dataframe[columnName] = pd.to_datetime(dataframe[columnName], errors='coerce')

    dataframe['day'] = dataframe[columnName].dt.day
    dataframe['month'] = dataframe[columnName].dt.month
    dataframe['year'] = dataframe[columnName].dt.year
    return dataframe


def list_to_column(listObject: list, dataframe: pd.DataFrame, columnName: str):
    dataframe[columnName] = pd.Series(listObject).astype(str)
    return dataframe
