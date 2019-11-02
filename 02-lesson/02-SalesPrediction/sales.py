#A company has determied that its annual profit is typically 23 percent of total sales. 
#Write a program that asks the user to enter the projected amount of total sales, and then displays
#the profit that will be made from that amount.
#Hint: Use the value 0.23 to represent 23 percent.

def total_sales():
    print("Enter the projected amount: ")
    projected_amount = int(input(">>> "))
    profit = projected_amount * 0.23
    print(profit)

total_sales()

