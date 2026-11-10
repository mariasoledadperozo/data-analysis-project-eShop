from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

ROOT_DIR = Path(__file__).resolve().parents[2] #Subir dos niveles del proyecto para llegar a la raíz del proyecto
DB_DIR = ROOT_DIR / "data" / "db" #Carpeta donde se guardarán las bases de datos


#Guarda el DataFrame final en la base de datos SQLite
def saveFinalDataFrameToDb(df: pd.DataFrame, dbName: str):
    DB_DIR.mkdir(parents=True, exist_ok=True)  

    dbPath = DB_DIR / f"{dbName}.db"
    engine = create_engine(f"sqlite:///{dbPath}")

    df.to_sql(dbName, engine, if_exists="replace", index=False)