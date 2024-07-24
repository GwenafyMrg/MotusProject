def hide_word(word):
    ''''''
    string = "";
    for letter in range(len(word)):
        string += "X";
    return string;

# def demand_answer2():
#     user_word = str(input("Tapez votre proposition de réponse : "));
#     if (len(hiding_word) > len(user_word)):
#         print("Votre mot est trop petit");
#         demand_answer();
#     elif (len(hiding_word) < len(user_word)):
#         print("Votre mot est trop grand");
#         demand_answer();
#     else :
#         user_word = user_word.lower();
#         return user_word;

def demand_answer():
    ''''''
    user_word = "";
    while (len(hiding_word) != len(user_word)):
        print("Votre mot doit contenir", len(hiding_word), "caractères.")
        user_word = str(input("Tapez votre proposition de réponse : "));
    user_word = user_word.lower();
    return user_word;

def standardize_word(word):
    ''''''
    standart_word = "";
    for letter in word :
        if (letter == "é" or letter == "è" or letter == "ê"):
            letter = "e";
        if (letter == "ï"):
            letter == "i";
        if (letter == "ù"):
            letter == "u";
        standart_word += letter;
    return standart_word;
        
def correct(word):
    for letter in word:
        carac = ord(letter);
        if (carac < 97 or carac > 122):
            print("Votre proposition ne doit contenir que des lettres et pas d'autres caractères...")
            return False;
    return True;

def compare_word(proposition, word_to_find, hiding_word):
    hiding_word = list(hiding_word);
    for i in range(len(word_to_find)):
        if (hiding_word[i] == "X" and proposition[i] == word_to_find[i]):
            hiding_word[i] = proposition[i];
            if (proposition[i] not in reveal_letters):
                reveal_letters.append(proposition[i]);
        if (hiding_word[i] == "X" and proposition[i] != word_to_find[i]):
            if (proposition[i] not in wrong_letters):
                wrong_letters.append(proposition[i]);
    hiding_word = "".join(hiding_word)
    print("Voici les lettres que vous avez révélé dans le mot :",hiding_word);
    print("Lettres révélées :", reveal_letters);
    print("Mauvaises lettres :",wrong_letters);
    return hiding_word;

words = ["Maison"];
word_to_find = words[0];
hiding_word = hide_word(word_to_find);
user_word = "";
reveal_letters = [];
wrong_letters = [];
tries = 0;

# print(words_to_find);
# print(hiding_word);
# print("\n");
# print(user_word);
# user_word = demand_answer();
# print(user_word);

'''Test de la fonction de comparaison de mot manuel.'''
print("Voici le mot que vous devez révélé :",hiding_word);
hiding_word = compare_word("marron","maison","XXXXXX");
print("Voici le mot que vous devez révélé :",hiding_word);
hiding_word = compare_word("marbre","maXXon","XXXXXX");

#50 min
#10h40
