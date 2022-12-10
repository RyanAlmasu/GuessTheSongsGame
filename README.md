Games
Guess The Music Games

Video Demo = https://www.youtube.com/watch?v=Y4Z9irx2xEY&ab_channel=Nevermind

This project has 4 existing structures. Such as project.py , README.md , requirements.txt and test_project.

Libraries

The libraries I used in this project include :

- re = ['A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).']
- random = ['This module implements pseudo-random number generators for various distributions. For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.']

Installing libraries

- pip install regex
- pip install random

How to Play the Game

- Running the game

Hello, press enter to play hangman!

Enter -e or --exit to end game
Enter -r or --retry to restart game with another music.

---

Guess a character or the music name (10 chances left):

- Guess the music using anywords by input it on the programs
- The music's include inside the program
- If you guess wrong about 10 times then you lost
- If you guess it correct without wrong in 10 words then you win!.
- Its easy right

About the Fucntions

- main()

Main function is used as a program structure that contains the game intro. This structure contains the code to determine the random music to be selected later. There are also question frames with blanks. Then there is create music using an existing list. The last one is the code to run the game and see the result.

- select_music(musics)

Select music is a program code that will be used to display a music which will be selected and used in the game.

- question(music_name)

This code function is used to fill in the questions in the game later. By using a loop to determine if any letters are guessed in the game. Also determines user input using capital letters or regular letters, so users don't have to bother with capital letters in guessing music

- game(question, music, year)

This function is used for exporting in-game and also as the main program in the game. In this code there is a program that will be used to create a music list in the form of a string. Then there is a code copy of the music list. Then make a list of music that will be guessed. Then there is a counter in the game with the logic already created. If the user guesses wrong, a counter from the program will appear. When the user guesses incorrectly 5 times, a hint will appear that will make it easier for the user to guess the music. And at that time, the year of release of the music will appear.

- get_result()

This function determines an end result of the user guessing. Is successful or failed.

Author = Ryan Ali Mas'ud
