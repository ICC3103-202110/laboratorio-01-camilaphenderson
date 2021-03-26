# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 14:41:47 2021

@author: camil
"""

# -*- coding: utf-8 -*-
import random
import numpy as np
ncartas = int(input("Ingrese numero de cartas: "))
a = []
b = []
c = []
d = []

for i in range(ncartas):
    i+=1
    c.append(i)
    a.append(i)
    b.append('*')
    d.append('*')
tablero = []
cartas = []
random.shuffle(c)
cartas.append(c)
random.shuffle(a)
cartas.append(a)
cartas = np.array(cartas)
tablero.append(b)
tablero.append(d)
tablero = np.array(tablero)

         
    

print('la coordenada es solo un numero contando desde el 0 de izquierda a derecha')
print('primera carta es en la linea de arriba, la segunda en la de abajo')

pj1 = 0
pj2 = 0 
ptotal = 0
while ptotal < ncartas:
         ptotal = pj1 + pj2
         print('el tablero esta asi\n', tablero)
         j11 = int(input("jugador 1, ingrese coordenada carta 1")) 
         tablero[0][j11] = cartas[0][j11]
         print(tablero)
         j12 = int(input("jugador 1, ingrese coordenada carta 2")) 
         tablero[1][j12] = cartas[1][j12]
         print(tablero)
         if cartas[0][j11] == cartas[1][j12]:
             while cartas[0][j11] == cartas[1][j12] :
                 pj1 +=1
                 ptotal = pj1 + pj2
                 tablero[0][j11] = " "
                 tablero[1][j12] = " "
                 if ncartas == ptotal:
                     break
                 else: 
                     print(tablero)
                     j11 = int(input("jugador 1, ingrese coordenada carta 1")) 
                     tablero[0][j11] = cartas[0][j11]
                     print(tablero)
                     j12 = int(input("jugador 1, ingrese coordenada carta 2")) 
                     tablero[1][j12] = cartas[1][j12]
                     print(tablero)
         if cartas[0][j11] != cartas[1][j12]:
             tablero[0][j11] = "*"
             tablero[1][j12] = "*"
             print('el tablero esta asi\n', tablero)
             j21 = int(input("jugador 2, ingrese coordenada carta 1"))
             tablero[0][j21] = cartas[0][j21]
             print(tablero)
             j22 = int(input("jugador 2, ingrese coordenada carta 2"))
             tablero[1][j22] = cartas[1][j22]
             print(tablero)
             if cartas[0][j21] == cartas[1][j22]:
                 while cartas[0][j21] == cartas[1][j22]:
                     pj2 +=1
                     tablero[0][j21] = " "
                     tablero[1][j22] = " "
                     print(tablero)
                     j21 = int(input("jugador 2, ingrese coordenada carta 1"))
                     tablero[0][j21] = cartas[0][j21]
                     print(tablero)
                     j22 = int(input("jugador 2, ingrese coordenada carta 2"))
                     tablero[1][j22] = cartas[1][j22]
                     print(tablero)
                     ptotal = pj1 + pj2
                     if ptotal == ncartas:
                         break
             else: 
                 tablero[0][j21] = "*"
                 tablero[1][j22] = "*"
                 
                 continue
if pj1 > pj2:
    print("Gana Jugador 1")
elif pj2 > pj1 :
    print("Gana jugador 2")
else:
    print("empate")
