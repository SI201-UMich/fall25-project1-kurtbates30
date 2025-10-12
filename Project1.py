import csv 

def load_csv(filename):

    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader][:50]
    return data

rows = load_csv('SampleSuperstore.csv')
print(rows)



