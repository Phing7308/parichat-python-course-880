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
phone = input("Enter your phone number:")


# name validate
name_validator = True
for char in name:
    #print(char,char.isalpha())
    if char.isalphe() == True or char == "":
        name_validator = true
    else:
        name_vzlidator = False
        break

# age validate
age_validator = True
if 18 <= age and age <= 65:
    age_validator = true
else:
    age_validator = False

# phone number validate
# 10 character
phone_validator = True
if len(phone) !=10:
    phone_validator = False

for char in phone:
    if char.isdigit() == False:
       phone_validator = False
       break

print()
print("Validation Results: ")
if name_validator == True
    print("Name: Valid(contains only letters and spaces)")
else:
    print("Name: Invalid (not contains only letter and spaces)")

if age_validator == True:
    print(f"Age : Valid({age}years old)")
else:
    print("Age: Invalid(less than 18 or more than 65)")

if phone_validator == True:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")

print()
print("Formatted Information:")
print("Name:",name.upper())

