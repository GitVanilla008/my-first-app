price = 14
print("Cost of item is: $", price)

money = int(input("Enter money amount: "))

while money < price:
    print("Enter $", price - money, "more")
    extra = int(input("Insert more money: "))
    money = money + extra

change = money - price

if change > 0:
    print("Change is", change)
else:
    print("No change")
    