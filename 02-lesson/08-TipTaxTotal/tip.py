#Write a program that calculates the total amount of a meal purchased at a restaurant. The
#program should ask the user to enter the charge for the food, and then calculate the amount
#of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

def tip_tax_total():
    print("Enter the charge for the food: ")
    amount = float(input(">>> "))
    tip = amount * 18
    print(f"Tip = ${tip} ")
    tax = amount * 7
    print(f"Tax = ${tax} ")
    total = amount + tip + tax
    print(f"Total = ${total} ")

tip_tax_total()

