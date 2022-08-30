'''
Algoritmo de despacho FIFO
Sarah Sofia Palacio
Sistemas Operativos
'''
rafaga = 0
TE = 0
TS = 0

datos = int(input("Introduzca el numero de procesos: "))
print("Por favor introduzca todos los datos como enteros")
print("           columna   columna    columna")
print("              1    |    2    |     3")
print("          -----------------------------")
print("Fila    1 |        |         |")
print("Fila    2 |        |         |")
print("Fila    N |        |         |")
print()

matriz = []
for i in range(datos):
    matriz.append([])
    for j in range(3):
        valor = int(input("fila {}, columna {} : ".format(i+1, j+1) ))
        matriz[i].append(valor)

matriz.sort(key=lambda x:x[2])

for i in range(datos):
    TE += rafaga - matriz[i][2] 
    rafaga += matriz[i][1]
    TS += rafaga - matriz[i][2]

print(matriz)
print(TE/datos)
print(TS/datos)