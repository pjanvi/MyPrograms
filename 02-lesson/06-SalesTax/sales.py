#Write a program that will ask the user to enter the amount of a purchase. The program
#should then compute the state and county sales tax. Assume the state sales tax is 5 percent
#and the county sales tax is 2.5 percent. The program should display the amount of the pur-
#chase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale
#(which is the sum of the amount of purchase plus the total sales tax).
#Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

def total_purchase():
    print("Enter the amount of purchase: ")
    amount = float(input(">>> "))
    sales_tax = amount * 0.05
    print(f"Sales Tax is ${sales_tax}")
    county_sales_tax = amount * 0.025
    print(f"County Sales Tax is ${county_sales_tax}")
    total_purchase = amount + sales_tax + county_sales_tax
    print(f"Total purchas is ${total_purchase}")

total_purchase()


