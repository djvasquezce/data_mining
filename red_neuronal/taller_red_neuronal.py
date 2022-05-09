import numpy as np
import pandas as pd
dataset  = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

mat_dataset = np.array(dataset)

print(mat_dataset)