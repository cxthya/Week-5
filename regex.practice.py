'''
Cinthya Calderon-Hernandez
CMSC 111
Spring 2026
Assignment 4: Regular expressions
'''

def extract_phone_numbers(text):
    # Regular expression pattern for phone numbers
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    # Find all matches in the text
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

# Example usage
text = "Call me at 123-456-7890 or 987-654-3210. Office: 555-111-2222. Invalid: 1234567890" \

numbers = extract_phone_numbers(text)
print("Extracted phone numbers:", numbers)

#Task 2: Extracting email addresses
def is_valid_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
   #Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    return False

#Prompt the user for an email address
email = input ("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address.")
else:    print("Invalid email address.")