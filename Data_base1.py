import sqlite3

#Conectar a la base de datos
conexion = sqlite3.connect("sqlite3/Dat1.sqlite3")

#Seleccionar el cursos para realizar la consulta
consulta = conexion.cursor()

insert = """
CREATE TABLE IF NOT EXISTS Dat1(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
cadena_texto VARCHAR(50) NOT NULL,
entero INTEGER NOT NULL,
decim FLOAT NOT NULL,
fecha DATE NOT NULL)"""

#Ejecutar la consulta
if(consulta.execute(insert)) : print("Tabla creada con exito")
else:
    print("Ha ocurrido un error al crear la tabla")

#Se termona la consulta
consulta.close()

#Se guarda los cambios en la base de datos
conexion.commit()

#Se cierra la conexion a la base de datos
conexion.close()
