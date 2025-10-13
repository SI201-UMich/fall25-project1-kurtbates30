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

def get_avg(state_data):

    def state_avg_profit(state_data):
        for state, data in state_data.items():
            total_sales = data["total_sales"]
            total_profit = data["total_profit"]
            if total_sales != 0:
                avg_profit = round(total_profit / total_sales, 2)
            else:
                avg_profit = 0
            data["avg_profit"] = avg_profit
        return state_data

    def state_avg_sales(state_data):
        for state, data in state_data.items():
            total_sales = data["total_sales"]
            total_profit = data["total_profit"]
            if total_profit != 0:
                avg_sales = round(total_sales / total_profit, 2)
            else:
                avg_sales = 0
            data["avg_sales"] = avg_sales
        return state_data
    state_data = state_avg_profit(state_data)
    state_data = state_avg_sales(state_data)
    return state_data


def avg_profit_catagory(rows):
    category_data = {}

    for row in rows:
        category = row["Category"]
        sales = round(float(row["Sales"]), 1)
        profit = round(float(row["Profit"]), 1)

        if category not in category_data:
            category_data[category] = {"total_sales" : 0, "total_profit": 0}
        category_data[category]["total_sales"] += sales
        category_data[category]["total_profit"] += profit

    for category, data in category_data.items():
        data["profit_margin"] = round(data["total_profit"] / data["total_sales"], 2)
    return category_data



def avg_discount_by_category(rows):
   cataegory_discounts = {}

   for row in rows:
       category = row["Category"]
       discount = round(float(row["Discount"]), 2)
       quntity = int(row["Quantity"])

       if category not in cataegory_discounts:
           cataegory_discounts[category] = {"total_discount": 0, "count": 0}
       cataegory_discounts[category]["total_discount"] += discount
       cataegory_discounts[category]["count"] += 1

   for category, data in cataegory_discounts.items():
        
        if data["count"] != 0:
            data["avg_discount"] = round(data["total_discount"] / data["count"], 2)
        else:
            data["avg_discount"] = 0
   return cataegory_discounts


def profit_margin_by_category(rows):
    margins = {}

    for row in rows:
        category = row["Category"]
        profit = float(row["profit"])
        sales = float(row["sales"])

        if category not in margins:
            margins["category"] = {"total_profit": 0, "total_sales": 0}
        margins["category"]["total_profit"] += profit
        margins["category"]["total_sales"] += sales
    for category, data in margins.items():
        if data["total_sales"] != 0:
            data["profit_margin"] = round(data["total_profit"] / data["total_sales"], 2)
        else:
            data["profit_margin"] = 0
    return margins



#funtion calls

rows = load_csv('SampleSuperstore.csv')

state_data = get_state_data(rows)
state_data = get_avg(state_data)
category_data = avg_profit_catagory(rows)
cataegory_discounts = avg_discount_by_category(rows)
print(cataegory_discounts)
#state_data = state_avg_profit(state_data)
#state_data = state_avg_sales(state_data)

#for state, data in state_data.items():
#    print(f"{state}: {data}")