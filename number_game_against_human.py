import random

wrong_input_message = 'The input is wrong. The game terminates.'
win_message = 'Computer hit!'
loose_message_h = 'Computer misses higher with {}'
loose_message_l = 'Computer misses lower with {}'

guesses = []

# guess the number
try:
    my_guess = int(input('Please, guess a number from 1 to 10:\n>'))
except ValueError:
    print(wrong_input_message)
else:
    if my_guess < 1 or my_guess > 10:
        print(wrong_input_message)
    else:
        min = 1
        max = 10
        while len(guesses) < 5:
            # let the computer to guess the number
            c_guess = random.randint(min, max)
            # if the number matches display winning message
            if c_guess == my_guess:
                print(win_message)
                break
            # if the number is higher let the computer guess in that direction
            elif c_guess > my_guess:
                print(loose_message_h.format(c_guess))
                max = c_guess
            # if the number is lower let the computer guess in that direction
            else:
                print(loose_message_l.format(c_guess))
                min = c_guess
            guesses.append(c_guess)
    if len(guesses) == 5:
        print('\nComputer lost!')
    else:
        print('\nComputer won!')
