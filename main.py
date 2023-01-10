import pandas

WANT_TO_EXIT = False
while not WANT_TO_EXIT:
    data = pandas.read_csv("Phonetic_Alphabet.csv")
    phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
    user_input = input("Enter a word? ").upper()
    if user_input == "EXIT":
        WANT_TO_EXIT = True
    else:
        output_list = [phonetic_dic[letter] for letter in user_input]
        print(output_list)
