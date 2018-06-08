import sqlite3, datetime

print("Programa ejecutado")

cadena_texto = input("Introduzca una cadena de texto: ")
entero = input("Introduzca un número entero: ")
decim = input("Introduzca un número decimal: ")

try: entero = int(entero)
except ValueError:
    print(entero, "no es un número entero")
    exit()

try: decim = float(decim) or int(decim)
except ValueError:
    print(decim, "no es un número decimal")
    exit()







#Establecer la conexión

conexion = sqlite3.connect("sqlite3/Dat1.sqlite3")


#Seleccionar el cursor para iniciar la consulta

consulta = conexion.cursor()

#Valor de los argumentos
argumentos = (cadena_texto, entero, decim, datetime.date.today())

sql = """
INSERT INTO Dat1(cadena_texto, entero, decim, fecha)
VALUES (?, ?, ?, ?)
"""

# Realizar la consulta
if (consulta.execute(sql, argumentos)):
    print("Registro guardado con exito")
else: ("Ha ocurrido un error al guardar el registro")

#Se termina la consulta

consulta.close()

#Se guarda los cambios en la base de datos
conexion.commit()

conexion.close()
