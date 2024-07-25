import csv
import random

def hide_word(word):
    ''''''
    string = word[0];
    for letter in range(len(word)-1):
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

def end_display(word, n):
    ''''''
    congrat_txt = "Félicitations ! Vous avez trouvé le mot '"+ word + "'.";
    tries_txt = "Il vous a fallu " + str(n) + " essaies pour réussir."
    print("+" + "-"*10 + "-"*len(congrat_txt) + "-"*10 + "+");
    print("|" + " "*10 + congrat_txt + " "*10 + "|");
    print("|" + " "*10 + tries_txt + " "*(10+len(congrat_txt)-len(tries_txt)) + "|");
    print("+" + "-"*10 + "-"*len(congrat_txt) + "-"*10 + "+");

def start():
    word_to_find = standardize_word(words[random.randint(0,len(words)-1)]);
    hiding_word = hide_word(word_to_find);
    user_word = "";
    tries = 0;
    display(hiding_word);
    while (hiding_word != word_to_find):
        user_word = demand_answer(hiding_word);
        user_word = standardize_word(user_word);
        if (correct(user_word) == False):
            print("Votre proposition de mot est incorrecte.");
        else : 
            tries += 1;
            hiding_word = compare_word(user_word,word_to_find,hiding_word);
    end_display(word_to_find,tries);


words = [];
with open('frequence.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=";");

    for row in reader:
        words.append(row[2]);
reveal_letters = [];
wrong_letters = [];

start();

#2h10 
#18h26