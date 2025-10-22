# Project1.py
# Author: Kurt Bates
# Date: 10-21-2025
# Description: Analyze sales data from SampleSuperstore.csv
# Used Gen AI to help write test cases and functions

import csv
import os
import unittest

#print(os.getcwd())

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
        sales = float(row["Sales"])
        profit = float(row["Profit"])
        if state not in state_data:
            state_data[state] = {"total_sales" : 0, "total_profit": 0}
        state_data[state]["total_sales"] += sales
        state_data[state]["total_profit"] += profit

    for state, data in state_data.items():
        data["avg_sales"] = round(data["total_sales"], 2)
        data["avg_profit"] = round(data["total_profit"], 2)
    print(1)
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

    print(2)
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
   print(3)


#txt file write

def write_results():
    state_data = get_state_data(rows)
    with open('state_data.txt', 'w') as file:
        for state, data in state_data.items():
            file.write(f"{state}: {data}\n")

        return state_data


