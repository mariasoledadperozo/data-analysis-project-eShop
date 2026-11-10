import pandas as pd

# --- Configuración (un solo sitio donde cambiar nombres de columnas) ---
FINAL_COLUMNS = [
    "nombre_cliente",
    "nombre_producto",
    "categoria",
    "pais",
    "cantidad",
    "total_venta",
    "fecha",
]


def renameColumns(df: pd.DataFrame, mapping: dict[str, str]) -> pd.DataFrame:
    return df.rename(columns=mapping)


def mergeTables(left: pd.DataFrame, right: pd.DataFrame, key: str) -> pd.DataFrame:
    return left.merge(right, on=key, how="left")


def addTotalSale(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(total_venta=df["cantidad"] * df["precio"])


def selectColumns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return df[columns].copy()


def createFinalDataFrame(
    rawDataSales: pd.DataFrame,
    rawDataProducts: pd.DataFrame,
    rawDataCustomers: pd.DataFrame,
) -> pd.DataFrame:
    products = renameColumns(rawDataProducts, {"nombre": "nombre_producto"})
    customers = renameColumns(rawDataCustomers, {"nombre": "nombre_cliente"})

    return (
        rawDataSales
        .pipe(mergeTables, products, "id_producto")
        .pipe(mergeTables, customers, "id_cliente")
        .pipe(addTotalSale)
        .pipe(selectColumns, FINAL_COLUMNS)
    )