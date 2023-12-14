import requests
import sqlite3

def obtener_tipo_cambio():
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hubo algún error en la petición
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}")
        return None

def insertar_tipo_cambio_en_db(tipo_cambio):
    # Conexión a la base de datos (SQLite en este ejemplo)
    conexion = sqlite3.connect('bd.Bd')
    cursor = conexion.cursor()

    # Crear la tabla si no existe
    cursor.execute("""
        CREATE TABLE  IF NOT EXISTS tipo_cambio (
                    id_tipo_cambio INTEGER PRIMARY KEY,
                    compra FLOAT NOT NULL,
                    venta FLOAT NULL,
                    origen VARCHAR(20) NOT NULL,
                    moneda VARCHAR(5) NOT NULL,
                    fecha DATETIME NOT NULL
                );
    """)

    # Insertar el tipo de cambio en la tabla
    cursor.execute('''
        INSERT INTO tipo_cambio (compra, venta, origen, moneda, fecha)
        VALUES (?, ?, ?, ?, ?)
    ''', (tipo_cambio['compra'], tipo_cambio['venta'], tipo_cambio['origen'], tipo_cambio['moneda'], tipo_cambio['fecha']))

    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def actualizar_tipo_cambio(user):
    tipo_cambio = obtener_tipo_cambio()

    if tipo_cambio:
        insertar_tipo_cambio_en_db(tipo_cambio)
        print("Tipo de cambio actualizado correctamente.")
    else:
        print("No se pudo obtener el tipo de cambio.")

def consultar_tipo_cambio(user):
    conexion = sqlite3.connect('bd.Bd')
    cursor = conexion.cursor()

    # Ejecutar una consulta para obtener todos los registros de la tabla tipo_cambio
    cursor.execute('SELECT * FROM tipo_cambio')
    
    # Obtener todos los resultados
    resultados = cursor.fetchall()

    # Imprimir los resultados
    for resultado in resultados:
        print(resultado)

    # Cerrar la conexión
    conexion.close()
