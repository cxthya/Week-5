'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 2: Using the len() function 
'''

#Ask user for password
password = input("Enter your password: ")

#Check the length of the password
if len(password) >= 8:
    print("Password is strong.")
else:    print("Password is too short. Please enter a password with at least 8 characters.")

    
