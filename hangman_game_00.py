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
        "word": df_filtered.loc[my_index, "word"],
        "language": df_filtered.loc[my_index, "language"],
        "difficulty": df_filtered.loc[my_index, "difficulty"],
        "word_index": my_index,
        "word_lenght": len(df_filtered.loc[my_index, "word"])
    }

    return choosen_word

word = random_word("Portuguese", "Hard")
print(word)