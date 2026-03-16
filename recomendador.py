import pickle

# Cargar modelo
with open("modelo_similitud.pkl", "rb") as f:
    data = pickle.load(f)

cosine_sim = data["cosine_sim"]
producto_idx_map = data["producto_idx_map"]
producto_inv_map = data["producto_inv_map"]

# Función para recomendar
def recomendar_productos(producto_id, top_n=10):
    producto_id = str(producto_id)

    if producto_id not in producto_idx_map:
        return []

    idx = producto_idx_map[producto_id]
    similitudes = cosine_sim[idx]

    # Ordenar por similitud
    similares = sorted(
        enumerate(similitudes),
        key=lambda x: -x[1]
    )

    recomendaciones = []
    for i, score in similares:
        if i == idx:
            continue
        recomendaciones.append((producto_inv_map[i], round(float(score), 3)))
        if len(recomendaciones) == top_n:
            break

    return recomendaciones