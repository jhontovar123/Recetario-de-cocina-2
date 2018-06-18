import sqlite3

#Conectar a la base de datos
conexion = sqlite3.connect("sqlite3/Dat1.sqlite3")

#Seleccionar el cursor para realizar la consulta
consulta = conexion.cursor()

insert = """
CREATE TABLE IF NOT EXISTS Dat1(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nombre_receta VARCHAR(50) NOT NULL,
ingredientes VARCHAR(150) NOT NULL,
pasos VARCHAR(300) NOT NULL)"""

#Ejecutar la consulta
if(consulta.execute(insert)) :
    print("Tabla creada con exito")
else:
    print("Ha ocurrido un error al crear la tabla")

#Se termina la consulta
consulta.close()

#Guardar cambios en la base de datos
conexion.commit()

#Se cierra la conexion a la base de datos
conexion.close()
