price = 14
money = int(input("Enter money amount: "))
change = money - price
if money > price:
    print("change is", change)
if money == price:
    print("no change")
if money < price:
    print("enter $", price - money)
