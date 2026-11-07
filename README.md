# eShopFast · Análisis de ventas

Proyecto final del curso de análisis de datos (OpenWebinars). Analiza ventas, productos y clientes de una tienda online ficticia para sacar conclusiones que ayuden a mejorar su estrategia comercial.

## Qué hace
1. **Extracción**: carga de `productos.csv`, `clientes.csv` y `ventas.csv` con pandas.
2. **Limpieza y transformación**: eliminación de duplicados, tratamiento de nulos (mediana en edad, "Desconocido" en país), cálculo de `total_venta` y unión en un único DataFrame.
3. **Visualización**: top 5 productos por unidades, distribución de ventas por país y evolución mensual.
4. **SQL**: base de datos SQLite (`eshop.db`) con tres tablas y consultas de ventas por cliente, ventas por producto y estadísticas de edad.

## Tecnologías
Python · pandas · matplotlib · SQLite

## Cómo ejecutarlo
    pip install pandas matplotlib
    python main.py

## Nota
Los datos son ficticios y se han generado para la práctica.
