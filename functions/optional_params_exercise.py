def send_email(address, body, subject='No Subject'):
    print(f'Address: {address}\n')
    print(f'Body: {body}\n')
    print(f'Subject: {subject}\n\n')

def calculate_total_cost(meal_cost, tip_rate=0.15):
    tip = meal_cost * tip_rate
    total_cost = meal_cost + tip
    print("Total cost of meal is: ",total_cost)

send_email('New Delhi', 'I want leave for tommorrow', 'Requesting Leave')

meal_cost = float(input("Enter the meal cost: "))
calculate_total_cost(meal_cost)