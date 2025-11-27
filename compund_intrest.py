

principle = float(input("Enter principle amount: "))

rate = float(input("Enter rate of interest: "))

time = float(input("Enter time in years: "))

amount1 = principle * (1 + rate/100) ** time
amount2 = principle * pow((1 + rate/100), time)

print("amount1 is:", amount1)
print("amount2 is:", amount2)