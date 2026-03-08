item = str((input("Enter item A,B, or C: "))).upper()
A = 120
B = 60
C = 75

#select item
while item not in ("A","B","C"):
    item = (input("Enter item A,B, or C: "))

if item == "A":
    print("enter", A)
elif item == "B":
    print("enter", B)
else:
    print("enter", C)

total = 0
coin = int(input("Enter coin: "))