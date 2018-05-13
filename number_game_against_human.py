import random

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

# accepts user input
def computer_guess(min, max, num_ot, user_g):
    guesses = []
    while len(guesses) < num_ot:
        comp_g = random.randint(min, max)
        if comp_g > user_g:
            print('Computer went heigher with {}.\n'.format(comp_g))
        elif comp_g < user_g:
            print('Computer went lower with {}.\n'.format(comp_g))
        if comp_g == user_g:
            win(len(guesses))
            break
        else:
            loose()
        guesses.append(comp_g)
        print(guesses)

# sets the game
def set_game(min, max, num_ot, comp_g):

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
