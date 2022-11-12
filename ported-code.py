#!/usr/bin/bash python3
 
# See https://aka.ms/new-console-template for more information
print("Well Hello There!");

# states date and time
from datetime import datetime
now =datetime.now()
print('now =', now)

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

print('date and time =', dt_string)

# Type your username and press enter
print("Enter your name:");


# Create a string variable and get user input from the keyboard and store it in the variable
userName = input()

# Print the value of the variable (userName), which will display the input value
print("Username is: " + userName);

print("Enter your age:");
age = input()
print("Your age is: " + age);