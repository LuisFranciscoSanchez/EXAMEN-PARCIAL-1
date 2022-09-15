import numpy as np

#Captura de datos
m = int(input("Ingresa la dimensión de una matriz: "))
s = (m,m)
mtx = np.zeros(s)

#Creación de vector con números primos
n = 1000*m
vec = []
for p in range (1, n):
    count = 0 
    for j in range(2, (p//2 + 1)):
        if(p % j == 0):
            count = count + 1
            break
    if (count == 0 and p != 1):
        vec.append(p)
a = len(vec)-m**2
vec = vec[:-a]

#Sustitución en matriz cuadrada

print("\n Matriz cuadrada de números primos: \n")
rshp = np.reshape(vec,(m,m))
t=""
for i in range (len(rshp)):
    for j in range (len(rshp)):
        t = t + str(rshp[i][j]) +"	"    
    t = t + "\n"
print(t)

#Suma de diagonal superior

d = np.triu(rshp,0)
suma = sum(sum(d))
print("\n La suma de todos los elementos en y por encima de la diagonal principal es: ",suma)
        
