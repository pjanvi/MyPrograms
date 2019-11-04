#A car’s miles-per-gallon (MPG) can be calculated with the following formula:
#MPG = Miles driven Gallons of gas used
#Write a program that asks the user for the number of miles driven and the gallons of gas
#used. It should calculate the car’s MPG and display the result.

def miles_per_gallon():
    print("Enter the number of miles driven: ")
    miles = float(input(">>> "))
    print("Enter the gas used: ")
    gas = float(input(">>> "))
    result = miles / gas
    print(f"Result is {result} mpg")

miles_per_gallon()
