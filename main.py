from datetime import datetime

# Variables
ruta = "/home/cmontes/Documentos/csv_python/nums/"
longitud = 0

# Lectura de archivo para conseguir la cantidad de lineas y el valor de las mismas
lect = open(ruta + "info.log", "r")
linea = lect.readlines()
longitud = len(linea)
print("Las lineas del archivo son", longitud)

# Escritura de archivo con las lineas pasadas y el date time con la siguiente linea del contador
escrt = open(ruta + "info.log", "w")
escrt.writelines(linea)
strContador = str(longitud + 1)
rutaNuevo = ruta + strContador + '-nums.csv'
escrt.writelines(["\n", str(datetime.now()), ' ', strContador, ' ', rutaNuevo])

# Cierre de archivos
escrt.close()
lect.close()

# Se crea el nuevo csv, por el momento se especifica la ruta
nuevo = open(rutaNuevo, 'w')
nuevo.write("Se creó el archivo" + ',' + rutaNuevo)
nuevo.close