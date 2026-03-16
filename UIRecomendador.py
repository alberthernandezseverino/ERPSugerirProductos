import tkinter as tk
from tkinter import messagebox
from recomendador import recomendar_productos

def crear_interfaz():
    def buscar():
        entrada = entry.get()
        if not entrada.isdigit():
            messagebox.showerror("Error", "Ingresa un ID de producto válido")
            return

        producto_id = int(entrada)
        resultado = recomendar_productos(producto_id)

        text_output.delete("1.0", tk.END)
        if resultado:
            for prod, score in resultado:
                text_output.insert(tk.END, f"Producto: {prod} | Score: {score}\n")
        else:
            text_output.insert(tk.END, "No se encontraron recomendaciones.")

    root = tk.Tk()
    root.title("Sugerencias de Producto")
    root.resizable(False, False)
    root.attributes("-topmost", True)

    ventana_width = 350
    ventana_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_pos = screen_width - ventana_width - 10
    y_pos = screen_height - ventana_height - 60
    root.geometry(f"{ventana_width}x{ventana_height}+{x_pos}+{y_pos}")

    tk.Label(root, text="Ingrese ID de producto:").pack(pady=10)
    entry = tk.Entry(root, justify='center')
    entry.pack()

    tk.Button(root, text="Buscar", command=buscar).pack(pady=10)

    text_output = tk.Text(root, height=10, width=40)
    text_output.pack(pady=5)

    root.mainloop()

crear_interfaz()