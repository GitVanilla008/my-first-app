number = int(input("Enter a number: "))
list = []

while number:
    list.append(number)
    number = int(input("Enter a number: "))
    break 
number = int(input("Enter a number: "))

print("Count is: ", len(list))
print("Sum is: ", sum(list))
print("Avg is: ", (sum(list) / len(list)))


