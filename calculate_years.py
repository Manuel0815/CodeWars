def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        y+=1
        principal = principal + principal * interest * (1-tax)
    return y

print calculate_years(1000, 0.05, 0.18, 1100)