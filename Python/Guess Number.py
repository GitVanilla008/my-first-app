secret = 30

while True:
    guess = int(input("input your value: "))
    if guess == secret:
        print('congrats')
        exit ()
    else:
        if guess > secret:
            print ('too high')
        else:
            print ('too low')