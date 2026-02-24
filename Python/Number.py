number = (input('Enter a number: '))
count = 0 
total = 0

while number == number:
    number = (input('Enter a number: '))
    count += 1
    total += number
    if number == '': 
        break

print('Number of inputs: ', count)
print('Sum of numbers: ', total)



