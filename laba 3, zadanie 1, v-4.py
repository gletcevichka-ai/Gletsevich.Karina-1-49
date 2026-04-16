#Глецевич Карина 1-49
#лабораторная работа 3, задание 1, вариант 4

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
print(df.head())
#print(df)

c1 = df['mean radius'] #радиус опухоли
c2 = df['mean texture'] #шероховатость опухоли
clas = df['target']
df_clas0 = df[df['target'] == 0]
df_clas1 = df[df['target'] == 1]

plt.figure(figsize=(10, 6))
plt.scatter (df_clas0['mean radius'], df_clas0['mean texture'], color = 'navy', label = 'Класс 0 (злокачественные)', alpha=0.7)  #alpha - прозрачность точки на графике
plt.scatter (df_clas1['mean radius'], df_clas1['mean texture'], color = 'fuchsia', label = 'Класс 1 (доброкачественные)', alpha=0.7)
plt.title('Breast cancer')
plt.xlabel('mean radius')
plt.ylabel('mean texture')
plt.legend()
plt.grid(True)
plt.show()