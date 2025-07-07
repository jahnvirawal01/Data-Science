"""
products = 
    [
        {"product" : "Mobile" , "Unit_sold" : 20 , "Unit_price" : 75000},
        {"product" : "Laptop" , "Unit_sold" : 28 , "Unit_price" : 105050},
        {"product" : "Laptop" , "Unit_sold" : 45 , "Unit_price" : 150000},
        {"product" : "Mobile" , "Unit_sold" : 10 , "Unit_price" : 50000},
        {"product" : "Tab" , "Unit_sold" : 10 , "Unit_price" : 50000},
        {"product" : "Tab" , "Unit_sold" : 5 , "Unit_price" : 30000},
    ]

    Product wise revenue generate ??? 

    Mobile : total unit sold ??? and Total revenue  ??
    

"""

products =[
        {"product" : "Mobile" , "Unit_sold" : 20 , "Unit_price" : 75000},
        {"product" : "Laptop" , "Unit_sold" : 28 , "Unit_price" : 105050},
        {"product" : "Laptop" , "Unit_sold" : 45 , "Unit_price" : 150000},
        {"product" : "Mobile" , "Unit_sold" : 10 , "Unit_price" : 50000},
        {"product" : "Tab" , "Unit_sold" : 10 , "Unit_price" : 50000},
        {"product" : "Tab" , "Unit_sold" : 5 , "Unit_price" : 30000},
    ]

total = {}

for i in products:
    name = i['product']
    units = i['Unit_sold']
    price = i['Unit_price']

    if name not in total:
        total[name] = {'Unit_sold': 0, 'Unit_price': 0}

    total[name]['Unit_sold'] += units
    total[name]['Unit_price'] += price 

for k,v in total.items():
    print(f"Total {k} sold are {v['Unit_sold']}")
    print(f"Total {k} revenue generated is {v['Unit_price']}")
    print()
