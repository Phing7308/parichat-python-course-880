"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = input("Enter your phone number: ")

# name validate
name_validator = True
for char in name:
    if char.isalpha() == True or char == " ":
        name_validator = True
    else:
        name_validator = False
        break

# age validate
age_validator = True
if 18 <= age <= 65:
    age_validator = True
else:
    age_validator = False

# phone number validate
phone_validator = True
if len(phone) != 10:
    phone_validator = False

for char in phone:
    if char.isdigit() == False:
        phone_validator = False
        break

print()
print("Validation Results:")

if name_validator == True:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (not contains only letters and spaces)")

if age_validator == True:
    print("Age: Valid (%d years old)" % age)
else:
    print("Age: Invalid (less than 18 or more than 65)")

if phone_validator == True:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")

print()
print("Formatted Information:")
print("Name: %s" % name.upper())

if 18 <= age <= 30:
    print("Age Group: Young Adult (18-30)")
elif 31 <= age <= 45:
    print("Age Group: Adult (31-45)")
elif 46 <= age <= 65:
    print("Age Group: Middle-aged Adult (46-65)")
else:
    print("Age Group: Invalid Age")

if phone_validator == True:
    print("Phone: +91-%s" % phone)
else:
    print("Phone: Invalid Number")
