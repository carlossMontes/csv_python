import random

columnas = 10
filas = 7
vaso = filas
filas = columnas
columnas = vaso

print(columnas, filas)

m = [[0] * filas] * columnas

for i in range(filas):
    for j in range(columnas):
        m[j][i] = random.randint(1,100)


print(m)