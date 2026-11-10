import pandas as pd
import extraction.extract as ex
import processing.cleaning as cl
import analysis.analysis as an 
import visualization.charts as ch
import database.exportDatabase as edb


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


