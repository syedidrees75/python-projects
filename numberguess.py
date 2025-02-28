import random

number = random.randint(1,100)
while True:
    try :
        guess=int(input('guess the number between 1 and 100: '))
        if guess < number - 5 :
            print('its too low')
        elif guess > number + 5:
            print('its too high')
        elif number -5 < guess < number:
            print('its low')
        elif number < guess < number + 5 :
            print('its high')
        else:
            print('you have guessed it correct')
            break
    except ValueError:
        print('Please enter a valid number')

