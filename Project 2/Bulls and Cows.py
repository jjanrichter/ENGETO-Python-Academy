# Bulls & Cows - JR

def main() -> None:
    global hrac
    hrac = jmeno_hrace()
    uvod(hrac)
    game()


def jmeno_hrace() -> str:
    return input('What\'s your name? ')

def uvod(hrac: str) -> None:
    print(f'''Hi {hrac}!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
To quit game immediately press \'q\'.''')

def pc_cislo() -> str:
    import random
    data = list(range(10))
    random.shuffle(data)
    secret_word = f'{data[0]}{data[1]}{data[2]}{data[3]}'

    #print(secret_word)

    return secret_word


def user_cislo() -> str:
    user_guess = input('Enter a 4-digit number please: ')
    return user_guess


def internal_game(secret_word: str, user_guess: str):

    global bulls
    global cows



    for i, pismeno in enumerate(secret_word):
        r10 = []
        for y in range(10):
            y = str(y)
            r10.append(y)

        if not user_guess:
            print('No input provided.')
            break

        elif user_guess in ('q', 'Q'):
            print('Game over on your request.')
            quit()

        elif len(user_guess) != 4:
            print('Your guess has more or less than 4 digits.')
            break

        elif user_guess[i] == pismeno:
            bulls += 1

        elif user_guess[i] in secret_word:
            cows += 1

        elif user_guess[i] not in r10:
            print('Use only numerical values.')
            break

    print(f'{bulls} bulls, {cows} cows')
    vyhodnoceni(bulls, pokus)


def vyhodnoceni(bulls: int, pokus: int) -> None:
    while bulls == 4:
        if pokus == 1:
            print(f'Correct, you\'ve guessed the right number in just {pokus} guess!')
            break

        elif pokus > 1:
            print(f'Correct, you\'ve guessed the right number in {pokus} guesses!')
            break


def timer() -> None:
    import time
    global t1
    t1 = round(time.perf_counter() - t0,2)
    print(f'You have finished this game in {t1} seconds')
    q1 = input('Do you want to play again? Type \'Yes\' for a new game.')
    if q1 in ('Y', 'y', 'Yes', 'yes'):
        game()
    else:
        print('The End')


def game():
    import time
    global t0
    t0 = time.perf_counter()

    pc = pc_cislo()

    global pokus
    pokus = 0

    for y in range(25):
        global bulls
        bulls = 0
        global cows
        cows = 0

        user = user_cislo()

        pokus += 1

        internal_game(pc, user)

        if bulls == 4:
            break

    timer()


main()
