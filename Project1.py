import csv
import os

print(os.getcwd())

def load_csv(filename):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)

    with open(full_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader][:50]
    return data

rows = load_csv('SampleSuperstore.csv')
#print(rows)





