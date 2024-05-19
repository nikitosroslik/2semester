import pandas as pd
file_path = 'file.csv'
data = pd.read_csv(file_path)
statistics = data.describe(include='all')
print("Статистика по каждому столбцу:")
print(statistics)
