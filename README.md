*ERPSugerirProductos*🚀

Módulo inteligente de recomendación de productos diseñado para integrarse con sistemas ERP (Siesa Enterprise / SAP). Este sistema analiza el histórico de ventas para sugerir artículos complementarios, optimizando el cross-selling y mejorando la experiencia de compra.

📋 Descripción del Proyecto
El sistema procesa transacciones de ventas para calcular la similitud de co-ocurrencia entre productos. Al identificar qué artículos se venden juntos con mayor frecuencia, el módulo permite al personal de ventas o al sistema automatizado realizar sugerencias estratégicas basadas en datos reales extraídos directamente de las bases de datos del ERP.

🏗️ Arquitectura Técnica
El flujo de datos está diseñado para ser compatible con la estructura de tablas de un ERP:

Entrenamiento (entrenar_y_guardar.py): Utiliza pandas para procesar los movimientos de inventario. Genera una matriz de similitud de coseno y la serializa como un modelo listo para producción.

Motor de Inferencia (recomendador.py): Clase optimizada para cargar el modelo serializado, permitiendo consultas rápidas mediante el ID del producto.

Interfaz de Usuario (UIRecomendarProductos.py): Interfaz de escritorio desarrollada en tkinter para consulta en tiempo real, facilitando la búsqueda de productos por código o descripción.

⚙️ Integración con ERP (Siesa/SAP)
Para adaptar este motor a su entorno productivo, el script entrenar_y_guardar.py incluye una plantilla de conexión mediante pyodbc, que permite:

Consumir vistas o tablas de ventas directamente desde el servidor SQL del ERP.

Integrar campos clave como f350_rowid (identificador de transacción) y f470_rowid_item_ext (identificador de producto) para mantener la integridad de los datos del sistema fuente.

🚀 Instalación y Uso
1. Requisitos Previos
Python 3.x

Librerías: pandas, scikit-learn, pickle (y pyodbc para la conexión al ERP).

2. Configuración
Asegúrate de que el archivo movitemsventas.csv (o tu consulta SQL) contenga los mapeos necesarios entre los IDs de producto y sus descripciones, tal como se define en la lógica de UIRecomendarProductos.py.

3. Ejecución
Entrenar: Ejecuta el entrenamiento para actualizar el modelo con los últimos movimientos:

Bash
python entrenar_y_guardar.py
Consultar: Lanza la interfaz gráfica para el usuario final:

Bash
python UIRecomendarProductos.py
