"""
                            Jay Bhavani

{"vadapav", 
    {
        'qty' : 2,
        'price' : 20
    }
}
            MENU 

vadapav    50 Rs.
dabeli     30 Rs.
sandwich   180 Rs.

Enter product which you want to buy : vadapav 
Enter no. of qty you want : 3

    price will be ::: 3 X 50Rs. =  150 Rs

do you want to add more product ?  press y for yes : y 

Enter product which you want to buy : dabeli
Enter no. of qty you want : 2

    price will be ::: 2 X 30Rs. =  60 Rs

do you want to add more product ?  press y for yes : n

INVOICE :
------------------
vadapav   Qty. 3 X Rs. 50  = Rs. 150
dabeli    Qty. 2 X Rs. 30  = Rs.  60
----------------------------------
Total : Rs. 210
"""

products = {} #main dictionary
customer_billing = {}
status = True
status1 = True
total_price = 0
menu = """
        press 1 for product manager
        press 2 for customer
        press 3 to exit
"""

while status:
    sub_dict = {}
    print(menu)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        product_name = input("Enter your product name: ")
        qty = int(input("Enter your qty: "))
        price = int(input("Enter price: "))

        if product_name in products.keys():
            sub_dict["qty"] = qty + products[product_name]["qty"]
            sub_dict["price"] = price
        else:
            sub_dict["qty"] = qty
            sub_dict["price"] = price

        products[product_name] = sub_dict

        for k in products.keys():
            print(f"{k} Qty.  {products[k]['qty']}  Price.  {products[k]['price']}")

    elif choice == 2:
        while status1:
            product_name1 = input("Enter your product name: ")
            qty1 = int(input("Enter your qty: "))

            if qty1 > products[product_name1]['qty']:
                print(f"Product available {products[product_name1]['qty']}")
                break
        
            price1 = qty1 * products[product_name1]['price']
            products[product_name1]["qty"] -= qty1

            sub_dict = {}
            sub_dict["qty"] = qty1
            sub_dict["price"] = price1

            if product_name1 in customer_billing.keys():
                customer_billing[product_name1]['qty'] += qty1 
                customer_billing[product_name1]['price'] += price1 
            else:
                customer_billing[product_name1] = sub_dict

            print(f"Price will be ::: {qty1} X Rs. {products[product_name1]['price']} =  Rs. {price1}")
            mark = input("Do you want to add more products? Press y for yes & n for no: ")
            total_price += price1
            if mark == 'y':
                status1 = True
            elif mark == 'n':
                status1 = False
            else:
                print("Invalid option!")


        print("INVOICE" \
            "--------------------------------")
        for k in customer_billing.keys():
            print(f"{k.ljust(10)} Qty. {str(customer_billing[k]['qty']).ljust(2)} X Rs. {str(products[k]['price']).ljust(4)} = Rs. {customer_billing[k]['price']}")

        
        print("----------------------------------------")
        
        print(f"Total : Rs. {total_price}")
        status = False