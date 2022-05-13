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

def calcular_input_output_nodos(me, p, t, i_n, o_n):
    for x in range(0,6):
        if x == 0:
            i_n[x] = ((me[0]*p[0]) + (me[1]*p[1]) + (me[2]*p[2]) + (me[3]*p[3]) + t[0])
            #print(me[0], me[1], me[2],me[3])
            o_n[x] = (1/(1+e**(-i_n[x])))
        if x == 1:
            i_n[x] = ((me[0]*p[4]) + (me[1]*p[5]) + (me[2]*p[6]) + (me[3]*p[7]) + t[1])
            o_n[x] = (1/(1+e**(-i_n[x])))
        if x == 2:
            i_n[x] = ((me[0]*p[8]) + (me[1]*p[9]) + (me[2]*p[10]) + (me[3]*p[11]) + t[2])
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

def calcular_errores(o_n, p, err_n, s1, s2, s3):
    for y in range(0, 6):
        if y == 0: #nodo 10
            err_n[y] = (o_n[5] * (1 - o_n[5]) * (s3 - o_n[5]))
        if y == 1: #nodo 9
            err_n[y] = (o_n[4] * (1 - o_n[4]) * (s2 - o_n[4]))
        if y == 2: #nodo 8
            err_n[y] = (o_n[3] * (1 - o_n[3]) * (s1 - o_n[3]))

        if y == 3: #nodo 7                            #SUMATORIA DE LOS ERRORES???
            err_n[y] = (o_n[2] * (1 - o_n[2]) * (err_n[0]*p[20] + err_n[1]*p[17] + err_n[2]*p[14]))
        if y == 4: #nodo 6                            #SUMATORIA DE LOS ERRORES???
            err_n[y] = (o_n[1] * (1 - o_n[1]) * (err_n[0]*p[19] + err_n[1]*p[16] + err_n[2]*p[13]))
        if y == 5: #nodo 5                             #SUMATORIA DE LOS ERRORES???
            err_n[y] = (o_n[0] * (1 - o_n[0]) * (err_n[0]*p[18] + err_n[1]*p[15] + err_n[2]*p[12]))
    return err_n

def actualizar_pesos(me, lr, p, err_n, o_n):
    i = 0
    j = 0
    for x in range(0, len(p)):
        
        if(x<=3):
            p[x] = p[x] + lr * err_n[5] * me[i]
        elif(x<=7):
            p[x] = p[x] + lr * err_n[4] * me[i]
        elif(x<=11):
            p[x] = p[x] + lr * err_n[3] * me[i]
        elif(x<=14): 
            p[x] = p[x] + lr * err_n[2] * o_n[j]
        elif(x<=17): 
            p[x] = p[x] + lr * err_n[1] * o_n[j]
        elif(x<=20): 
            p[x] = p[x] + lr * err_n[0] * o_n[j]

        
        if(x<=11):   
            if(i<3):
                i = i+1
            else:
                i = 0
                j = 0
        else: 
            if(j<2): 
                j = j+1
            else: 
                j = 0
    return p

# ---------------MAIN-----------------------------------------------------
dataset = pd.read_csv(
    "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

# datos a una matriz
mat_dataset = np.array(dataset)

training_size = 105  # int(input("Ingrese valor: "))
learning_rate = 0.9

mat_entrenamiento = np.empty((0, 5))

for i in range(0, training_size):
    aleatorio = random.randint(0, len(mat_dataset) - 1)
    mat_entrenamiento = np.vstack([mat_entrenamiento, mat_dataset[aleatorio]])
    mat_dataset = np.delete(mat_dataset, aleatorio, axis=0)

mat_prueba = mat_dataset
#---

#lista pesos
lista_pesos = []
#lista tetta
lista_theta =[]

lista_pesos, lista_theta = inicializar(lista_pesos, lista_theta)


#lista intup nodos
input_nodos = [0,0,0,0,0,0]
#lista output nodos
output_nodos = [0,0,0,0,0,0]

#error de cada nodo
error_nodos = [-1, -1, -1, -1, -1, -1]

print(mat_entrenamiento)
for i in range(0, len(mat_entrenamiento)):
    print("\nIteración ", i+1, "\n")

    input_nodos, output_nodos = calcular_input_output_nodos(mat_entrenamiento[i], lista_pesos, lista_theta, input_nodos, output_nodos)
    
    if(mat_entrenamiento[i][4] == "Setosa"):
        error_nodos = calcular_errores(output_nodos, lista_pesos, error_nodos, 1, 0, 0)
    elif (mat_entrenamiento[i][4] == "Versicolor"):
        error_nodos = calcular_errores(output_nodos, lista_pesos, error_nodos, 0, 1, 0)
    elif (mat_entrenamiento[i][4] == "Virginica"):
        error_nodos = calcular_errores(output_nodos, lista_pesos, error_nodos, 0, 0, 1)
    else:
        print("--------------HAY ALGO MAL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    lista_pesos = actualizar_pesos(mat_entrenamiento[i], learning_rate, lista_pesos, error_nodos, output_nodos)
    print(lista_pesos)
    
    
