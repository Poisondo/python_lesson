import requests
import numpy as np
import pandas as pd

# Используем библиотеку requests для загрузки данных с сайта
response = requests.get('https://api.exchangerate-api.com/v4/latest/RUB')
data = response.json()
rates = data['rates']

# Преобразуем словарь в DataFrame с помощью Pandas
df = pd.DataFrame.from_dict(rates, orient='index', columns=['Rate'])

# Добавляем столбец с отклонением от среднего значения курса с помощью NumPy
mean_rate = np.mean(df['Rate'])
df['Deviation'] = df['Rate'].apply(lambda x: x - mean_rate)

# Сохраняем результаты в файл CSV
df.to_csv('out.csv', index_label='Currency')