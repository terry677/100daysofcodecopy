print("Welcome to the Tip calculator!!!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10 , 12, or 25: "))
people_for_bill = int(input("How many people to split bill?: "))
tip_percentage_of_bill = bill * (tip_percentage / 100)

total_bill = bill + tip_percentage_of_bill

share_of_bill = round((total_bill / people_for_bill), 2)

print(f"Each person will pay ${share_of_bill}")
