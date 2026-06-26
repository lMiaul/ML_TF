# HR Analytics - Predicción de Promoción de Empleados (ML_TF)

Este proyecto implementa un pipeline completo de Machine Learning para predecir la promoción de empleados a partir de datos históricos de Recursos Humanos. Abarca desde la ingesta y limpieza de datos hasta el entrenamiento, evaluación y explicabilidad de múltiples modelos de clasificación.

## 🚀 Instalación y Configuración

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd ML_TF
```

2. Crear y activar un entorno virtual (recomendado):
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar el notebook `pipeline.ipynb` desde Jupyter o VS Code.

## 📂 Estructura del Proyecto

```
ML_TF/
├── conexion_bd.py      # Módulo de descarga e ingesta del dataset desde Google Drive
├── pipeline.ipynb      # Notebook principal con el pipeline completo de ML
├── data.csv            # Dataset descargado automáticamente (no versionado)
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Exclusiones de Git (.venv, __pycache__)
└── README.md
```

| Archivo | Descripción |
|---------|-------------|
| `conexion_bd.py` | Descarga automáticamente el dataset desde Google Drive (si no existe localmente) y lo retorna como un DataFrame de Pandas. |
| `pipeline.ipynb` | Notebook principal que contiene todo el flujo de trabajo: EDA, preprocesamiento, transformación, modelado, evaluación y explicabilidad. |
| `requirements.txt` | Librerías necesarias: `gdown`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `shap`, `tabulate`, `ipykernel`, `ipython`. |

## 📊 Fases del Pipeline

### 1. Ingesta de Datos
Descarga e ingesta automatizada del dataset desde Google Drive hacia un DataFrame de Pandas, gestionada por el módulo `conexion_bd.py`.

### 2. Comprensión y Diagnóstico de los Datos (EDA)
- Separación algorítmica de variables numéricas vs. categóricas.
- Estadísticas descriptivas y resumen de estructura del dataset.
- Cálculo de porcentajes de valores nulos/vacíos por columna.
- Detección y visualización de filas duplicadas exactas.
- Análisis de cardinalidad: frecuencias y modas (Top 20) para variables categóricas.
- Detección de outliers en variables numéricas mediante el método del Rango Intercuartílico (IQR).

### 3. Visualización de Datos
- Histogramas de distribución y Boxplots de dispersión para variables numéricas.
- Gráficos de barras (Top 10) para variables categóricas y numéricas.
- Matriz de correlación numérica mediante Mapas de Calor (*Heatmaps*).
- Análisis bivariado con *Pie Charts* para medir el peso de los datos nulos sobre la variable objetivo (`is_promoted`).

### 4. Limpieza de Datos
- **Imputación con lógica de negocio**:
  - `previous_year_rating` → imputado con `0` (asumiendo nuevas contrataciones).
  - `education` → imputado con `"Desconocido"`.
- **Feature Selection — Eliminación de columnas**:
  - `employee_id`: identificador único sin capacidad predictiva.
  - `region`, `gender`, `age`: variables sensibles eliminadas para mitigar sesgos discriminatorios.

### 5. Transformación de Datos
- **One-Hot Encoding**: conversión de variables categóricas en variables numéricas binarias.
- **Escalamiento con StandardScaler**: estandarización de variables numéricas para homogeneizar rangos.
- **Análisis de correlación post-transformación**: verificación de que no existen pares de variables con correlación superior a 0.85, descartando la necesidad de eliminar columnas adicionales.

### 6. Modelado
Entrenamiento y optimización de tres modelos de clasificación mediante `RandomizedSearchCV` con validación cruzada estratificada (`StratifiedKFold`):

| Modelo | Descripción |
|--------|-------------|
| **Random Forest** | Modelo principal, optimizado con búsqueda aleatoria de hiperparámetros. |
| **Regresión Logística** | Modelo de comparación lineal. |
| **SVM (Support Vector Machine)** | Modelo de comparación basado en márgenes. |

### 7. Evaluación y Pruebas
- Evaluación con métricas clave: Accuracy, Precision, Recall, F1-Score, AUC-ROC.
- Calibración de umbral de decisión.
- Matriz de comparación de desempeño entre los tres modelos.

### 8. Explicabilidad del Modelo (SHAP)
- **Waterfall Plot**: explicabilidad local (predicción individual).
- **Beeswarm Plot**: explicabilidad global (importancia de features a nivel del dataset).

## 🛠️ Tecnologías Utilizadas

| Librería | Uso |
|----------|-----|
| `pandas` | Manipulación y análisis de datos |
| `numpy` | Operaciones numéricas |
| `matplotlib` | Visualización de datos |
| `seaborn` | Visualización estadística |
| `scikit-learn` | Preprocesamiento, modelado y evaluación |
| `shap` | Explicabilidad de modelos |
| `gdown` | Descarga de datos desde Google Drive |
| `tabulate` | Formateo de tablas |
| `ipykernel` / `ipython` | Ejecución de notebooks |
