import sqlite3

print("Inicie a crear sus recetas:")

nombre_receta = input("Introduzca el nombre de la receta: ")
ingredientes = input("Introduzca los ingredientes: ")
pasos = input("Introduzca los pasos: ")








#Establecer la conexión

conexion = sqlite3.connect("sqlite3/Dat1.sqlite3")


#Seleccionar el cursor para iniciar la consulta

consulta = conexion.cursor()

#Valor de los argumentos
argumentos = (nombre_receta, ingredientes, pasos)

sql = """
INSERT INTO Dat1(nombre_receta, ingredientes, pasos)
VALUES (?, ?, ?)
"""

# Realizar la consulta
if (consulta.execute(sql, argumentos)):
    print("Registro guardado con éxito")
else: ("Ha ocurrido un error al guardar el registro")

#Se termina la consulta

consulta.close()

#Se guarda los cambios en la base de datos
conexion.commit()

#Terminar conexión
conexion.close()
