import xdrlib
import pandas as pd
import numpy as np
import random
import math

dataset  = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

mat_dataset = np.array(dataset)

#cuantos datos usaremos para el entrenamiento, input usuario -> 105
training_size = 105#int(input("Ingrese valor: "))

mat_entrenamiento = np.empty((0, 5))

for i in range (0, training_size):
    aleatorio = random.randint(0, len(mat_dataset) - 1)
    mat_entrenamiento = np.vstack([mat_entrenamiento, mat_dataset[aleatorio]])
    mat_dataset = np.delete(mat_dataset, aleatorio, axis=0)

mat_prueba = mat_dataset




def k_menores_y_respuesta(mat_dist, k):
    #print(mat_dist)
    mat_dist = mat_dist[mat_dist[:, 0].argsort()] #ordenados la columna 0
    print("--------------")
    print(mat_dist)

    for i in range (0, k):
        None

    


# e -> mat_entrenamiento p -> mat_prueba
def calcular_distancias(e, p, k):
    print("\nLa tupla es: " , p, "\n")
    lis_distancias = []
    mat_distancias =np.empty((0, 2))
    for x in range (0, len(e)):
        distancia = math.sqrt((e[x][0]-p[0])**2 + (e[x][1]-p[1])**2 + (e[x][2]-p[2])**2 + (e[x][3]-p[3])**2 )
        distancia = round(distancia, 6)
        lis_distancias.append(distancia)
        fila = [distancia, e[x][4]]
        mat_distancias = np.r_[mat_distancias,[fila]]
        
    #print(mat_distancias)
    aux = pd.DataFrame(mat_distancias, columns=['distancia', 'etiqueta'])
    #print(aux)
    aux[['distancia']] = aux[['distancia']].astype(float)
    mat_distancias = np.array(aux)
    #print(mat_distancias)
    k_menores_y_respuesta(mat_distancias, k)
    
    # [6.3 3.3 6.0 2.5 'Virginica'] entrenamiento

    # [4.5 2.3 1.3 0.3 'Setosa'] prueba

k =5

print("La matriz de entrenamiento (tamaño ", len(mat_entrenamiento), ") es: \n", mat_entrenamiento)
print("\nla matriz de prueba (tamaño ", len(mat_prueba), ") es: \n", mat_prueba)

calcular_distancias(mat_entrenamiento, mat_prueba[0], k)
#for i in range(0, len(mat_prueba)):
    #calcular_distancias(mat_entrenamiento, mat_prueba[i], k)

'''print("Y LA MATRIZ ORIGINAL ES")

for i in range(0, len(mat_entrenamiento)):
    print(mat_entrenamiento[i][4], end= "  ")'''



#calcular la distancia de cada uno de los elemntos de mat prueba con todos los elementos de mat entrenemiento,
#indice y distancia en un arreglo 
#ordenarlas,y encontrar las k menores (menores distancias)
#cuantas cuincidencias hay con las etiquetas, y preuba si la categoría con más coincidencia es la misma que la mat prieba original

