#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

bill_tip = bill * (1+tip_percentage/100)
bill_shared = bill_tip / people

final_amount = round(bill_shared, 2)
final_amount = "{:.2f}".format(bill_shared)
message = f"Each person should pay: US${final_amount}"
print(message)