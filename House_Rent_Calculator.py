## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit

## Output
# Total amount you've to pay is

rent = int(input("Enter the hostel/flat rent: "))
food = int(input("Enter the amount of food ordered: "))
electricity_spend = int(input("Enter the total of electricity spend: "))
charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Enter the number of persons living in room/flat: "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print(f"Each person will pay {output}.")