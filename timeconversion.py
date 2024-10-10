#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Extract the period (AM/PM) from the string
    period = s[-2:]  # Last two characters are AM or PM
    hour = int(s[:2])  # First two characters represent the hour
    minutes_seconds = s[2:-2]  # The middle part is minutes and seconds

    if period == 'AM':
        if hour == 12:
            hour = 0  # Convert 12 AM to 00
    else:  # PM case
        if hour != 12:
            hour += 12  # Convert PM hour to 24-hour format

    # Format the hour to ensure it is two digits
    return f"{hour:02}{minutes_seconds}"


s = input("Enter time in 12-hour format (e.g., 07:05:45PM): ")
result = timeConversion(s)
print(result)