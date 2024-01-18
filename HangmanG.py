import random  # Function to select a random word from a list
import string  # Function to perform various operations on strings

words = ["aboard","abrasive","absent","absorbing","banana", "orange", "grape", "watermelon", "strawberry", "pineapple", "kiwi", "blueberry", "peach",
    "apricot", "plum", "pear", "cherry", "mango", "lemon", "lime", "coconut", "pomegranate", "fig",
    "avocado", "blackberry", "raspberry", "cranberry", "papaya", "dragonfruit", "guava", "lychee", "nectarine", "tangerine",
    "melon", "persimmon", "starfruit", "cantaloupe", "honeydew", "passionfruit", "mulberry", "boysenberry", "elderberry", "grapefruit",
    "quince", "date", "kumquat", "plantain", "gooseberry", "rhubarb", "durian", "jackfruit", "breadfruit", "acai",
    "soursop", "salak", "ackee", "pawpaw", "feijoa", "mangosteen", "carambola", "rambutan", "breadnut", "chirimoya",
    "longan", "mamey", "sapote", "ugli", "tamarillo", "loquat", "saskatoon", "damson", "medlar", "quandong",
    "santal", "surinam", "goumi", "yuzu", "jabuticaba", "salmonberry", "lingonberry", "cloudberry", "loganberry", "boysenberry",
    "goji", "persimmon", "feijoa", "bilberry", "cloudberry", "elderberry", "pomelo", "tayberry", "ugli", "clementine",
    "sugarcane", "quince", "pawpaw", "chayote", "amaranth"]  # words for the game

hangman_visually = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

def get_the_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangmanGame():
    word = get_the_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters_again = set()

    lives = 7

    # taking input to check
    while len(word_letters) > 0 and lives > 0:
        print('You have only', lives, 'lives')


        word_list = [letter if letter in used_letters_again else '-' for letter in word]
        print(hangman_visually[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess the letter: ').upper()
        if user_letter in alphabet - used_letters_again:
            used_letters_again.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # if the answer is wrong, it takes a life away
                print('\nThis letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters_again:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nUse a valid letter.')

    #checking the lives
    if lives == 0:
        print(hangman_visually[lives])
        print('YOU DIED SORRY!!!  The word is', word)
    else:
        print('WHOA! YOU WON THE GAME!!!', word, '!!')


if __name__ == '__main__':
    hangmanGame()