
from collections import deque

'''creacion de lista/diccionario'''

names=[]
names =  ['Alexs','Monica','Juan','David','Juan']


'''menu de opciones'''

while True:
    print("***Menu prncipal***\n")
    print("1. listas\n")
    print("2. listas como colas y compresion de listas.\n")
    print('3. Conjuntos\n')
    print('4. Diccionarios\n')
    opc=input("ingrese una opcion: ")
    if opc=="1":
        print('\n')
        print('lista inicial: ',names)
        print('\n')
        print('cantidad de veces que se repite Juan:',names.count('Juan'))
        print('\n')
        print('Posicion del nombre "Juan": ',names.index('Juan'))
        print('\n')
        print('Posicion del nombre "Juan" a partir de la posicion 4: ',names.index('Juan',4))
        print('\n')
        names.reverse()
        print('alterar el orden de la lista: ',names)
        print('\n')
        names.append('Diego')
        print('se agrega el nombre "Diego": ',names)
        print('\n')
        names.insert(2,'Manuel')
        print('se agrega un nuevo dato en la posicion indicada: ',names)
        print('\n')
        names.extend(['Maria'])
        print('Se agrega un nuevo dato y se extiende la lista (extend)',names)
        print('\n')
        names.sort()
        print('se ordenan alfabeticamente los elementos de la lista/sort',names)
        print('\n')
        names.pop(2)
        print('Se elimina un elemento de la lista/pop: ',names)

    elif opc=="2":

        print("Usando listas como colas: \n")
        lst = deque(["Computador", "Celular", "Televisor"])
        lst.append("Consola")          
        print('Se agrega nuevo dato: \n',lst)
        lst.append("Nevera")          
        print('Se agrega nuevo dato: \n',lst)
        lst.popleft()                 # The first to arrive now leaves
        print('Se elimina el primer elemento que se agregó: \n',lst)
        lst.popleft()                 # The second to arrive now leaves
        print('Se elimina el segundo elemento que se agregó: \n',lst)

#compresion de listas

        print('Compresion de listas:')    
        cubes = []
        for x in range(10):     cubes.append(x**3)
        print('Lista de cubos generados de 1 a 10: \n',cubes)  

    elif opc =="3":
        print('Conjuntos: \n')
        print('Se crea un conjunto de numeros:')
        num = {'18', '15', '20', '12', '3', '5'}
        print(num,'\n')  
        print('Se encuentra el numero 15 en el conjunto? \n')                    
        print('15' in num,'\n')    
        print('Se encuentra el numero 33 en el conjunto? \n') 
        print('33' in num,'\n')   

    elif opc =="4":
        print("Diccionarios:") 

    else:
        print('Opcion no valida')           