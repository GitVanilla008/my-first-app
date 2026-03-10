weight = float(input("Enter the weight of your parcel: "))

if weight <= 2:
    cost = 5

elif weight > 2 and weight <= 5: 
    cost = 10

else:
    cost = 18

print("the cost of your delivery is: ", cost)
