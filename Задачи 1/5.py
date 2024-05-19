import csv
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
filename = 'data.csv'
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
data = list(zip(*csv_reader))
for col_index, col_data in enumerate(data):
        numbers = [float(num) for num in col_data]
        avg = calculate_average(numbers)
        print(f'Среднее арифметическое для колонки {col_index + 1}: {avg}')
