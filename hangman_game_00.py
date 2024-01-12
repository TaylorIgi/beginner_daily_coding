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
        df_filtered = df_aux.loc[df_words["difficulty"] == difficulty]
    elif language != "Any":
        df_filtered = df_words.loc[df_words["language"] == language]
    elif difficulty != "Any":
        df_filtered = df_words.loc[df_words["difficulty"] == difficulty]
    else:
        df_filtered = df_words
    
    my_index = rd.randint(0, df_filtered.index.max())
    print(my_index)
    print(df_filtered.loc[my_index, "word"])
    print(df_filtered.loc[my_index, "language"])
    print(df_filtered.loc[my_index, "difficulty"])

random_word("Portuguese", "Hard")