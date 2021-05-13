import numpy as np
from math import *

def mostrarMatriz(M,f,c):
    print()
    print("Matriz")
    for i in range(f):
        for j in range(c):
            print(M[i][j],end="  ")
        print()

def ingresarMatriz(M,f,c):
    for i in range(f):
        for j in range(c):
            M[i][j]=float(input("Ingrese valor: "))

def maximoDeSumaColumna(M,f,c):
    L=[]
    for j in range(c):
        suma=0
        for i in range(f):
            suma=suma+abs(M[i][j])

        L.append(suma)

    maximo=L[0]
    for i in range(c):
        if L[i]>maximo:
            maximo=L[i]
    return maximo
    
def maximoDeMatrizInversa(M,f,c):
    #invirtiendo la matriz
    MxInversa=[]
    for i in range(f):
        MxInversa.append([0]*c)
    
    MxInversa=np.linalg.inv(M)
    #print( np.linalg.inv(M))


    #positivizando los elementos de la matriz
    MxInversaAbs=[]
    for i in range(f):
        MxInversaAbs.append([0]*c)
    for i in range(f):
        for j in range(c):
            MxInversaAbs[i][j]=abs(MxInversa[i][j])
    
    #buscando el la columna de la matriz positivizada
    L2=[]
    for j in range(c):
        suma=0
        for i in range(f):
            suma=round(suma+MxInversaAbs[i][j],4)

        L2.append(suma)

    maximo2=L2[0]
    for i in range(c):
        if L2[i]>=maximo2:
            maximo2=L2[i]
    return maximo2

def NumCondicion_Norma_Uno():
    normaUno=maximoDeSumaColumna(M,f,c)*maximoDeMatrizInversa(M,f,c)
    return normaUno


def Norma_Infinita(M,f,c):

    L3=[]
    for i in range(f):
        suma=0
        for j in range(c):
            suma=suma+abs(M[i][j])

        L3.append(suma)

    maximo3=L3[0]
    for i in range(f):
        if L3[i]>maximo3:
            maximo3=L3[i]
    return maximo3


def NumCondicion_Norma_Infinita():
    condicionNinfinita=Norma_Infinita(M,f,c)*maximoDeMatrizInversa(M,f,c)
    return condicionNinfinita

def Norma_Dos():
    resultado=Norma_Infinita(M,f,c)*maximoDeSumaColumna(M,f,c)
    normaDos=sqrt(resultado)
    return normaDos
def NumCondicion_Norma_Dos():
    condicionNdos=Norma_Dos()*maximoDeMatrizInversa(M,f,c)
    return condicionNdos

f=int(input("Ingrese numero de filas:  "))
c=int(input("Ingrese numero de columnas:  "))
M=[]
for i in range(f):
    M.append([0]*c)

Minversa=[]
for i in range(f):
    Minversa.append([0]*c)
#print(M)
ingresarMatriz(M,f,c)
mostrarMatriz(M,f,c)
#print("El maximo de la columna es:")
#print(maximoDeSumaColumna(M,f,c))

print(  )
#print("El maximo(absoluto y luego suma de columna)es : ")
#Minversa=matrizInversa(M,f,c)
#mostrarMatriz(Minversa,f,c)



print("Numero de condicion con Norma Uno: ",NumCondicion_Norma_Uno())
print("Numero de condicon con Norma Infinita: ",NumCondicion_Norma_Infinita())
print("Numero de condicio con Norma Dos: ",NumCondicion_Norma_Dos())
#print("Norma infinta",Norma_Infinita(M,f,c))
#print("halllzazgoo",maximoDeMatrizInversa(M,f,c))
print("Norma 2:",Norma_Dos())


print(maximoDeMatrizInversa(M,f,c))