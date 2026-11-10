import matplotlib as plt
import pandas as pd


def mostSelledProduct(ProductDataFrame: pd.DataFrame):
    topProducts = (
        ProductDataFrame.groupby("nombre_producto")["cantidad"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(10, 5))
    topProducts.plot(kind="bar")

    plt.title("Top 5 productos más vendidos")
    plt.xlabel("Producto")
    plt.ylabel("Unidades vendidas")

    plt.tight_layout()
    plt.show()

def mostSelledProductPerCountry (ProductDataFrame: pd.DataFrame):
    topProducts = (
        ProductDataFrame.groupby("pais")["cantidad"]
        .sum()
        .sort_values(ascending=False)
    )

    topProducts.plot.pie(autopct="%1.1f%%", startangle=90)
    plt.title("Distribución de ventas por país")
    plt.ylabel("")  
    plt.show()

def monthlySales (ProductDataFrame: pd.DataFrame):
    df = ProductDataFrame.copy()
    df["fecha"] = pd.to_datetime(df["fecha"])

    monthlySales = (
        df.groupby(df["fecha"].dt.to_period("M"))["cantidad"]
        .sum()
    )

    monthlySales.plot.line(marker="o")
    plt.title("Evolución mensual del total de ventas")
    plt.xlabel("Mes")
    plt.ylabel("Total de ventas")
    plt.grid(True)
    plt.show()