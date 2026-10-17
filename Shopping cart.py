items = input("what item would you like to buy")
price = float(input("what is the price"))
quantity = int(input("how many would you like?"))
Total =  price * quantity

print(Total)
print(f"you have bought {quantity} x {items}/s")
print(f"your total is: R{Total}")