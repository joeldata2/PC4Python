#!pip install pyfiglet

import modulos.bd as bd
from modulos.jobs import *
from modulos.proceso import *
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()
figlet.setFont(font='rectangles')

database=None
def main():
    salir=False
    init=True
    while not salir:
        #flag para que se inice solo una vez
        if init:
            user=input("ingrese su nombre de usuario temporal: ") 
            init=False
            config() ## ejecutar las consideraciones basicas al iniciar la aplicacion
        opciones="""
        1.  Crear producto
        2.  Listar productos
        3.  Editar nombre de producto 
        4.  Eliminar producto
        5.  Consultar tipo de cambio
        6.  Actualizar tipo de cambio
        7.  Agregar cliente 
        8.  Listar clientes 
        9.  Editar precio 
        10. Editar stock 
        11. Buscar producto   
        12. Salir"""
        figlet = Figlet()
        figlet.setFont(font='rectangles')
        print(figlet.renderText("Bienvenidos a store DatuxTec"))
        print(opciones)
        opc=int(input("ingrese una opcion: "))
        if opc==1:
            crear_producto(user)
        elif opc==2:
            listar_producto(user)
        elif opc==3:
            editar_nombre(user)
        elif opc==4:
            eliminar_producto(user)
        elif opc==5:
            consultar_tipo_cambio(user)
        elif opc==6:
            actualizar_tipo_cambio(user)
        elif opc==7:
            agregar_cliente(user)
        elif opc==8:
            listar_clientes(user)
        elif opc==9:
            editar_precio(user)
        elif opc==10:
            editar_stock(user)
        elif opc==11:
            buscar_producto_por_nombre(user) 
        elif opc==12:
            salir=True
            print("terminando sesion....")
            break
        else:
            print("ingrese una opcion valida")

#funcion que configura la inicializacion de la aplicacion
def config():

    database=bd.Bd()
    query_products="""
        CREATE TABLE  IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    price REAL NOT NULL,
                    stock INTEGER NOT NULL
                );
    """
    #{"compra":3.762,"venta":3.774,"origen":"SUNAT","moneda":"USD","fecha":"2023-12-12"}
    query_tipo_cambio="""
        CREATE TABLE  IF NOT EXISTS tipo_cambio (
                    id_tipo_cambio INTEGER PRIMARY KEY,
                    compra FLOAT NOT NULL,
                    venta FLOAT NULL,
                    origen VARCHAR(20) NOT NULL,
                    moneda VARCHAR(5) NOT NULL,
                    fecha DATETIME NOT NULL
                );
    """
    query_cliente="""
        CREATE TABLE IF NOT EXISTS cliente (
                    id_cliente INTEGER PRIMARY KEY,
                    name_cliente VARCHAR(100) NOT NULL,
                    direccion VARCHAR(200) NOT NULL,
                    telefono INTEGER NOT NULL
                );
    """
    #"""DROP TABLE IF EXISTS cliente;"""
    
    database.execute_query(query_products)
    database.execute_query(query_tipo_cambio)
    database.execute_query(query_cliente)


if __name__=='__main__':
    main()




if __name__ == "__main__":
    user = "Joel"  # Reemplaza con el nombre de usuario adecuado
    consultar_tipo_cambio(user)
    buscar_producto_por_nombre(user)