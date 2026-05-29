import gdown
import pandas as pd
import os

def obtener_dataframe(file_id='1fzWfN2YhxITILVXv2PW6JKJ1z4H4XAiK', local_path='data.csv'):
    """
    Descarga el dataset desde Google Drive (si no existe localmente) y retorna un DataFrame de Pandas.
    """
    # --- Descarga ---
    try:
        if not os.path.exists(local_path):
            print("Descargando archivo desde Google Drive...")
            gdown.download(f'https://drive.google.com/uc?id={file_id}', local_path, quiet=False)
            print(f"Archivo guardado en: {local_path}")
        else:
            print(f"Archivo ya existe localmente: {local_path}")
    except Exception as e:
        raise RuntimeError(f"Error al descargar el archivo: {e}")

    # --- Carga ---
    try:
        df = pd.read_csv(local_path, encoding='latin-1', sep=None, engine='python')
        print(f"DataFrame cargado correctamente: {df.shape[0]} filas x {df.shape[1]} columnas")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo: {local_path}")
    except pd.errors.ParserError as e:
        raise ValueError(f"Error al parsear el CSV: {e}")
    except Exception as e:
        raise RuntimeError(f"Error inesperado al cargar los datos: {e}")

if __name__ == "__main__":
    # Esto solo se ejecutará si corres el script directamente (python conexion_bd.py)
    # y sirve para hacer pruebas.
    df_prueba = obtener_dataframe()
    print(df_prueba.head())
