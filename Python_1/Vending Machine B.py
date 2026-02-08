item = str((input("Enter item A,B, or C: "))).upper()
A = 120
B = 60
C = 75

#select item
while item not in ("A","B","C"):
    item = (input("Enter item A,B, or C: "))
paid = int(input("Enter amount tendered: "))

#printing change
if item == "A":
    print("change is", paid - A)
elif item == "B":
    print("change is", paid - B)
else:
    print("change is", paid - C)

#coin input
total = 0
coin = int(input("Enter coin: "))
print("amount inserted", coin)
while coin != 0:
    total = total + coin
    coin = int(input("Enter coin: "))
    print("amount inserted", total)