import pandas as pd

def createFinalDataFrame(
    rawDataSales: pd.DataFrame,
    rawDataProducts: pd.DataFrame,
    rawDataCustomers: pd.DataFrame
) -> pd.DataFrame:

    products = rawDataProducts.rename(columns={"nombre": "nombre_producto"})
    customers = rawDataCustomers.rename(columns={"nombre": "nombre_cliente"})

    salesWithProducts = rawDataSales.merge(
        products,
        on="id_producto",
        how="left"
    )

    salesWithCustomers = salesWithProducts.merge(
        customers,
        on="id_cliente",
        how="left"
    )

    salesWithCustomers["total_venta"] = (
        salesWithCustomers["cantidad"] *
        salesWithCustomers["precio"]
    )

    finalDataFrame = salesWithCustomers[[
        "nombre_cliente",
        "nombre_producto",
        "categoria",
        "pais",
        "cantidad",
        "total_venta",
        "fecha"
    ]]

    return finalDataFrame