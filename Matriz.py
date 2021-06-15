print("///Multiplicacion de matrizes///")
print ("Ingreso de dimensiones")
filas=int(input("ingresa el numero de filas: "))
columna_1= int(input("ingresa el numero de columnas de la primera matriz: "))
columna_2 =int (input("Ingresa el numero de columnas de la segunda matriz: "))
#Creacion de la Matriz 1
print (" ")
print ("------- Matriz 1 -------")
print (" ")
M1=[]
for i in range (filas):
    M1.append ([0]*columna_1)
    print (M1[i])
#Creacion de la Matriz 2 
print (" ")
print ("------- Matriz 2 -------")
print (" ")
M2=[]
for i in range (columna_1):
    M2.append ([0]*columna_2)
    print (M2[i])
print (" ")
print ("Ingresa los valores de la primera matriz 1")
print (" ")

#Intercambio de valores en la primera matriz 1
for i in range (filas):
    for j in range (columna_1):
        M1[i][j]=float(input("Introduce los valores en (%d, %d): "  %(i,j)))
print (" ")
print ("------- Valores ingresados en la matriz 1 -------")
print (" ")
for i in range (filas):
    print (M1[i])

print (" ")
print ("Ingresa los valores de la primera matriz  2") 
print (" ")
#Intercambio de valores en la primera matriz 2

for i in range (columna_1):
    for j in range (columna_2):
        M2[i][j]=float(input("Ingrese los valores en (%d,%d) : " %(i,j)))
print (" ")
print ("------- Valores ingresados en la matriz 2 -------")
print (" ")
for i in range (columna_1):
    print (M2[i])
print (" ")
print ("----- MULTIPLICACION -----") 
print (" ")
#Matriz de resultado
R=[]
for i in range (filas):
    R.append([0]*columna_2)
    
#MULTIPLICACION
for i in range (filas):
    for j in range (columna_2):
            for k in range (columna_1):
                R[i][j] += M1 [i] [k] * M2 [k] [j]

for i in range (filas):
    M=[]
    for j in range (columna_2):
        M.append(R[i][j])
    print (M)
