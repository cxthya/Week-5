'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 1: String Slicing
'''

#Applying string slicing to the string "I love Mexico"

text = "I love Mexico"

#Slicing the first character
print(text[0]) 

#Slicing the word "love"
print(text[2:6]) 

#Uppercase the whole phrase
print(text.upper())

#Making a function to make the text uppercase
def shout(text):
    return text.upper()
result = shout(text)
print(result)