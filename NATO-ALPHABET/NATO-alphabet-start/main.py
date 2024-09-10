student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

key_list = []
value_list = []
#Looping through dictionaries:
for (key, value) in student_dict.items():
    key_list.append(key)
    value_list.append(value)


import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
dict2 = {}
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
for (index, row) in df.iterrows():
    dict2[row.letter] = row.code

# print(dict2)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Whats your name? ").upper()

list = [words for words in user_input]

empty_list = []
for let in list:
    print(f"{let}: {dict2[let]}")
    empty_list.append(dict2[let])

print(empty_list)