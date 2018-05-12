import random

def get_rank(tried):
    # reward = 'the Bronze Medal!\n🥉'
    if tried == 0 or tried == 1:
        reward = 'the Golden Crown!\n👑'
    elif tried == 2:
        reward = 'the Silver Ring!💍\n'
    elif tried == 3 or tried == 4:
        reward = 'the Bronze Medal!\n🥉'
    print('And you are ranked for {}'.format(reward))

def win(tried):
    noun = 'tries'
    if tried == 1:
        noun = 'try'
    print('Congratulations and salutations! You win having spent only {} {}!!!'.format(tried, noun))
    get_rank(tried)

def loose(num_ot, tried):
    tries_left = num_ot - tried
    noun = 'tries'
    if tried == num_ot - 1:
        noun = 'try'
    sentence = 'Luck has been bad to you this time - your guess was wrong. You have {} more {}!'.format(tries_left, noun)
    if tried == num_ot:
        sentence = 'Unsuccessfully you ran out of tries and hence must loose! But only for now...\nAnd no reward either! Come by tomorrow!\n'
    print(sentence)

# accepts user input
def get_input(num_ot, comp_g):
    tried = 0
    while tried < num_ot:
        try:
            u_in = int(input('> '))
        except ValueError:
            print('Invalid input also counts as a try!')
            tried += 1
            loose(num_ot, tried)
        else:
            if comp_g > u_in:
                print('The guessed number is higher than the one you guessed.\n')
            elif comp_g < u_in:
                print('The guessed number is lower than the one you guessed.\n')
            if comp_g == u_in:
                win(tried)
                break
            else:
                tried += 1
                loose(num_ot, tried)

# sets the game
def set_game(min, max, num_ot, comp_g):

    print('Oh, noble user! You have {} tries to guess an already generated number between {} and {}! Think responsively!\n'.format(num_ot, min, max))

    get_input(num_ot, comp_g)

# sets the values for the game and provides them to the game
def main():

    # inclusive
    min = 1
    # inclusive
    max = 10
    # number of tries
    num_ot = 5
    # computer guess, stays the same throughout the game
    comp_g = random.randint(min, max)

    # setting up the game
    set_game(min, max, num_ot, comp_g)

# starts the app
main()

while True:
    another_round = input('Would you like to play one more time? (y/n)').upper()
    if another_round == 'Y' or another_round == 'YES':
        main()
    elif another_round == 'N' or another_round == 'NO':
        break
    else:
        continue
print('\n')
