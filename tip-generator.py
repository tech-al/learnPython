#If the bill was $150.00, split between 5 people, with 12% tip.
from typing import final

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

# Get user input for the bill, tip percentage, and number of people
bill = float(input("What was the total bill? $\n"))
percentage = float(input("How much tip would you like to give? 10, 12, or 15?\n"))
number_of_people = int(input("How many people will be splitting this bill?\n"))

# Calculate the total tip
tip_amount = (percentage / 100) * bill

# Calculate the total bill including tip
total_bill_with_tip = tip_amount + bill

# Calculate each person's share
bill_per_person = total_bill_with_tip / number_of_people

# Round the result to 2 decimal places and format as a currency value
final_amount = f"{bill_per_person:.2f}"

print(f"Each person should pay: ${final_amount}")

