income = float(input("Enter net income: "))

total_tax = 0

print("\nTax Details by Bracket")

# Bracket 1: 0 - 150,000
if income > 0:
    taxable = min(income, 150000)
    tax = taxable * 0
    total_tax = total_tax + tax
    print("0 -", taxable, ":", tax)

# Bracket 2: 150,001 - 300,000
if income > 150000:
    taxable = min(income, 300000) - 150000
    tax = taxable * 0.05
    total_tax = total_tax + tax
    print("150,001 -", min(income, 300000), ":", tax)

# Bracket 3: 300,001 - 500,000
if income > 300000:
    taxable = min(income, 500000) - 300000
    tax = taxable * 0.10
    total_tax = total_tax + tax
    print("300,001 -", min(income, 500000), ":", tax)

# Bracket 4: 500,001 - 750,000
if income > 500000:
    taxable = min(income, 750000) - 500000
    tax = taxable * 0.15
    total_tax = total_tax + tax
    print("500,001 -", min(income, 750000), ":", tax)

# Bracket 5: 750,001 - 1,000,000
if income > 750000:
    taxable = min(income, 1000000) - 750000
    tax = taxable * 0.20
    total_tax = total_tax + tax
    print("750,001 -", min(income, 1000000), ":", tax)

# Bracket 6: 1,000,001 - 2,000,000
if income > 1000000:
    taxable = min(income, 2000000) - 1000000
    tax = taxable * 0.25
    total_tax = total_tax + tax
    print("1,000,001 -", min(income, 2000000), ":", tax)

# Bracket 7: 2,000,001 - 5,000,000
if income > 2000000:
    taxable = min(income, 5000000) - 2000000
    tax = taxable * 0.30
    total_tax = total_tax + tax
    print("2,000,001 -", min(income, 5000000), ":", tax)

# Bracket 8: More than 5,000,000
if income > 5000000:
    taxable = income - 5000000
    tax = taxable * 0.35
    total_tax = total_tax + tax
    print("More than 5,000,000 :", tax)

net_income = income - total_tax

effective_rate = (total_tax / income) * 100

print("\nTotal Tax =", total_tax)
print("Net Income =", net_income)
print("Effective Tax Rate =", effective_rate, "%")