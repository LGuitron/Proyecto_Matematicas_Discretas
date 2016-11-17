##Funciones##
    ##Validacion
"""def ConjuntoValido(universo):
    ""valida los elementos introducidos en el conjunto A
    en relacion con los elementos de U""
    conjuntoValido = False
    while (conjuntoValido==False):

        A = input("Introduce los elementos del conjunto A: \n")

        #Guardar los elementos en el array separado por comas
        input_list = A.split(',')
        cG = [x.strip() for x in input_list]

        for i in range(len(cG)):
            existe = False
            for j in range(len(universo)):
                if cG[i]==universo[j]:
                    existe=True

            if(existe==False):
                print("El conjunto A no es subconjunto de U")
                conjuntoValido=False
                break
            conjuntoValido=True
    return cU
"""
##Intersecion
def Div(cA,cB, universo):
    index=0
    cT = [A] * len(cA)
    
    for i in range(len(cA)-index):
        for j in range(len(cB)-index):
            if(cA[i]==cB[j]):
                cT[index]=cA[i]
                index+=1
                del cA[i]
                del cB[j]
                i -= 1
                j -= 1
                break               
    cI=[A]*index
    for i in range(index):
        cI[i]=cT[i]
    return cI, cA, cB

##Union
def Union(cA,cB):
    cI=Interseccion(cA,cB)
    cU = len(cA) + len(cB) - len(cI)

##Impresiones
        #A
def printA(cA):
    for i in range(len(cA)):
        print(cA[i])
        
        #B
def printB(cB):
    for i in range(len(cB)):
        print(cB[i])

        #I
def printI(cI):
    for i in range(len(cI)):
        print(cI[i])
    

U = input("Introduce los elementos del universo \n")
input_list = U.split(',')
universo = [x.strip() for x in input_list]

##Validar
#cU = ConjuntoValido(universo)
#cU = ConjuntoValido(universo)
## bubble sort 
"""
valida los elementos introducidos en el conjunto A
    en relacion con los elementos de U"""
conjuntoValido=False

while (conjuntoValido==False):

    A = input("Introduce los elementos del conjunto A: \n")
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

"""valida los elementos introducidos en el conjunto B
en relacion con los elementos de U"""
conjuntoValido=False

while (conjuntoValido==False):

    B = input("Introduce los elementos del conjunto B: \n")
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


cI,cA,cB = Div(cA,cB, universo)
##Interseccion
print("Interseccion")
printI(cI)

##diferencia
    #A
print("Solo A")
printA(cA)

    #B
print("Solo B")
printB(cB)

##complemento
    #A
print("Complemento A")
print(cB)
"""Falta imprimr lo que esta afuera, en el unvierso"""

    #B
print("Complemento B")
print(cA)


##potencia

