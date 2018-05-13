import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_rank(tried):
    if tried == 0 or tried == 1:
        reward = 'the Golden Crown!\n👑\n'
    elif tried == 2:
        reward = 'the Silver Ring!\n💍\n'
    elif tried == 3 or tried == 4:
        reward = 'the Bronze Medal!\n🥉\n'
    print('And it is ranked with {}'.format(reward))

def win(tried):
    noun = 'tries'
    if tried == 1:
        noun = 'try'
    print('\nCongratulate your honoured machine! It won having spent only {} {}!!!'.format(tried, noun))
    get_rank(tried)

def loose():
    print('Unsuccessfully computer ran out of tries and hence must loose forever!\n')

def guess_proper(guesses, number):
    if guesses.count(number) >= 1:
        return False
    else:
        return True

# accepts user input
def computer_guess(min, max, num_ot, user_g):
    guesses = []
    while len(guesses) < num_ot:
        print(guesses)
        comp_g = random.randint(min, max)
        while not guess_proper(guesses, comp_g):
            comp_g = random.randint(min, max)
        if comp_g > user_g:
            print('Computer went heigher with {}.\n'.format(comp_g))
            max = comp_g
        elif comp_g < user_g:
            print('Computer went lower with {}.\n'.format(comp_g))
            min = comp_g
        if comp_g == user_g:
            win(len(guesses))
            break
        if len(guesses) == num_ot - 1:
            loose()
        guesses.append(comp_g)

# sets the game
def set_game(min, max, num_ot, comp_g):

    cls()

    print('Oh, noble user! Computer has {} tries to guess your number!\n'.format(num_ot))

    guesses = []

    computer_guess(min, max, num_ot, comp_g)

# sets the values for the game and provides them to the game
def main():

    # inclusive
    min = 1
    # inclusive
    max = 10
    # number of tries
    num_ot = 5
    # computer guess, stays the same throughout the game
    user_g = int(input('Please, guess a number from 1 to 10:\n>'))

    # setting up the game
    set_game(min, max, num_ot, user_g)

# starts the app
main()

while True:
    another_run = input('Would you like to guess agains computer one more time? (Y/n)\n>')
    if another_run != 'n':
        main()
    else:
        break
print('\n')
