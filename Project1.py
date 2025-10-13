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


def get_state_data(rows):
    state_data = {}
    for row in rows:
        state = row["State"]
        sales = round(float(row["Sales"]), 1)
        profit = round(float(row["Profit"]), 1)
        if state not in state_data:
            state_data[state] = {"total_sales" : 0, "total_profit": 0}
        state_data[state]["total_sales"] += sales
        state_data[state]["total_profit"] += profit
    return state_data

state_data = get_state_data(rows)
print(state_data)

