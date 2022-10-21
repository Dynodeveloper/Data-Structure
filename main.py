import math
from collections import deque

'''creacion de lista/diccionario'''

names = ['Alexs', 'Monica', 'Juan', 'David', 'Juan']
num = {'18', '15', '20', '12', '3', '5'}
lst = deque(["Computador", "Celular", "Televisor"])
dic = {'game-1': 2056, 'game-2': 1256}
d2 = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
    ]
trasponer=[]
a = [-1, 1, 66.25, 333, 333, 1234.5]
knights = {'Nick': 'the Stronger', 'Monik': 'the queen'}
qs = ['name', 'quest', 'favorite color']
an = ['Cesar', 'the snake eater', 'black']
dat = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filt_dat = []


'''menu de opciones'''

while True:
    print("***Menu principal***\n")
    print("1. listas\n")
    print("2. listas como colas y compresion de listas.\n")
    print('3. Conjuntos\n')
    print('4. Diccionarios\n')
    opc = input("ingrese una opcion: ")
    if opc == "1":
        print('\n')
        print('lista inicial: ', names)
        print('\n')
        print('cantidad de veces que se repite Juan:', names.count('Juan'))
        print('\n')
        print('Posicion del nombre "Juan": ', names.index('Juan'))
        print('\n')
        print('Posicion del nombre "Juan" a partir de la posicion 4: ',
              names.index('Juan', 4))
        print('\n')
        names.reverse()
        print('alterar el orden de la lista: ', names)
        print('\n')
        names.append('Diego')
        print('se agrega el nombre "Diego": ', names)
        print('\n')
        names.insert(2, 'Manuel')
        print('se agrega un nuevo dato en la posicion indicada: ', names)
        print('\n')
        names.extend(['Maria'])
        print('Se agrega un nuevo dato y se extiende la lista (extend)', names)
        print('\n')
        names.sort()
        print('se ordenan alfabeticamente los elementos de la lista/sort', names)
        print('\n')
        names.pop(2)
        print('Se elimina un elemento de la lista/pop: ', names)

    elif opc == "2":

        print("Usando listas como colas: \n")
        lst.append("Consola")
        print('Se agrega nuevo dato: \n', lst)
        lst.append("Nevera")
        print('Se agrega nuevo dato: \n', lst)
        lst.popleft()                 # el primero en agregarse se elimina
        print('Se elimina el primer elemento que se agregó: \n', lst)
        lst.popleft()                 # el siguiente en agregarse se elimina
        print('Se elimina el segundo elemento que se agregó: \n', lst)
        print('intruccion DEL\n')
        del a[0]
        print('se elimina en base al indice, en este caso el primer elemento:\n',a)
        del a[:]
        print('se elimina todo el contenido de la lista:\n',a)
        print('este metodo tambien permite eliminar vaariables enteras')
        del a


# compresion de listas

        print('Compresion de listas:\n')
        cubes = []
        for x in range(10):
            cubes.append(x**3)
        print('Lista de cubos generados de 1 a 10: \n', cubes)
        cubes = list(map(lambda x: x**2, range(10)))
        print('otra opcion:',cubes)
        vc = [-3, -5, 0, 3, 5]
           # crear una nueva lista con valores doblados
        [x*2 for x in vc]
        print('lista con valores doblados:\n',vc)
         # filter the list to exclude negative numbers
        [x for x in vc if x >= 0]
        print('filtro de negativos:\n',vc)
         # apply a function to all the elements
        [abs(x) for x in vc]
        [[row[i] for row in d2] for i in range(4)] #Creará listas con las filas basadas en las columnas
        print('trasponer listas y columnas:\n',d2)
        for i in range(4):
         trasponer.append([row[i] for row in d2])
        print('almacenar trasposicion en una nueva lista:\n',trasponer)
        #uso de una funcion para la misma tarea
        list(zip(*d2))
        print('ejemplo pero usando la funcion zip:\n',d2)


    elif opc == "3":
        print('Conjuntos: \n')
        print('Se crea un conjunto de numeros:')
        print(num, '\n')
        print('Se encuentra el numero 15 en el conjunto? \n')
        print('15' in num, '\n')
        print('Se encuentra el numero 33 en el conjunto? \n')
        print('33' in num, '\n')

    elif opc == "4":
        print("Diccionarios: \n")

        print('Creacion de Diccionario: ', dic)
        print('\n se agrega nuevo elemento al diccionario:')
        dic['game-3'] = 2501
        print(dic)
        print('\nEliminacion de un dato')
        del dic['game-1']
        print(dic)
        print('\n Se encuentra game-2 en el diccionario?')
        print('game-2' in dic)
        print('se permite crear diccionarios con la sentencia dict\n')
        dict([('n1', 4129), ('n2', 4357), ('n3', 4689)])
        print('tecnicas de iteracion')
        for k, v in knights.items():
         print(k, v)
        print('la iteracion permite unificar clave y valor\n') 
        for i, v in enumerate(['tic', 'tac', 'toe']):
          print(i, v)
        print('con la funcion enumerate y la iteracion permite convertirlo en una secuencia:\n')
        for q, a in zip(qs, an):
         print('What is your {0}?  It is {1}.'.format(q, a))
        print('\ncon la funcion zip se puede iterar sobre dos o mas listas al tiempo\n')
        for i in reversed(range(1, 10, 2)):
          print(i)
        print('con la funcion reversed y la secuencia en orden se puede iterar en orden contrario\n')  
        for i in sorted(names):
           print(i)
        print('se puede iterar sobre una secuencia ordenada y con la funcion sorted devolver una nueva sin cambiar la original\n')   
        for value in dat:
            if not math.isnan(value):
                  filt_dat.append(value)
        print('si se desea cambiar una lista mientrs está siendo iterada es mas conveniente crear una lista nueva:\n',filt_dat)           
    else:
        print('Opcion no valida')
