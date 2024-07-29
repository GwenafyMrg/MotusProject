#------------------------------------Packages------------------------------------------#

import csv
import random

#------------------------------------Functions------------------------------------------#

def hide_word(word):
    '''
    Fonction permettant de masquer un mot à base d'une suite de caractères 'X'
    Args :
        word(string)    --> le mot que nous souhaitons masquer.
    Return :
        string(string)  --> un string composé d'une suite de 'X' de même taille que l'argument word.
    '''
    #On ne souhaite pas masqué la première lettre du mot pour aider l'utilisateur dans sa recherche.
    string = word[0];
    for letter in range(len(word)-1):
        string += "X";
    return string;

def demand_answer(hiding_word):
    '''
    Demande un mot à l'utilisateur, tant que celui-ci soit de la même taille que le mot masqué.
    Le mot est ensuite passé en minuscule.
    Args :
        hiding_word(string)     --> mot masqué que l'utilisateur doit retrouver.
    Return : 
        user_word(string)       --> mot proposé par l'utilisateur en minuscule.
    '''
    user_word = "";
    while (len(hiding_word) != len(user_word)):
        #On indique à le nombre de caractère attendu.
        print("Enter word of", len(hiding_word), "letters.")
        user_word = str(input("Your proposition : "));
    user_word = user_word.lower();
    return user_word;

def standardize_word(word):
    '''
    Modifie le mot afin de supprimer les caractères accentués.
    Args :
        word(string)            --> un mot contenant des caractères accentués.
    Return :
        standart_word(string)   --> le mot ne contenant que des lettres non accentuées.
    '''
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
    '''
    Vérifie que la variable passé en argument ne contient que des lettres minuscules allant de a à z.
    Args :
        word(string)    --> un mot contenant des caractères quelconques.
    Return :
        boolean         --> True si le mot est composé uniquement de caractère entre a et z. False sinon.
    '''
    for letter in word:
        carac = ord(letter);
        if (carac < 97 or carac > 122):
            print("Your word must contain characters between 'a' and 'z' only...")
            return False;
    return True;

def start_display():
    '''
    Affiche l'introduction du jeu.
    Args :
        None
    Return :
        None
    '''
    intro = "Welcome in Motus Game, the goal ? Find the hiding word.";
    print("+" + "-"*5 + "-"*len(intro) + "-"*5 + "+");
    print("|" + " "*5 + intro + " "*5 + "|");
    print("+" + "-"*5 + "-"*len(intro) + "-"*5 + "+", end="\n\n");

def display(new_hiding_word):
    '''
    Affiche le mot masqué et l'état de chaque lettre utilisé dans la proposition de l'utilisateur.
    Args :
        new_hiding_word(string)     --> le mot masqué.
    Return :
        None
    '''
    gap = len(new_hiding_word);
    print("+" + "-"*5 + "-"*gap + "-"*5 + "+");
    print("|" + " "*5 + new_hiding_word + " "*5 + "|");
    print("+" + "-"*5 + "-"*gap + "-"*5 + "+", end="\n\n");

    if (reveal_letters != []):
        print("This letters are correct and at the good place :\n", reveal_letters);
    if (wrong_place != []):
        print("This letters are correct but at the wrong place :\n", wrong_place);
    if (wrong_letters != []):
        print("This letters not appear in the word :\n",wrong_letters);

def end_display(finding_word, tries, result):
    '''
    Affichage à la fin de la partie quand l'utilsiteur a découvert le mot à trouver.
    Args :
        finding_word(string) --> le mot découvert.
        n(int)          --> le nombre d'essai qu'il a fallu pour découvrir le mot.
        resutl(boolean) --> resultat de la partie
    Return :
        None
    '''
    if (result == True):
        congrat_txt = "Congratulations ! You found the word : '"+ finding_word + "'.";
        tries_txt = "You took " + str(tries) + " tries to success.";
    else:
        congrat_txt = "Too bad ! You didn't find the word : '"+ finding_word + "'.";
        tries_txt = "Vous avez proposez trop de mots sans succés.";
    stats = "You used " + str(len(wrong_letters)) + " wrong letters.";

    print("+" + "-"*10 + "-"*len(congrat_txt) + "-"*10 + "+");
    #Afficher le message de félicitations.
    print("|" + " "*10 + congrat_txt + " "*10 + "|");
    #Afficher le nombre d'essais.
    print("|" + " "*10 + tries_txt + " "*(len(congrat_txt)-len(tries_txt)+10) + "|");
    #Afficher le nombres de lettres incorrectes.
    print("|" + " "*10 + stats + " "*(len(congrat_txt)-len(stats)+10) + "|");
    print("+" + "-"*10 + "-"*len(congrat_txt) + "-"*10 + "+", end="\n\n");

def compare_word(proposition, word_to_find, hiding_word):
    '''
    Compare la proposition de l'utilisateur avec le mot masqué en s'appuyant sur le mot à trouver.
    Args :
        proposition(string)     --> le mot proposé par l'utilsateur.
        word_to_find(string)    --> le mot que l'utilisateur doit trouver.
        hiding_word(string)     --> le mot masqué contenant des 'X' et des lettres révélés par l'utilisateur.
    Return :
        hiding_word(string)     --> le mot masqué et actualisé une fois que l'utilisateur a proposé son mot.
    '''
    #conversion des chaines de caractères en liste afin de faciliter la manipulation.
    hiding_word = list(hiding_word);
    temp_hiding_word = list(hide_word(word_to_find))
    word_to_find = list(word_to_find);
    proposition = list(proposition);

    #Suppression des premières lettres puisque la première lettre du mot masqué est visible.
    del(word_to_find[0]);
    del(proposition[0]);
    del(temp_hiding_word[0]);

    for i in range(len(proposition)):
        letter = proposition[i];
        #Si la lettre est incorrecte (ne se trouve pas dans le mot à trouver).
        if (letter not in word_to_find):
            if (letter not in wrong_letters):
                wrong_letters.append(letter);
        #Si la lettre est correcte (se trouve dans le mot à trouver).
        else :
            #Si on a trouvé tous les emplacements de la lettre dans le mot.
            if (word_to_find.count(letter) == temp_hiding_word.count(letter)):
                continue
            #Si la lettre est bien placé.
            elif (letter == word_to_find[i]):
                hiding_word[i+1] = letter;
                if (letter not in reveal_letters):
                    reveal_letters.append(letter);
                if (letter in wrong_place):
                    wrong_place.remove(letter);
            #Si la lettre n'est pas bien placé.
            else :
                if (letter not in wrong_place):
                    wrong_place.append(letter);
    #Conversion de la liste en chaine de caractères.
    hiding_word = "".join(hiding_word)
    display(hiding_word);
    return hiding_word;

def start():
    '''
    Demande une limite d'essai pour plus de difficulté, Lance la partie ; Pioche un mot parmi une liste, demande un mot à l'utilisateur en 
    vérifiant sa compatibilité avec le jeu, s'arrête et affiche le message de fin une fois que 
    le mot masqué soit entièrement révélé.
    Args :
        None
    Return :
        None
    '''
    start_display();

    # word_to_find = standardize_word(words[random.randint(0,len(words)-1)]);
    word_to_find = "marron";
    hiding_word = hide_word(word_to_find);
    user_word = "";
    tries = 0;

    #Demande si le joueur souhaite une limite d'essaies :
    response = input("* Do you want to set try limit ? Press 'Y' or 'N' : ").strip().upper();
    while play not in ["Y", "N"]:
        print("Invalid input. Please enter 'Y' or 'N'.")
        response = input("* Do you want to set try limit ? Press 'Y' or 'N' : ").strip().upper();
    
    if (response == 'N'):
        max_tries = None
    else:
        try :
            max_tries = int(input("* How many tries do you want for this part ? "));
        except ValueError:
            print("Invalid input. You must enter a number correct... \nThe part will start without try limit.");
    
    #Part start
    display(hiding_word);
    while (hiding_word != word_to_find and tries != max_tries):
        user_word = demand_answer(hiding_word);
        user_word = standardize_word(user_word);
        if (correct(user_word) == False):
            print("Your proposition is incorrect.");
        else : 
            tries += 1;
            hiding_word = compare_word(user_word,word_to_find,hiding_word);
    #Si le mot n'a pas été trouvé et que le nombre d'essaies est atteint.
    if (hiding_word != word_to_find and tries == max_tries):
        win = False;
    #Si le mot a été trouvé sur le dernier essai.
    else:
        win = True;
    end_display(word_to_find,tries,win);

#------------------------------------Main programm------------------------------------------#

#Rempli le tableau de mot
words = [];
with open('frequence.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=";");

    for row in reader:
        words.append(row[2]);

#Start the first game.
play = "Y";
while (play == "Y"):
    #Initialise les tableaux d'états pour les différentes lettres.
    reveal_letters = [];
    wrong_place = [];
    wrong_letters = [];
    start();

    play = input("* Do you want to play again? Y / N: ").strip().upper()
    while play not in ["Y", "N"]:
        print("Invalid input. Please enter 'Y' or 'N'.")
        play = input("* Do you want to play again? Y / N: ").strip().upper()
        
print("You left the game. Goodbye !")

#Environ 5h55 de projet incluant la réfléxion, le code et la documentation.
#1