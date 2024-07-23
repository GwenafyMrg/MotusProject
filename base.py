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
            return False;
    return True;

words = ["Maison"];
words_to_find = words[0];
hiding_word = hide_word(words_to_find);
user_word = demand_answer();
letters = [];
tries = 0;


# print(words_to_find);
# print(hiding_word);
# print(user_word);

#35 min
#18h