import pandas as pd

def getRawData(nameCsv: str)  -> pd.DataFrame:
    return pd.read_csv(f'data/raw/{nameCsv}.csv')

