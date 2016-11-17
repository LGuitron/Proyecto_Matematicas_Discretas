#!/usr/bin/python3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


FUNCIONES


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Funcion para menu
def Menu():
    
    terminar=False
    conjuntosEstablecidos=False
    
    while(terminar==False):
        print("____Calculadora de Conjuntos_____\n")
        print("Selecciona una opcion: \n")
        print("1. Introduce nuevos conjuntos")
        print("2. Realiza operacion con conjuntos")
        print("3. Ver conjuntos A,B y U")
        print("4. Salir")
        respuesta=input("Tu seleccion: ")

        if(respuesta=="1"):
            U=CrearUniverso()
            A=CrearConjunto(U,"A")
            B=CrearConjunto(U,"B")
            print("\n")
            conjuntosEstablecidos=True
            
        elif((respuesta=="2" or respuesta=="3") and conjuntosEstablecidos==False):
            print("Debes introducir nuevos conjuntos para realizar esta seleccion")
            print("\n")

        elif(respuesta=="2"):
            SeleccionarOperacion(A,B,U)
            
        elif(respuesta=="3"):
            ImprimirConjunto(A,"A")
            ImprimirConjunto(B,"B")
            ImprimirConjunto(U,"U")
            
        elif(respuesta=="4"):
            terminar=True

        else:
            print("Opcion no valida, escoje un numero entre 1 y 3")
            print("\n")

#Funcion para elegir operacion de conjuntos
def SeleccionarOperacion(A,B,U):
    
    print("Selecciona la operacion que quieres realizar: \n")
    print("1. A ∩ B")
    print("2. A ∪ B")
    print("3. A - B")
    print("4. B - A")
    print("5. Complemento A")
    print("6. Complemento B")
    print("7. Potencia A")
    print("8. Potencia B")
    print("9. Potencia U \n")
    respuesta=input("Tu seleccion: ")

    #Imprime resultados
    if(respuesta=="1"):
        ImprimirConjunto(Interseccion(A,B),"A ∩ B")       
    elif(respuesta=="2"):
        ImprimirConjunto(Union(A,B),"A ∪ B")    
    elif(respuesta=="3"):
        ImprimirConjunto(Diferencia(A,B),"A - B")  
    elif(respuesta=="4"):
        ImprimirConjunto(Diferencia(B,A),"B - A")  
    elif(respuesta=="5"):
        ImprimirConjunto(Complemento(A,U),"Complemento A")    
    elif(respuesta=="6"):
        ImprimirConjunto(Complemento(B,U),"Complemento B")   
    elif(respuesta=="7"):
        ImprimirPotencia(A,"Conjunto potencia A")  
    elif(respuesta=="8"):
        ImprimirPotencia(B,"Conjunto potencia B")     
    elif(respuesta=="9"):
        ImprimirPotencia(U,"Conjunto potencia U")       
    else:
        print("Opcion no valida")

#Funcion que crea el conjunto universo
def CrearUniverso():
    U = input("Introduce los elementos del universo separados por comas: \n")
    input_list = U.split(',')                                                          #Distingue elementos separados por comas
    universo = [x.strip() for x in input_list]  
    universo=QuitarRepetidos(universo)                                                 
    return universo

#Funcion que crea y valida los conjuntos A y B
def CrearConjunto(universo , nombre_conjunto_nuevo):
    conjuntoValido=False
    
    TextoInput1="Introduce los elementos del conjunto "
    TextoInput2=" separados por comas : \n"
    TextoInput=TextoInput1+nombre_conjunto_nuevo+TextoInput2                            #Concatena nombre escogido para el conjunto
    
    while (conjuntoValido==False):
        conjuntoNuevo = input(TextoInput)
        input_list = conjuntoNuevo.split(',')                                           #Distingue elementos separados por comas
        conjuntoNuevo = [x.strip() for x in input_list]

        for i in range(len(conjuntoNuevo)):
            existe = False
            for j in range(len(universo)):                  
                if conjuntoNuevo[i]==universo[j]:                                       #Verifica que cada elemento del nuevo conjunto esté en U       
                    existe=True
            if(existe==False):                                                          #Si algun elemento no esta se debe volver a introducir el conjunto
                print("El conjunto ",nombre_conjunto_nuevo ," no es subconjunto de U")  
                conjuntoValido=False
                break
            conjuntoValido=True
            
    conjuntoNuevo=QuitarRepetidos(conjuntoNuevo)                                        #Se eliminan elementos repetidos
    return conjuntoNuevo

#Funcion que elimina elementos repetidos de un conjunto
def QuitarRepetidos(cA):
    i=0
    j=0
    while i<len(cA):
        j=0
        while j<len(cA):
            if(i!=j and cA[i]==cA[j]):                              #Encuentra elementos iguales con diferente indice
                del cA[j]                                           #Elimina una de las repeticiones
                i = 0                                               #Se reinician ambos contadores para mantener el orden original
                j = 0
            j+=1
        i+=1
    return cA

def Diferencia(Minuendo,Sustraendo):
    resultado=Minuendo[:]                                            #Se hace una copia del minuendo
    for i in range(len(resultado)):
        for j in range(len(Sustraendo)):
            if(i<len(resultado) and resultado[i]==Sustraendo[j]):    #Verifica que no se salga del arreglo al reducir su tamaño
                resultado.remove(resultado[i])                       #Quita elementos comunes en resultado
    return resultado

def Interseccion(cA,cB):
    resultado=[]
    for i in range(len(cA)):
        for j in range(len(cB)):
            if(cA[i]==cB[j]):                   #Inserta elementos comunes en resultado
                resultado+=cA[i]
    return resultado

def Union(cA,cB):
    resultado=[]
    for i in range(len(cA)):
        resultado+=[cA[i]]                      #Agrega todos los elementos de A
    for i in range(len(cB)):    
        resultado+=[cB[i]]                      #Agrega todos los elementos de B
    resultado=QuitarRepetidos(resultado)        #Quita repetidos
    return resultado

#Funcion para complemento de un conjunto
def Complemento (cA,universo):
    cR=[]
    for i in range(len(universo)):
        elementoEncA = False
        for j in range(len(cA)):
            if(cA[j]==universo[i]):             #Se verifica si un elemento en cA esta en cU
                elementoEncA=True               
        if(elementoEncA==False):                #Si no está es agregado al complemento
            cR+=universo[i]
    return cR

#Funcion para conjunto potencia de un conjunto
def Potencia(cA):
    for i in range(0,2**len(cA)):           #Hay 2^n combinaciones
        bin_comb = bin(i)[2:].zfill(len(cA))#Pasar a binario y agregar 0s izq
        combination = []                    #Combinacion que se agregara                 
        for j in range(0,len(bin_comb)):   
            if bin_comb[j]=='1':            #Si hay 1 agregar ese elemento
                combination+=[cA[j]]
        yield combination                   #Regresamos esa combinacion

#Funcion para imprimir conjuntos
def ImprimirConjunto(conjunto,nombre_del_conjunto):
    print(nombre_del_conjunto)
    print("[",end="")
    for i in range(len(conjunto)):
        if(i<len(conjunto)-1):
            print(conjunto[i],",",end="")       #Imprime con coma si no es el ultimo elemento
        else:
            print(conjunto[i],end="] \n")       
    
#Funcion para imprimir conjunto potencia
def ImprimirPotencia(cA,nombre_del_conjunto):
    print (nombre_del_conjunto)
    for combination in Potencia(cA):
        print(combination)
    print("\n")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


MAIN


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Menu()

