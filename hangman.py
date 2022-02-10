import random
import string
with open('words.txt', 'r') as var:
    words = set()
    for line in var:
        line = line.rstrip()
        words.add(line)

    def get_word(words):
        word = random.choice(tuple(words))
        while len(word) < 8:
            word = random.choice(tuple(words))
        return word.upper()

    def hangman():
        lives = 6
        word = get_word(words)
        word_letters = set()
        for char in word:
            word_letters.add(char.upper())
        alphabet = set(string.ascii_uppercase)
        used_letters = set()
        while len(word_letters) > 0 and lives > 0:
            print('You have used these letters: ', ' '.join(used_letters))
            print(f'You have {lives} lives remaining')
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print(''.join(word_list))
            guess = input("Guess a letter: ").upper()
            if guess not in alphabet:
                guess = input("Invalid. Guess a letter: ").upper()
            if guess in used_letters:
                guess = input("You already guessed that. Guess again: ").upper()
            if guess in alphabet - used_letters:
                used_letters.add(guess)
                if guess in word_letters:
                    word_letters.remove(guess)
                else:
                    print(f'{guess} not in word. One life lost.')
                    lives = lives - 1
        if len(word_letters)>0:
            print(f"Sorry, you lose. The correct word was {word}")
        else:
            print(f"You win! You guessed {word} correctly!")

hangman()