# Project1.py
# Author: Kurt Bates
# Date: 10-21-2025
# Description: Analyze sales data from SampleSuperstore.csv
# Used Gen AI to help write test cases and functions

import csv
import os
import unittest

#print(os.getcwd())
def main():
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



class TestProject1(unittest.TestCase):

    #  TEST load_csv 
    def test_load_csv_returns_list(self):
        data = load_csv('SampleSuperstore.csv')
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)

    def test_load_csv_limited_rows(self):
        """General: Should only load 50 rows as defined."""
        data = load_csv('SampleSuperstore.csv')
        self.assertLessEqual(len(data), 50)

    def test_load_csv_bad_filename(self):
        """Edge: Missing file should raise FileNotFoundError."""
        with self.assertRaises(FileNotFoundError):
            load_csv('nonexistent.csv')

    def test_load_csv_empty_file(self):
        """Edge: Empty file should return empty list."""
        with open('empty.csv', 'w') as f:
            pass
        data = load_csv('empty.csv')
        self.assertEqual(data, [])
        os.remove('empty.csv')

    # TEST get state data 
    def test_state_data_general(self):
        """General: Should aggregate sales and profit per state."""
        rows = [
            {'State': 'CA', 'Sales': '100', 'Profit': '20'},
            {'State': 'CA', 'Sales': '50', 'Profit': '10'},
            {'State': 'TX', 'Sales': '80', 'Profit': '5'}
        ]
        result = get_state_data(rows)
        self.assertEqual(result['CA']['total_sales'], 150.0)
        self.assertEqual(result['TX']['total_profit'], 5.0)

    def test_state_data_empty(self):
        """Edge: Empty dataset should return empty dict."""
        self.assertEqual(get_state_data([]), {})

    def test_state_data_missing_values(self):
        """Edge: Missing profit or sales handled gracefully."""
        rows = [{'State': 'CA', 'Sales': '', 'Profit': '10'}]
        with self.assertRaises(ValueError):
            get_state_data(rows)

    def test_state_data_rounding(self):
        """General: Totals should round to 2 decimals."""
        rows = [{'State': 'CA', 'Sales': '100.556', 'Profit': '50.447'}]
        result = get_state_data(rows)
        self.assertAlmostEqual(result['CA']['avg_sales'], 100.56)
        self.assertAlmostEqual(result['CA']['avg_profit'], 50.45)

    #  TEST avg profit catagory 
    def test_avg_profit_category_general(self):
        """General: Should compute total sales and profit by category."""
        rows = [{'Category': 'Furniture', 'Sales': '200', 'Profit': '20'}]
        result = avg_profit_catagory(rows)
        self.assertIn('Furniture', result)
        self.assertEqual(result['Furniture']['total_sales'], 200.0)

    def test_avg_profit_category_empty(self):
        """Edge: Empty rows should return empty dict."""
        self.assertEqual(avg_profit_catagory([]), {})

    def test_avg_profit_category_multiple(self):
        """General: Multiple categories summed separately."""
        rows = [
            {'Category': 'Tech', 'Sales': '100', 'Profit': '40'},
            {'Category': 'Office', 'Sales': '200', 'Profit': '10'}
        ]
        result = avg_profit_catagory(rows)
        self.assertIn('Tech', result)
        self.assertIn('Office', result)

    def test_avg_profit_category_missing(self):
        """Edge: Missing numeric data handled gracefully."""
        rows = [{'Category': 'Furniture', 'Sales': '', 'Profit': '5'}]
        with self.assertRaises(ValueError):
            avg_profit_catagory(rows)

    #  TEST avg discount by category 
    def test_discount_category_general(self):
        """General: Compute avg discount per category."""
        rows = [
            {'Category': 'Furniture', 'Discount': '0.2', 'Quantity': '2'},
            {'Category': 'Furniture', 'Discount': '0.1', 'Quantity': '3'}
        ]
        result = avg_discount_by_category(rows)
        self.assertAlmostEqual(result['Furniture']['avg_discount'], 0.15)

    def test_discount_category_multiple(self):
        """General: Two categories have separate averages."""
        rows = [
            {'Category': 'Tech', 'Discount': '0.5', 'Quantity': '2'},
            {'Category': 'Office', 'Discount': '0.1', 'Quantity': '1'}
        ]
        result = avg_discount_by_category(rows)
        self.assertIn('Tech', result)
        self.assertIn('Office', result)

    def test_discount_category_empty(self):
        """Edge: Empty list should return {}."""
        self.assertEqual(avg_discount_by_category([]), {})

    def test_discount_category_zero_count(self):
        """Edge: No valid entries should give avg_discount 0."""
        rows = [{'Category': 'Tech', 'Discount': '0', 'Quantity': '0'}]
        result = avg_discount_by_category(rows)
        self.assertEqual(result['Tech']['avg_discount'], 0)

    # ---------- TEST profit_margin_by_category ----------
    def test_profit_margin_general(self):
        """General: Compute profit margin per category."""
        rows = [{'Category': 'Tech', 'profit': '100', 'sales': '500'}]
        result = profit_margin_by_category(rows)
        tech = result['category']
        self.assertAlmostEqual(tech['profit_margin'], 0.2)

    def test_profit_margin_zero_sales(self):
        """Edge: Zero sales should yield 0 margin."""
        rows = [{'Category': 'Office', 'profit': '100', 'sales': '0'}]
        result = profit_margin_by_category(rows)
        self.assertEqual(result['category']['profit_margin'], 0)

    def test_profit_margin_empty(self):
        """Edge: Empty list returns empty dict."""
        self.assertEqual(profit_margin_by_category([]), {})

    def test_profit_margin_multiple(self):
        """General: Multiple entries per category accumulate."""
        rows = [
            {'Category': 'Tech', 'profit': '50', 'sales': '100'},
            {'Category': 'Tech', 'profit': '25', 'sales': '100'}
        ]
        result = profit_margin_by_category(rows)