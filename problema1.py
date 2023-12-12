# Ruta del archivo
ruta_archivo = r'/workspaces/PC4Python/texto_practica4.txt'

#Leer el archivo, estandarizar texto y contar la frecuencia de la palabra "la"
with open(ruta_archivo, 'r') as archivo:
    contenido = archivo.read()
    fr_la = contenido.lower().count('la')  # Convertir a minúsculas para evitar diferencia mayúsculas y minúsculas
print(f'La palabra "la" aparece {fr_la} veces en el archivo.')

def agregar_texto(ruta_archivo):
    # Solicitar al usuario que ingrese un texto
    texto_nuevo = input('Ingresa el texto que quieres agregar al final del archivo:\n')

    # Agregar el texto
    with open(ruta_archivo, 'a') as archivo:
        archivo.write('\n' + texto_nuevo + '\n')

    print('Texto agregado exitosamente al final del archivo.')

# Llamar a la función
agregar_texto(ruta_archivo)
