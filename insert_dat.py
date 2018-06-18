import sqlite3

print("Programa ejecutado")

nombre_receta = input("Introduzca el nombre de la receta: ")
ingredientes=[]
for i in range(50):
    i= input("Introduzca ingrediente:")
    ingredientes.append(i)
    if i=="nada":
        break
a= len(ingredientes)
print("Los ingredientes son:", ingredientes[0:a-1])
Pasos=[]
for i in range(50):
  i=input("Ingresar paso:")
  Pasos.append(i)
  if i=="nada":
    break
b=len(Pasos)
print("Los pasos son:", Pasos[0:b-1])







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
    print("Registro guardado con exito")
else: ("Ha ocurrido un error al guardar el registro")

#Se termina la consulta

consulta.close()

#Se guarda los cambios en la base de datos
conexion.commit()

conexion.close()
