#------------------------------------Packages------------------------------------------#

import csv
import random

#------------------------------------Traitment Functions------------------------------------------#

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
            letter = "i";
        if (letter == "ù"):
            letter = "u";
        if (letter == "ç"):
            letter = "c";
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
    return (hiding_word, reveal_letters, wrong_place, wrong_letters);

def traitment(word, hiding_word):
    '''
    Vérifie la conformité de la proposition et passe celle-ci dans un format standart.
    Puis compare la proposition avec le mot caché.
    Args :
        word(string)                --> la proposition du joueur.
        hiding_word(string)         --> le mot caché à trouver.
    Return :
        hiding_word(string)         --> le mot caché après la comparasion avec la proposition.
    '''

    user_word = None;
    global tries;

    if (hiding_word != word_to_find and tries != max_tries):
        user_word = word;
        user_word = standardize_word(user_word);
        if (correct(user_word) == True):
            tries += 1;
            hiding_word = compare_word(user_word,word_to_find,hiding_word);
    return hiding_word;

#------------------------------------Functions for the Interface ------------------------------------------#

def getTryLimit(n):
    '''
    Récupère et enregistre la limite d'essai.
    Args :
        n(int)              --> limite d'essai.
    Return :
        None
    '''
    global max_tries;
    if (n == 0): max_tries = None;
    else: max_tries = n;

def getHidingWord():
    '''
    Traduit le mot à trouver en mot caché et le retourne.
    Args :
        None
    Return :
        hiding_word(string)         --> le mot masqué.
    '''
    global hiding_word;
    hiding_word = hide_word(word_to_find);
    return hiding_word;

def reset_data():
    '''
    Vide les listes contenant les lettres traitées ainsi que la limite d'essai.
    Et séléctionne un autre mot au hasard.
    Args :
        None
    Return :
        tuple               --> contient le nouveau mot à trouver et les listes de traitement de lettres.
    '''
    global tries;
    global word_to_find;
    tries = 0;
    word_to_find = standardize_word(words[random.randint(0,len(words)-1)]);
    reveal_letters.clear();
    wrong_place.clear();
    wrong_letters.clear();
    return (word_to_find, reveal_letters, wrong_place, wrong_letters);

def doYouWin(hiding_word):
    '''
    Vérifie si le jeu est gagné, perdu ou encore en cours selon le mot caché et le nombre d'essai réalisés.
    Args :
        hiding_word(string)         --> le mot caché.
    Return :
        result(bool)                --> True, le jeu est gagné.
                                    --> False, le jeu est perdu.
                                    --> None, le jeu est encore en cours.
    '''

    result = [None, ""];
    #Without try limit:
    if (max_tries == None):
        #If the hiding word is find.
        if (hiding_word == word_to_find):
            result[0] = True;
            result[1] = f"Congratulations ! You found the word {word_to_find}. \n You took {tries} tries to success.";
    #With try limit:
    else :
        #If there are too many tries.
        if (hiding_word != word_to_find and tries >= max_tries):
            result[0] = False;
            result[1] = f"Too bad ! You didn't find the word '{word_to_find}'... Vous avez proposez trop de mots sans succes.";
        #If the hiding word is find.
        elif (hiding_word == word_to_find and tries < max_tries):
            result[0] = True;
            result[1] = f"Congratulations ! You found the word {word_to_find}. \n You took {tries} tries to success.";
    return result;

#------------------------------------Main programm------------------------------------------#

#Rempli le tableau de mot:
words = [];
with open('frequence.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=";");

    for row in reader:
        words.append(row[2]);

#------------------------------Initializing Globales Variables----------------------------#
word_to_find = standardize_word(words[random.randint(0,len(words)-1)]);
hiding_word = "";
tries = 0;
reveal_letters = [];
wrong_place = [];
wrong_letters = [];