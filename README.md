
[Link to my Blogpost](https://pumoxi.com/2024/11/10/building-a-hangman-game-with-python/)

# Hangman Game - Fruits and Vegetables Edition

This is a simple Hangman-style game built in Python. The game randomly selects a word from a list of fruits and vegetables, and players try to guess the word one letter at a time. You have 7 lives—each incorrect guess loses one life, and a part of the hangman is drawn. If you run out of lives before guessing the word, you lose the game!

## Features

- **Word List**: Over 40 fruit and vegetable names to guess.
- **Guess Feedback**: Correct guesses reveal letters, while incorrect guesses reduce lives and display the hangman.
- **Endgame Detection**: Win the game by guessing the word, or lose by running out of lives.

## How to Play

1. The program will choose a random word from the list.
2. You will be prompted to guess a letter for the word.
3. If the letter is in the word, it will be revealed in the blank spaces. Otherwise, you lose a life.
4. The game ends when you guess the word or run out of lives.

## Example Output

```plaintext
You have 7 lives left.

_ _ _ _ _

Guess a letter for fruit and vegetable: a

_ a _ a _ a

You have 6 lives left.
You guessed "z", that's not in the word. You lose a life.

+---+
|   |
O   |
/|\  |
/    |
      |
=========