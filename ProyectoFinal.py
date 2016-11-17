#!/usr/local/bin/python3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


FUNCIONES


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def Menu():
    
    terminar=False
    conjuntosEstablecidos=False
    
    while(terminar==False):
        print("____Calculadora de Conjuntos_____\n")
        print("Selecciona una opcion: \n")
        print("1. Introduce nuevos conjuntos")
        print("2. Realiza operacion con conjuntos")
        print("3. Salir")
        respuesta=input("Tu seleccion: ")

        if(respuesta=="1"):
            
            U=CrearUniverso()
            A=CrearConjunto(U,"A")
            B=CrearConjunto(U,"B")
            print("\n")
            conjuntosEstablecidos=True
       
        elif(respuesta=="2" and conjuntosEstablecidos==False):
            print("Primero introduce nuevos conjuntos para poder realizar operaciones")
            print("\n")

        elif(respuesta=="2"):
            interseccion,soloA,soloB,union = Operaciones(A,B,U)
            A_complemento = Complemento(A,U)
            B_complemento = Complemento (B,U)
            cPotencia = Potencia(U)
            print("Los resultados son:\n")
            ImprimirConjunto(interseccion,"A Interseccion B")
            ImprimirConjunto(soloA,"A - B")
            ImprimirConjunto(soloB,"B - A")
            ImprimirConjunto(union,"A U B")
            ImprimirConjunto(A_complemento,"A Complemento")
            ImprimirConjunto(B_complemento,"B Complemento")
            print ("Conjunto potencia Universo")
            for combination in Potencia(U):
                print(combination)
            print("\n")
            
        elif(respuesta=="3"):
            terminar=True

        else:
            print("Opcion no valida, escoje un numero entre 1 y 3")
            print("\n")


##Con esta funcion se crea el conjunto universo##
def CrearUniverso():
    U = input("Introduce los elementos del universo separados por comas: \n")
    input_list = U.split(',')
    universo = [x.strip() for x in input_list]
    return universo

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
    cT = [' '] * len(cA)
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
    cI=[' ']*index

    #Obtiene la interseccion de A y B
    for i in range(index):
        cI[i]=cT[i]
    #Obtiene A union B
    cU = cA+cI+cB
    return cI, cA, cB, cU

##Esta funcion devuelve el complemento de un conjunto dado
def Complemento (cA,universo):
    cR=[' ']*(len(universo)-len(cA))
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

##Esta Funcion Imprime los conjuntos##
def ImprimirConjunto(conjunto,nombre_del_conjunto):
    print(nombre_del_conjunto)
    for i in range(len(conjunto)):
        if(i<len(conjunto)-1):
            print(conjunto[i],", ",end="")
        else:
            print(conjunto[i])
    print()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


MAIN


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Menu()

