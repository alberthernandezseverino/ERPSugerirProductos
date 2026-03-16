import pandas as pd
# import pyodbc
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
# Conexión a SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=TU_SERVIDOR;DATABASE=TU_BASE;UID=TU_USUARIO;PWD=TU_PASSWORD;'
)

query = "SELECT venta_id, producto_id FROM ventas_detalle"
df = pd.read_sql(query, conn)
"""
#df = pd.read_csv('movitemsventas.csv', encoding='latin1', delimiter= ';')

df = pd.read_csv('movitemsventas.csv', delimiter= ';')
df.head()

# Agrupar productos por venta
ventas_agrupadas = df.groupby('f350_rowid')['f470_rowid_item_ext'].apply(lambda x: ' '.join(map(str, x)))
ventas_agrupadas = ventas_agrupadas.reset_index()

# Convertir a matriz de co-ocurrencia
vectorizer = CountVectorizer(token_pattern=r"(?u)\b\d+\b")
X = vectorizer.fit_transform(ventas_agrupadas['f470_rowid_item_ext'])

# Calcular similitud de coseno
cosine_sim = cosine_similarity(X.T)

# Mapear IDs
producto_idx_map = vectorizer.vocabulary_         # producto_id (str) → index
producto_inv_map = {v: int(k) for k, v in producto_idx_map.items()}  # index → producto_id (int)

# Guardar modelo
with open("modelo_similitud.pkl", "wb") as f:
    pickle.dump({
        "cosine_sim": cosine_sim,
        "producto_inv_map": producto_inv_map,
        "producto_idx_map": producto_idx_map
    }, f)

print("✅ Modelo guardado exitosamente.")