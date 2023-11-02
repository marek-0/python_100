print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill? $"))
bill_tip = float(input("What percentage tip would you like to give? %"))
bill_tipcalc = bill_tip / 100
bill_personcount = float(input("How many people to split the bill?"))
bill_perperson = (bill_total + bill_total * bill_tipcalc) / bill_personcount
print(f"Each person should pay: ${bill_perperson:.2f}")