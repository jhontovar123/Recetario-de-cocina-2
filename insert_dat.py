import sqlite3

print("Programa ejecutado")

nombre_receta = input("Introduzca el nombre de la receta: ")
ingredientes=[]
for i in range(20):
    i= input("Introduzca ingrediente:")
    ingredientes.append(i)
    if i=="":
        break
a= len(ingredientes)
ingredientes= " ".join(ingredientes[0:a-1])
print("Los ingredientes son:", ingredientes)

Pasos=[]
for i in range(20):
  i=input("Ingresar paso:")
  Pasos.append(i)
  if i=="":
    break
b=len(Pasos)
pasos= " ".join(Pasos[0:b-1])
print("Los pasos son:", pasos)








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
