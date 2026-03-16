
# ==========
# INTERFAZ
# ==========

import tkinter as tk
import pandas as pd
from tkinter import messagebox
from recomendador import recomendar_productos


#cargar datos para el detalle de los items

df = pd.read_csv('movitemsventas.csv', encoding='latin1', delimiter= ';')
df.head()


# Creamos un nuevo df item detalle unico, con el fin de buscar los nombres por medio del codigo
df_items = df[['f470_rowid_item_ext','f120_descripcion']].drop_duplicates()
df_items.head()


def buscar_nombre(cliente_id):
    fila = df_items[df_items['f470_rowid_item_ext'] == cliente_id]
    if not fila.empty:
        return fila.iloc[0]['f120_descripcion']
    else:
        return None


def crear_interfaz():
    def buscar():
        entrada = entry.get()
        if not entrada.isdigit():
            messagebox.showerror("Error", "Ingresa un ID de producto válido (número entero)")
            return

        producto_id = int(entrada)
        resultado = recomendar_productos(producto_id)
        
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, f"----------------------------------\n")
        text_output.insert(tk.END, f" Sugerencia para:\n")
        text_output.insert(tk.END, f" * {producto_id}:{buscar_nombre(producto_id)} \n")
        text_output.insert(tk.END, f"----------------------------------\n")
        if resultado:
            for prod, score in resultado:
                text_output.insert(tk.END, f"> {prod} | {buscar_nombre(prod)} \n")
        else:
            text_output.insert(tk.END, "No se encontraron recomendaciones.")

    # Crear ventana
    root = tk.Tk()
    root.title("Sugerencias de Producto")
    root.resizable(False, False)
    root.attributes("-topmost", True)  # Siempre encima

    # Tamaño deseado de ventana
    ventana_width = 400
    ventana_height = 600

    # Obtener tamaño de pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Coordenadas para ubicar en esquina inferior derecha (con un margen arriba de la barra de tareas)
    x_pos = screen_width - ventana_width - 10
    y_pos = screen_height - ventana_height - 77  # Ajusta esto si tapa la barra de tareas

    # Aplicar posición
    root.geometry(f"{ventana_width}x{ventana_height}+{x_pos}+{y_pos}")

    # Widgets
    tk.Label(root, text="Ingrese ID de producto:").pack(pady=10)
    entry = tk.Entry(root, justify='center')
    entry.pack()
    # muestra el nombre del item consultado.
    #label_output = tk.Label(root, text=f"Item consultado : {buscar_nombre(entry.get())}").pack(pady=10)
    #label_output.pack(pady=5)
    
    #Button
    tk.Button(root, text="Buscar", command=buscar).pack(pady=10)

    text_output = tk.Text(root, height=60, width=50)
    text_output.pack(pady=5)

    root.mainloop()

# ==========
# INICIAR UI
# ==========
crear_interfaz()