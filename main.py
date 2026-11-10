import pandas as pd
import src.extraction.extract as ex
import src.processing.cleaning as cl
import src.analysis.analysis as an 
import src.visualization.charts as ch
import src.database.exportDatabase as edb


# Step 1: Extract data from CSV files
dfCliente = ex.getRawData("clientes")
dfProductos = ex.getRawData("productos")
dfVentas = ex.getRawData("ventas")

# Step 2: Clean the data
dfCliente = cl.cleanData(dfCliente)
dfProductos = cl.cleanData(dfProductos)
dfVentas = cl.cleanData(dfVentas)

# Step 3: Fill missing values and set formats for dfCliente and dfProductos
dfCliente = cl.fillMissingValues(dfCliente, "nombre", "string")
dfCliente = cl.fillMissingValues(dfCliente, "edad", "int")
dfCliente = cl.fillMissingValues(dfCliente, "pais", "string")
dfCliente = cl.settingFormat(dfCliente, "pais", "string")
dfCliente = cl.settingFormat(dfCliente, "nombre", "string")

dfProductos = cl.fillMissingValues(dfProductos, "nombre", "string")
dfProductos = cl.fillMissingValues(dfProductos, "categoria", "string")
dfProductos = cl.fillMissingValues(dfProductos, "precio", "float")
dfProductos = cl.settingFormat(dfProductos, "nombre", "string")
dfProductos = cl.settingFormat(dfProductos, "categoria", "string")

# Step 4: Format dfVentas (ajusta las columnas a las que tengas)
dfVentas = cl.fillMissingValues(dfVentas, "cantidad", "int")

# Step 5: Build the final DataFrame
dfFinal = an.createFinalDataFrame(dfVentas, dfProductos, dfCliente)

# Step 6: Save to database
edb.saveFinalDataFrameToDb(dfFinal, "eshop")

# Step 7: Charts
ch.mostSelledProduct(dfFinal)
ch.mostSelledProductPerCountry(dfFinal)
ch.monthlySales(dfFinal)

if __name__ == "__main__":
    main()
