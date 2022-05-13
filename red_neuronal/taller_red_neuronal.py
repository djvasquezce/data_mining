import numpy as np
import pandas as pd
import random
from math import e

def inicializar(lista1, lista2):
    for i in range(0, 27):
        if i < 21:
            aleatorio = random.uniform(-1.5, 1.5)
            lista1.append(aleatorio)
        else:
            aleatorio = random.uniform(-1.5, 1.5)
            lista2.append(aleatorio)
    return lista1, lista2

def calcular_input_output_nodos(me, fme, p, t, i_n, o_n):
    for x in range(0,6):
        if x == 0:
            i_n[x] = ((me[fme][0]*p[0]) + (me[fme][1]*p[1]) + (me[fme][2]*p[2]) + (me[fme][3]*p[3]) + t[0])
            #print(me[fme][0], me[fme][1], me[fme][2],me[fme][3])
            o_n[x] = (1/(1+e**(-i_n[x])))
        if x == 1:
            i_n[x] = ((me[fme][0]*p[4]) + (me[fme][1]*p[5]) + (me[fme][2]*p[6]) + (me[fme][3]*p[7]) + t[1])
            o_n[x] = (1/(1+e**(-i_n[x])))
        if x == 2:
            i_n[x] = ((me[fme][0]*p[8]) + (me[fme][1]*p[9]) + (me[fme][2]*p[10]) + (me[fme][3]*p[11]) + t[2])
            o_n[x] = (1/(1+e**(-i_n[x])))
        if x == 3:
            i_n[x] = ((o_n[0]*p[12]) + (o_n[1]*p[13]) + (o_n[2]*p[14]) + t[3])
            o_n[x] = (1/(1+e**(-i_n[x])))
        if x == 4:
            i_n[x] = ((o_n[0]*p[15]) + (o_n[1]*p[16]) + (o_n[2]*p[17]) + t[4])
            o_n[x] = (1/(1+e**(-i_n[x])))
        if x == 5:
            i_n[x] = ((o_n[0]*p[18]) + (o_n[1]*p[19]) + (o_n[2]*p[20]) + t[5])
            o_n[x] = (1/(1+e**(-i_n[x])))
    return i_n, o_n

# ---------------MAIN-----------------------------------------------------
dataset = pd.read_csv(
    "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

# datos a una matriz
mat_dataset = np.array(dataset)

training_size = 105  # int(input("Ingrese valor: "))

mat_entrenamiento = np.empty((0, 5))

for i in range(0, training_size):
    aleatorio = random.randint(0, len(mat_dataset) - 1)
    mat_entrenamiento = np.vstack([mat_entrenamiento, mat_dataset[aleatorio]])
    mat_dataset = np.delete(mat_dataset, aleatorio, axis=0)

mat_prueba = mat_dataset
me = mat_entrenamiento
#---

#lista pesos
lista_pesos = []
#lista tetta
lista_tetta =[]

lista_pesos, lista_tetta = inicializar(lista_pesos, lista_tetta)
print(len(lista_pesos))
print(len(lista_tetta))

#lista intup nodos
input_nodos = [0,0,0,0,0,0]
#lista output nodos
output_nodos = [0,0,0,0,0,0]

#error de cada nodo
err_n = [-1, -1, -1, -1, -1, -1]
'''pesos:
[0] w15
[1] w25
[2] w35
[3] w45
[4] w16
[5] w26
[6] w36
[7] w46
[8] w17
[9] w27
[10] w37
[11] w47
[12] w58
[13] w68
[14] w78
[15] w59
[16] w69
[17] w79
[18] w5 10
[19] w6 10
[20] w7 10
'''
print(lista_pesos)
print(lista_tetta)
for i in range(0, len(me)):
    print("\nInteración ", i+1, "\n")
    input_nodos, output_nodos =calcular_input_output_nodos(mat_entrenamiento, i, lista_pesos, lista_tetta, input_nodos, output_nodos)
    
    
    print(input_nodos)
    print(output_nodos)
    
