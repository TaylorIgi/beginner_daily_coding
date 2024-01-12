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
    for i in range(0, len(user_letter)-1):
        if user_past_letters[i] == user_letter:
            return "nok"
    return "ok"

def check_letter_in_word(choosen_word, user_word, user_letter):
    new_user_word = user_word
    for i in range(0, len(user_word)):
        print(f"i = {i} word_letter = {choosen_word[i]} user_letter = {user_letter}")
        if choosen_word[i] == user_letter:
            new_user_word[i] = user_letter
    return new_user_word

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# Testes 
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# choosen_word = random_word()
choosen_word = {"word": "arara", "language": "Portuguese", "difficulty": "Easy", "word_index": 0, "word_lenght": 5}

user_word = []
for i in range(0, len(choosen_word["word"])):
    user_word.append("_")
user_past_letters = []

user_letter = input("What letter is your guess? ").lower()

while check_new_letter(user_past_letters, user_letter) == "nok":
    user_letter = input(f"{user_letter.upper()} has already been guessed! Please guess another letter: ".lower)

user_past_letters.append(user_letter)
user_word = check_letter_in_word(choosen_word["word"], user_word, user_letter)

print(choosen_word)
print(user_word)
print(user_past_letters)
