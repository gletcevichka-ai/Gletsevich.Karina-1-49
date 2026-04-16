#Глецевич Карина 1-49
#лабораторная работа 3, задание 2, вариант 4

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.datasets import grunfeld

data = grunfeld.load_pandas().data
print(data.head())
print('Список всех фирм:')
firms = data['firm'].unique()
firm1,firm2,firm3 = firms[0], firms[1], firms[2]
print(firm1,firm2,firm3)

f1 = data[data['firm'] == firm1]
f2 = data[data['firm'] == firm2]
f3 = data[data['firm'] == firm3]

plt.plot (f1['year'], f1['invest'], label = 'фирма №1', color = 'hotpink')
plt.plot (f2['year'], f2['invest'], label = 'фирма №2', color = 'rebeccapurple')
plt.plot (f3['year'], f3['invest'], label = 'фирма №3', color = 'crimson')
plt.title('Инвестиции фирм за время')
plt.xlabel('Год')
plt.ylabel('Инвестиции')
plt.grid(True) #сетка
plt.legend()
plt.show()

plt.bar(f1['year'], f1['invest'], label = 'фирма №1', color = 'hotpink')
plt.bar (f2['year'], f2['invest'], label = 'фирма №2', color = 'rebeccapurple')
plt.bar (f3['year'], f3['invest'], label = 'фирма №3', color = 'crimson')
plt.title('Инвестиции фирм за время')
plt.xlabel('Год')
plt.ylabel('Инвестиции')
plt.grid(True) #сетка
plt.legend()
plt.show()

plt.scatter (f1['year'], f1['invest'], label = 'фирма №1', c= 'hotpink', s=5, marker = 'o')
plt.scatter (f2['year'], f2['invest'], label = 'фирма №2', c= 'rebeccapurple', s=5, marker = 'o')
plt.scatter (f3['year'], f3['invest'], label = 'фирма №3', c= 'crimson', s=5, marker = 'o')
plt.title('Инвестиции фирм за время')
plt.xlabel('Год')
plt.ylabel('Инвестиции')
plt.grid(True) #сетка
plt.legend()
plt.show()