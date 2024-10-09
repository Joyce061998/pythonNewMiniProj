#other solution
welcome1= """
Welcome to Car Option 
"""
print(welcome1)
help=input("Type Help>")

title = str("Help")
if help == title:
    help1 = """
    start -  to start the car - please select 1
    stop- to stop the car - please select 2
    quit- to exit - please select 3
    """
    print(help1)
else:
    help = input(">")

car_count = 0
car_limit = 3
while car_count < car_limit:
    try:
        car = int(input("Please select the Option: "))
        car_count += 1
        if car == 1:
            print("Start Engine!")
            continue
        elif car == 2:
            print("Stop Engine")
            continue
        elif car == 3:
            print("Bye")
        else:
            print("I Dont Understand")
    except:
        print("Invalid")

