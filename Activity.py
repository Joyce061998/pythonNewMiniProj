"""
1. Write a Python program to print the following string in a specific format (see the output).
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

"""

star= """
Twinkle, twinkle, little star, 
How I wonder what you are! Up above the world so high, 
Like a diamond in the sky. 
Twinkle, twinkle, little star, How I wonder what you are
"""

print(star)

"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14

"""

import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

radius = float(input("Type the radius:"))
area = 3.14 * (radius**2)
print(area)


"""
Write a Python program that accepts the user's first and 
last name and prints them in reverse order with a space between them.
"""