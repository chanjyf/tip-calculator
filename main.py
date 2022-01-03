bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

bill_tip = bill * (1+tip_percentage/100)
bill_shared = bill_tip / people

final_amount = round(bill_shared, 2)
final_amount = "{:.2f}".format(bill_shared)
message = f"Each person should pay: US${final_amount}"
print(message)
