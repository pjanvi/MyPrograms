#Assuming there are no accidents or delays, the distance that a car travels down the inter-
#state can be calculated with the following formula:
#Distance = Speed * Time
#A car is traveling at 70 miles per hour. Write a program that displays the following:
#• The distance the car will travel in 6 hours
#• The distance the car will travel in 10 hours
#• The distance the car will travel in 15 hours

def distance():
    speed = 70
    time1 = 6
    time2 = 10
    time3 = 15
    distance1 = speed * time1
    # time=6, speed=70, distance=
    print(f"If time = {time1} speed = {speed} then distance travelled is {distance1} kmph.")
    distance2 = speed * time2
    print(f"If time = {time2} speed = {speed} then distance travelled is {distance2} kmph.")
    distance3 = speed * time3
    print(f"If time = {time3} speed = {speed} then distance travelled is {distance3} kmph.")

distance()
