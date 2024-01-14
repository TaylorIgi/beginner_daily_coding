'''
Goal: create a Python program that simulates a simple hangman game
Inspiration: Chat GPT
'''

def random_word(language="Any", difficulty="Any"):
    
    import pandas as pd
    import random as rd
    import pdb
    
    df_words = pd.read_excel("hangman_words.xlsx")

    if ( language != "Any" ) and ( difficulty != "Any" ):
        df_aux = df_words.loc[df_words["language"] == language]
        df_filtered = df_aux.loc[df_aux["difficulty"] == difficulty]
    elif language != "Any":
        df_filtered = df_words.loc[df_words["language"] == language]
    elif difficulty != "Any":
        df_filtered = df_words.loc[df_words["difficulty"] == difficulty]
    else:
        df_filtered = df_words
    
    my_index = rd.randint(0, df_filtered.index.max())

    choosen_word = {
        "word": df_filtered.loc[my_index, "word"].lower(),
        "language": df_filtered.loc[my_index, "language"],
        "difficulty": df_filtered.loc[my_index, "difficulty"],
        "word_index": my_index,
        "word_lenght": len(df_filtered.loc[my_index, "word"])
    }

    return choosen_word

def check_new_letter(user_past_letters, user_letter):

    for i in range(0, len(user_past_letters)):
        if user_past_letters[i] == user_letter:
            return "nok"
    return "ok"

def check_letter_in_word(choosen_word, user_word, user_letter):
    
    new_user_word = user_word
    for i in range(0, len(user_word)):
        if choosen_word[i] == user_letter:
            new_user_word[i] = user_letter
    return new_user_word

def try_choosen_word(language = "Any", difficulty = "Any"):
    
    try_again = True
    while try_again:
        try:
            choosen_word = random_word(language, difficulty)
            try_again = False
        except:
            continue
    return choosen_word

def play_game(choosen_word):

    import os

    user_word = []
    for i in range(0, len(choosen_word["word"])):
        user_word.append("_")
    user_past_letters = []
    remain_guesses = 6

    while ''.join(map(str, user_word)) != choosen_word["word"] and remain_guesses > 0:

        os.system("cls")

        print(f"You can guess wrongly {remain_guesses} more times!\n")

        user_word_str = ''.join(map(str, user_word))
        print(f"Current word: {user_word_str}")

        if len(user_past_letters) > 0:
            print(f"Past guesses: {user_past_letters}\n")

        user_letter = input("What letter is your guess? ").lower()

        while check_new_letter(user_past_letters, user_letter) == "nok":
            user_letter = input(f"{user_letter.upper()} has already been guessed! Please try another letter: ".lower())

        user_past_letters.append(user_letter)

        user_word_aux = []
        for i in range(0, len(user_word)):
            user_word_aux.append(user_word[i])

        user_word = check_letter_in_word(choosen_word["word"], user_word, user_letter)

        if user_word == user_word_aux:
            remain_guesses = remain_guesses - 1
    
    if ''.join(map(str,user_word)) == choosen_word["word"]:
        return "win"
    else:
        return "lost"


def main():

    import time
    import os

    choosen_word = try_choosen_word()
    print(choosen_word["word"])
    time.sleep(4)

    result = play_game(choosen_word)

    if result == "win":
        os.system("cls")
        print(f"\nCongrats!!! You guessed {choosen_word["word"].upper()} correctly!!!\n\n")
    elif result == "lost":
        os.system("cls")
        print(f"\nToo bad...You lost...")
        print(f"The word was {choosen_word['word'].upper()}\n\n")
    else:
        os.system("cls")
        print("\nSorry...we had some problem...\n\n")

    if input("Do you wanna play again? (Yes or No)\n").lower() == "yes":
        main()

main()