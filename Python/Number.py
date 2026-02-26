count = 0 
total = 0

while True:
    number = (input('Enter a number: '))
    print('You entered: ', number)
    if number.isdigit():
        number = int(number)
        count += 1
        total += number
    else:
        print('Invalid input')
        break
    

print('Number of inputs: ', count)
print('Sum of numbers: ', total)
print('Average: ', total/count)




