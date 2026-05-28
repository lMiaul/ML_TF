import gdown
import pandas as pd
import os

FILE_ID = '1fzWfN2YhxITILVXv2PW6JKJ1z4H4XAiK'
LOCAL_PATH = 'data.csv'

# --- Descarga ---
try:
    if not os.path.exists(LOCAL_PATH):
        print("Descargando archivo desde Google Drive...")
        gdown.download(f'https://drive.google.com/uc?id={FILE_ID}', LOCAL_PATH, quiet=False)
        print(f"Archivo guardado en: {LOCAL_PATH}")
    else:
        print(f"Archivo ya existe localmente: {LOCAL_PATH}")
except Exception as e:
    raise RuntimeError(f"Error al descargar el archivo: {e}")

# --- Carga ---
try:
    df = pd.read_csv(LOCAL_PATH, encoding='latin-1', sep=None, engine='python')
    print(f"DataFrame cargado correctamente: {df.shape[0]} filas x {df.shape[1]} columnas")
    print(df.head())
except FileNotFoundError:
    raise FileNotFoundError(f"No se encontró el archivo: {LOCAL_PATH}")
except pd.errors.ParserError as e:
    raise ValueError(f"Error al parsear el CSV: {e}")
except Exception as e:
    raise RuntimeError(f"Error inesperado al cargar los datos: {e}")
