def hide_word(word):
    ''''''
    string = "";
    for letter in range(len(word)):
        string += "X";
    return string;

def demand_answer(hiding_word):
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
    ''''''
    for letter in word:
        carac = ord(letter);
        if (carac < 97 or carac > 122):
            print("Votre proposition ne doit contenir que des lettres et pas d'autres caractères...")
            return False;
    return True;

def compare_word(proposition, word_to_find, hiding_word):
    ''''''
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
    display(hiding_word);
    return hiding_word;

def display(string):
    ''''''
    gap = len(string);
    print("+" + "-"*5 + "-"*gap + "-"*5 + "+");
    print("|" + " "*5 + string + " "*5 + "|");
    print("+" + "-"*5 + "-"*gap + "-"*5 + "+");

    if (reveal_letters != []):
        print("Les lettres révélées et utilisées dans le mot sont :\n", reveal_letters);
    if (wrong_letters != []):
        print("Les mauvaises lettres que vous avez utilisées sont :\n",wrong_letters);

def end_display():
    ''''''
    pass

words = ["maison"];
reveal_letters = [];
wrong_letters = [];
tries = 0;

def start():
    word_to_find = standardize_word(words[0]);
    hiding_word = hide_word(word_to_find);
    user_word = "";
    display(hiding_word);
    while (hiding_word != word_to_find):
        user_word = demand_answer(hiding_word);
        user_word = standardize_word(user_word);
        if (correct(user_word) == False):
            print("Votre proposition de mot est incorrecte.");
        else : 
            hiding_word = compare_word(user_word,word_to_find,hiding_word);
    print("Bravo !");
    end_display();


# print(words_to_find);
# print(hiding_word);
# print("\n");
# print(user_word);
# user_word = demand_answer();
# print(user_word);

# '''Test de la fonction de comparaison de mot manuel.'''
# hiding_word = compare_word("marbre","maison","XXXXXX");
# hiding_word = compare_word("maison","maXXon","XXXXXX");

start();

#2h 
#19h