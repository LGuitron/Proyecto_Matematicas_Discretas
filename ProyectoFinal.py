#!/usr/local/bin/python3

##Variables##
conjuntoValido=False

##Funciones##
##Esta funcion devuelve 4 conjuntos##
##(A-B), (B-A), (A^B), (A U B)
def Operaciones(cA,cB, universo):
    
    index=0
    cT = [A] * len(cA)
    i=0
    j=0

    #Obtiene (A-B) y (B-A) en estos ciclos
    while i<len(cA):
        j=0
        while j<len(cB):
            if(cA[i]==cB[j]):
                cT[index]=cA[i]
                index+=1
                del cA[i]
                del cB[j]
                i = 0
                j = 0
                break
            j+=1
        i+=1
    cI=[A]*index

    #Obtiene la interseccion de A y B
    for i in range(index):
        cI[i]=cT[i]

    #Obtiene A union B
    cU = cA+cI+cB
    
    return cI, cA, cB, cU

##Esta funcion devuelve el complemento de un conjunto dado
def Complemento (cA,universo):
    cR=[A]*(len(universo)-len(cA))
    index=0
    for i in range(len(universo)):
        elementoEncA = False
        for j in range(len(cA)):
            if(cA[j]==universo[i]):
                elementoEncA=True
        if(elementoEncA==False):
            cR[index]=universo[i]
            index+=1   
    return cR

##Esta funcion devuelve el conjunto potencia de un conjunto dado##
def Potencia(cA):
    for i in range(0,2**len(cA)):           #Hay 2^n combinaciones
        bin_comb = bin(i)[2:].zfill(len(cA))#Pasar a binario y agregar 0s izq
        combination = []                    #Combinacion que se agregara                 
        for j in range(0,len(bin_comb)):   
            if bin_comb[j]=='1':            #Si hay 1 agregar ese elemento
                combination+=[cA[j]]
        yield combination                   #Regresamos esa combinacion

##Inputs##
U = input("Introduce los elementos del universo separados por comas: \n")
input_list = U.split(',')
universo = [x.strip() for x in input_list]


#valida los elementos introducidos en el conjunto A
#en relacion con los elementos de U
while (conjuntoValido==False):

    A = input("Introduce los elementos del conjunto A separados por comas : \n")
    input_list = A.split(',')
    cA = [x.strip() for x in input_list]

    for i in range(len(cA)):
        existe = False
        for j in range(len(universo)):
            if cA[i]==universo[j]:
                existe=True
        if(existe==False):
            print("El conjunto A no es subconjunto de U")
            conjuntoValido=False
            break
        conjuntoValido=True


#valida los elementos introducidos en el conjunto B
#en relacion con los elementos de U
conjuntoValido=False

while (conjuntoValido==False):

    B = input("Introduce los elementos del conjunto B separados por comas:  \n")
    input_list = B.split(',')
    cB = [x.strip() for x in input_list]

    for i in range(len(cB)):
        existe = False
        for j in range(len(universo)):
            if cB[i]==universo[j]:
                existe=True
        if(existe==False):
            print("El conjunto B no es subconjunto de U")
            conjuntoValido=False
            break
        conjuntoValido=True

Acomp = Complemento(cA,universo)
Bcomp = Complemento (cB,universo)
cI,cA,cB,cU = Operaciones(cA,cB, universo)

print("A Interseccion B")
for i in range(len(cI)):
    if(i<len(cI)-1):
        print(cI[i],",",end="")
    else:
        print(cI[i])
    
print("A-B")
for i in range(len(cA)):
    if(i<len(cA)-1):
        print(cA[i],",",end="")
    else:
        print(cA[i])
        
print("B-A")
for i in range(len(cB)):
    if(i<len(cB)-1):
        print(cB[i],",",end="")
    else:
        print(cB[i])

print("A Union B")
for i in range(len(cU)):
    if(i<len(cU)-1):
        print(cU[i],",",end="")
    else:
        print(cU[i])

print("A complemento")
for i in range(len(Acomp)):
    if(i<len(Acomp)-1):
        print(Acomp[i],",",end="")
    else:
        print(Acomp[i])

print("B complemento")
for i in range(len(Bcomp)):
    if(i<len(Bcomp)-1):
        print(Bcomp[i],",",end="")
    else:
        print(Bcomp[i])
##potencia
print ("Conjunto potencia Universo")
for combination in Potencia(universo):
    print(combination)


