#One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
#enter the total square feet in a tract of land and calculates the number of acres in the tract.
#Hint: Divide the amount entered by 43,560 to get the number of acres.

def no_of_acres():
    print("Enter the total square feet: ")
    total_square_feet = float(input(">>> "))
    one_acre_of_land = 43560
    total_acres = total_square_feet / one_acre_of_land
    #print(str(total_square_feet) + " feet =" + str(total_acres) + " acres")
    # f strings
    print(f"{total_square_feet} feet = {total_acres} acres")

no_of_acres()
