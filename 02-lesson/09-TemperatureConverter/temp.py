#Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula
#is as follows:
#9/5 * c + 32 = f
#The program should ask the user to enter a temperature in Celsius, and then display the
#temperature converted to Fahrenheit.

def temp_converter():
    print("Enter the temperature in celsius: ")
    celsius = float(input(">>> "))
    Fahrenheit = (9 / 5 * (celsius)) + 32
    print(f"the temperature converted is {Fahrenheit} F ")

temp_converter()
