import random
import re

musics = [
    'Creep (2007)',
    'I dont love you (2006)',
    'I miss you (2009',
    'Kings for a day (2010',
    'Helena (2007)',
    'Famous last word (2008)',
    'The kill (2009)',
    'The pretender (2006)',
    'Im not okay (2007)',
    'Thank you for the venom (2011)',
    'Umbrella (2012)',
    'The ghost of you (2009)',
    'Summertime (2010)',
    'Hold on till may (2009)',
    'Bring me to life (2001)',
]


def main():
    print("\nWelcome to the Guess The Music Games")
    input('\nHello, press enter to play!')
    print('\nEnter -e or --exit to end game')
    print('Enter -r or --retry to restart game with another music.\n\n')


    # select a random music
    music, year = select_music(musics)

    # print music name and year - DEMO
    # print(f'(Demo purpose - music name : {music})\n')

    # frame question with blanks
    ques = question(music)

    # create list of musicname
    music_list = [letter for letter in music]

    # run game and get result
    res = game(ques, music_list, year)

    if res == 'exit':
        print('Game Ended.')
        return
    if res == True or res == False:
        print(get_result(res))


def select_music(musics):
    music = random.choices(musics)

    if search := re.search(r'^([A-Za-z0-9_.-:,\' ]*) \((\d{4})\)$', music[0]):
        return search.groups()


def question(music_name):
    q = []
    for letter in music_name:
        if letter.isalpha() or letter.isnumeric():
            q.append('_')
        else:
            q.append(letter)

    return q


def game(question, music, year):

    # create musicname in str
    musicname = ''.join(map(str, music)).strip().lower()

    # copy musicname list
    musiccp = music.copy()

    # create a list of all elements of music in lowercase
    lower_music = [x.lower() for x in music]

    # initiate counter
    count = 1
    hint = False

    while count < 11 and '_' in question:
        print(*question, '\n')

        if count > 5 and hint == False:
            print('To get hint, enter \'--hint\'\n')

        answer = input(f'Guess a character or the music name ({11-count} chances left): ').lower().strip()

        if answer == '--hint' and count > 5 and hint == False:
            print(f'The music was released in {year}\n')
            hint = True

        elif answer == '--exit' or answer == '-e' or answer == '--quit':
            return 'exit'

        elif answer == '-r' or answer == '--retry':
            print('\n')
            return main()

        elif answer in lower_music:
            while answer in lower_music:
                index = lower_music.index(answer)
                question[index] =  musiccp[index]
                lower_music[index] = 'NULL'

        elif answer == musicname:
            question=musiccp.copy()
            break

        else:
            # if wrong guess increase counter
            count+=1

    if count < 11:
        print(*question,'\n')
        return True
    return False


def get_result(result):
    if result:
        return 'Correct!'
    else:
        return 'Incorrect, try again!'


if __name__ == "__main__":
    main()