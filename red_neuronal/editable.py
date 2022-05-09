import pandas as pd
import numpy as np
import random
import math

#list_r -> respuestas dada por el modelo, datos_reales -> mat_prueba
def calcular_precision(list_r, datos_reales):
    aciertos = 0
    errores = 0
    cuales_fallaron = []
    for i in range(0, len(list_r)):
        if(list_r[i] == datos_reales[i][4]):
            aciertos += 1
        else:
            errores += 1
            cuales_fallaron.append(i+1)

    print("\naciertos: ", aciertos)
    print("errores: ", errores)
    print("en las siguientes itereaciones falló el modelo: ", cuales_fallaron)
    precision = (aciertos/len(datos_reales)) * 100
    return float(np.around(precision, 2))

def k_menores_y_respuesta(mat_dist, k):
    #print(mat_dist)
    mat_dist = mat_dist[mat_dist[:, 0].argsort()] #ordenados la columna 0
    #print(mat_dist)
    setosa = 0
    versicolor = 0
    virginica = 0

    for i in range (0, k):
        print(mat_dist[i])
        if(mat_dist[i][1] == "Setosa"):
            setosa+=1
        elif(mat_dist[i][1] == "Versicolor"):
            versicolor+=1
        elif(mat_dist[i][1] == "Virginica"):
            virginica+=1
        
    if(setosa>=versicolor and setosa>=virginica):
        return "Setosa"
    elif(versicolor>=setosa and versicolor>=virginica):
        return "Versicolor"
    elif(virginica>=setosa and virginica>=versicolor):
        return "Virginica"

# e -> mat_entrenamiento p -> mat_prueba
def calcular_distancias(e, p):
    print("La tupla recibida es: " , p, "\n")
    mat_distancias =np.empty((0, 2))
    for x in range (0, len(e)):
        distancia = math.sqrt((e[x][0]-p[0])**2 + (e[x][1]-p[1])**2 + (e[x][2]-p[2])**2 + (e[x][3]-p[3])**2 )
        distancia = round(distancia, 6)
        fila = [distancia, e[x][4]]
        mat_distancias = np.r_[mat_distancias,[fila]]
        
    #print(mat_distancias)
    aux = pd.DataFrame(mat_distancias, columns=['distancia', 'etiqueta'])
    #print(aux)
    aux[['distancia']] = aux[['distancia']].astype(float)
    mat_distancias = np.array(aux)
    #print(mat_distancias)
    return mat_distancias

#------------------------------------------------------------------------------------------------

dataset  = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

mat_dataset = np.array(dataset)

#cuantos datos usaremos para el entrenamiento, input usuario -> 105
training_size = 105 #int(input("Ingrese valor: "))

mat_entrenamiento = np.empty((0, 5))

for i in range (0, training_size):
    aleatorio = random.randint(0, len(mat_dataset) - 1)
    mat_entrenamiento = np.vstack([mat_entrenamiento, mat_dataset[aleatorio]])
    mat_dataset = np.delete(mat_dataset, aleatorio, axis=0)

mat_prueba = mat_dataset

k = 10

respuestas_modelo = []
#print("La matriz de entrenamiento (tamaño ", len(mat_entrenamiento), ") es: \n", mat_entrenamiento)
#rint("\nla matriz de prueba (tamaño ", len(mat_prueba), ") es: \n", mat_prueba)

for i in range(0, len(mat_prueba)):
    print("---------------------------------------------------------")
    print("ITEREACIÓN ", i+1)
    matriz_distancias = calcular_distancias(mat_entrenamiento, mat_prueba[i])
    solucion_modelo = k_menores_y_respuesta(matriz_distancias, k)
    respuestas_modelo.append(solucion_modelo)

precision = calcular_precision(respuestas_modelo, mat_prueba)
print("La precisión del modelo es ", precision, "%")

print("_____________________________________________")
print("\n*** INGRESE DATOS DE FLOR ***")
print("_____________________________________________")
parametro1 = float(input("Ingrese paarametro1: "))
parametro2 = float(input("Ingrese paarametro2: "))
parametro3 = float(input("Ingrese paarametro3: "))
parametro4 = float(input("Ingrese paarametro4: "))

list_parametros = [parametro1, parametro2, parametro3, parametro4]
matriz_distancias = calcular_distancias(mat_entrenamiento, list_parametros)
solucion_modelo = k_menores_y_respuesta(matriz_distancias, k)
print("\n---->la flor ingresada es una: ", solucion_modelo, "\n")

