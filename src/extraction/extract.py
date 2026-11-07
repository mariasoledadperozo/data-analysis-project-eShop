import pandas as pd

def getRawData(nameCsv: str)  -> pd.DataFrame:
    return pd.read_csv('data/raw/{nameCsv}.csv')

