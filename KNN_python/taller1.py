import pandas as pd
import numpy as np
import random
dataset  = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

mat_dataset = np.array(dataset)

#cuantos datos usaremos para el entrenamiento, input usuario -> 105
training_size = 105

mat_entrenamiento = np.empty((0, 5))



for i in range (0, training_size):
    aleatorio = random.randint(0, len(mat_dataset)-1)
    #print("numero aleatoio: ", aleatorio)
    mat_entrenamiento = np.vstack([mat_entrenamiento, mat_dataset[aleatorio]])
    mat_dataset = np.delete(mat_dataset, aleatorio, axis=0)

mat_prueba = mat_dataset

print("La matriz de entrenamiento (tamaño ", len(mat_entrenamiento), ") es: \n", mat_entrenamiento)
print("\nla matriz de prueba (tamaño ", len(mat_prueba), ") es: \n", mat_prueba)

##print(mat_dataset)
