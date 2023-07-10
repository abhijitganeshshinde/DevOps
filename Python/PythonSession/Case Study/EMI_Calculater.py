def calculate_emi(principal, rate, months):
    r = rate / 12 / 100  
    emi = principal * r * (1 + r)**months / ((1 + r)**months - 1)
    return emi


principal = float(input("Enter Principal Amount :- "))
rate =  float(input("Enter Rate Of Interest :- "))
months = int(input("Enter Months :- "))

emi = calculate_emi(principal, rate, months)
print(f"Monthly EMI Amount :- {round(emi,2)}")
