#A customer in a store is purchasing five items. Write a program that asks for the price of
#each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
#Assume the sales tax is 7 percent.

def total_purchase():
    item1 = float(input("Item 1: "))
    item2 = float(input("Item 2: "))
    item3 = float(input("Item 3: "))
    item4 = float(input("Item 4: "))
    item5 = float(input("Item 5: "))
    subtotal = item1 + item2 + item3 + item4 + item5
    print(f"subtotal\t:\t\t {subtotal}")
    sales_tax = subtotal * 0.07
    print(f"sales_tax\t:\t\t {sales_tax}")
    total = subtotal + sales_tax
    print(f"total\t\t:\t\t {total}")

total_purchase()
    
