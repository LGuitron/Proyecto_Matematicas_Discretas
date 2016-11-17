#!/usr/local/bin/python3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


FUNCIONES


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
##Con esta funcion se crean y validan los conjuntos A y B##
def CrearConjunto(universo , nombre_conjunto_nuevo):
    conjuntoValido=False
    
    TextoInput1="Introduce los elementos del conjunto "
    TextoInput2=" separados por comas : \n"
    TextoInput=TextoInput1+nombre_conjunto_nuevo+TextoInput2
    
    while (conjuntoValido==False):
        conjuntoNuevo = input(TextoInput)
        input_list = conjuntoNuevo.split(',')
        conjuntoNuevo = [x.strip() for x in input_list]

        for i in range(len(conjuntoNuevo)):
            existe = False
            for j in range(len(universo)):
                if conjuntoNuevo[i]==universo[j]:
                    existe=True
            if(existe==False):
                print("El conjunto ",nombre_conjunto_nuevo ," no es subconjunto de U")
                conjuntoValido=False
                break
            conjuntoValido=True            
    return conjuntoNuevo

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


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


MAIN


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

U = input("Introduce los elementos del universo separados por comas: \n")
input_list = U.split(',')
universo = [x.strip() for x in input_list]

A=CrearConjunto(U,"A")
B=CrearConjunto(U,"B")

Acomp = Complemento(A,universo)
Bcomp = Complemento (B,universo)
cI,cA,cB,cU = Operaciones(A,B, universo)

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

print ("Conjunto potencia Universo")
for combination in Potencia(universo):
    print(combination)




