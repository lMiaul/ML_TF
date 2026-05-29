# HR Analytics - Predicción de Promoción de Empleados (ML_TF)

Este proyecto consiste en un pipeline de Machine Learning diseñado para predecir la promoción de empleados basándose en datos históricos de Recursos Humanos. 

## 🚀 Instalación y Configuración

1. Crear y activar tu entorno virtual (recomendado).
2. Instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## 📂 Estructura del Proyecto

* **`conexion_bd.py`**: Módulo refactorizado que se encarga de descargar automáticamente el dataset (`data.csv`) desde Google Drive y devolverlo como un DataFrame de Pandas listo para usarse.
* **`pipeline.ipynb`**: Notebook principal donde se lleva a cabo el Análisis Exploratorio de Datos (EDA) y el Preprocesamiento.
* **`requirements.txt`**: Archivo con las librerías necesarias para la ejecución (`pandas`, `matplotlib`, `seaborn`, `gdown`, etc).

## 📊 Fases Completadas (Preprocesamiento y EDA)

1. **Ingesta de Datos**: Descarga e ingesta automatizada desde la nube hacia Pandas.
2. **Diagnóstico y Comprensión de los Datos**: 
   * Separación algorítmica de variables numéricas vs. categóricas.
   * Resumen y cálculo de porcentajes de registros vacíos/nulos por columna.
   * Detección y visualización de filas duplicadas exactas.
3. **Análisis Estadístico Multidimensional**:
   * **Cardinalidad**: Extracción automatizada de frecuencias y modas (Top 20) para las variables categóricas.
   * **Detección de Outliers**: Identificación de valores atípicos en variables numéricas mediante el método del Rango Intercuartílico (IQR).
4. **Visualización de Datos Integrada**:
   * Histogramas de distribución y Boxplots de dispersión.
   * Gráficos de barras optimizados para conteos (Top 20 registros más frecuentes).
   * Matriz de Correlación Numérica mediante Mapas de Calor (*Heatmaps*).
   * Análisis bivariado con *Pie Charts* para medir el peso de los datos nulos sobre la variable a predecir (`is_promoted`).
5. **Decisiones de Limpieza y Transformación**:
   * **Imputación con lógica de negocio**: Conservación de registros nulos debido a que contienen variables objetivo positivas. `previous_year_rating` se imputa con `0` (asumiendo nuevos ingresos) y `education` con `"Desconocido"`.
   * **Feature Selection**: Remoción de la columna `employee_id` para evitar sobreajuste y ruido en los futuros modelos.

---
*Pipeline en desarrollo. Próximos pasos: Transformación de variables categóricas (Encoding), Escalado de numéricas, y Entrenamiento de Modelos.*
