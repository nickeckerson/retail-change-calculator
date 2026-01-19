# Module 2 In-Class Activity Program 2

price = float(input("What is the listed price of the item: "))
customer_paid = float(input("How much did the customer pay: "))
change = customer_paid - price - (price * 0.06)
print(f"They get ${change:.2f} in change")