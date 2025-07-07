"""
1) sales_data = [
    {"product": "Apple", "quantity": 10, "price": 0.5},
    {"product": "Banana", "quantity": 5, "price": 0.3},
    {"product": "Orange", "quantity": 8, "price": 0.6},
    {"product": "Apple", "quantity": 7, "price": 0.5},
    {"product": "Banana", "quantity": 3, "price": 0.3},
    {"product": "Orange", "quantity": 6, "price": 0.6},
]

Tasks to Complete:
-----------------------------
Total Sales per Product
Total Quantity Sold per Product:
Identify the most Popular Product.
Find the product that generated the most revenue.
====================================================================
"""

sales_data = [
    {"product": "Apple", "quantity": 10, "price": 0.5},
    {"product": "Banana", "quantity": 5, "price": 0.3},
    {"product": "Orange", "quantity": 8, "price": 0.6},
    {"product": "Apple", "quantity": 7, "price": 0.5},
    {"product": "Banana", "quantity": 3, "price": 0.3},
    {"product": "Orange", "quantity": 6, "price": 0.6},
]

total = {}

for i in sales_data:
    name = i['product']
    quant = i['quantity']
    price = i['price']

    if name not in total:
        total[name] = {'quant' : 0, 'price' : 0}

    total[name]['quant'] += quant
    total[name]['price'] += price

for k,v in total.items():
    print(f"Total Sales per {k}: {v['price']}")
    print(f"Total Quantity Sold per {k}: {v['quant']}")
    print()

popular = max(total, key = lambda x : total[x]['quant'])
profit = max(total, key = lambda x: total[x]['price'])

print(f"The most Popular Product is {popular}.")
print(f"The product that generated the most revenue is {profit}.")
