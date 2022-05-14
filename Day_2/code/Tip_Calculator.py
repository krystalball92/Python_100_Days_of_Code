#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 15, or 20? "))
split = int(input("How many people will split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = tip_as_percent * bill
total_bill = bill + total_tip_amount
split_bill = total_bill / split
final_amount = round(split_bill, 2)
final_amount = "{:.2f}".format(split_bill)
print(f"Each person should pay ${final_amount}")
