import pandas as pd

"""
Limpieza de duplicados

"""
def cleanData(rawData: pd.DataFrame) -> pd.DataFrame:
    return rawData.drop_duplicates()

"""
Limpieza de nulos

"""
def fillMissingValues(
    rawData: pd.DataFrame,
    colToClean: str,
    typeData: str
) -> pd.DataFrame:

    rawData = rawData.copy()

    if typeData.lower() == 'string':
        rawData[colToClean] = rawData[colToClean].fillna('Desconocido')

    elif typeData.lower() in ('int', 'float'):
        rawData[colToClean] = rawData[colToClean].fillna(
            rawData[colToClean].mean()
        )

    else:
        raise ValueError("Data type is not supported")

    return rawData
"""
Ajuste de formato

"""

def settingFormat(rawData: pd.DataFrame, 
                    colToClean: str,
                    typeData: str) -> pd.DataFrame:

    if typeData.lower == 'string':
        rawData[colToClean] = rawData[colToClean].str.strip().str.capitalize()

    return rawData


def fillAverageSale(rawData: pd.DataFrame):
        sales = rawData.merge(
        rawData[["id_producto", "precio"]],
        on="id_producto",
        how="left"
    )

