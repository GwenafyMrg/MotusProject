#------------------------------------Packages------------------------------------------#

import tkinter as tk
import tkinter.messagebox as msgBox
import functions as fn

#------------------------------------Functions------------------------------------------#

root = tk.Tk();

def clear_windows():
    '''
    Détruit tous les widgets de l'interface à l'exception du widget contenant le titre.
    Args:
        None
    Return :
        None
    '''
    for widget in root.winfo_children():
        if (widget != title):
            widget.destroy();

def save_settings(n):
    '''
    Enregistre la limite d'essai décider par le joueur à travers une variable globale.
    Args :
        n(int) --> Nombre d'essai que le joueur souhaite se donner.
    Return :
        None
    '''
    global hiding_word_txt;
    hiding_word_txt = fn.getHidingWord();
    fn.getTryLimit(n); #Send try limit to traitment functions.
    game_panel(hiding_word_txt, rl, wp, wl);

def update_word(word, hiding_word):
    '''
    Vérifie la comformité de la proposition du joueur.
    Actualise le mot caché en conséquence.
    Vérifie si le jeu est terminé ou non.
    Args :
        word(string)            --> proposition du joueur.
        hiding_word(string)     --> mot caché que le joueur doit trouver.
    '''
    global rl, wp, wl;
    #Check the lenght of the proposition.
    if(len(word) != len(hiding_word)):
        msgBox.showerror("Erreur de Saisie",f"Votre mot doit contenir {len(hiding_word)} lettres.");
        game_panel(hiding_word, rl, wp, wl);
    #Traitment of the proposition.
    else:
        infos_traitment = fn.traitment(word, hiding_word);
        hiding_word_txt = infos_traitment[0];
        rl = infos_traitment[1];
        wp = infos_traitment[2];
        wl = infos_traitment[3];
        #Is the part finish ?
        result = fn.doYouWin((hiding_word_txt));
        if (result[0] == None):
            game_panel(hiding_word_txt, rl, wp, wl);
        else:
            end_panel(result);

def new_game():
    '''
    Restart a part
    Args :
        None
    Return :
        None
    '''
    global hiding_word_txt;
    data = fn.reset_data();
    hiding_word_txt = data[0];
    rl = data[1];
    wp = data[2];
    wl = data[3];
    settings_panel();

#-------------------------------------Functions to manage panel---------------------------------#

def settings_panel():
    '''
    Affiche le panneau de paramètrage du jeu. Celui-ci permettant notamment de sélectionner
    sa limite d'essai.
    Args :
        None
    Return :
        None
    '''
    
    #Manage old Widgets:
    clear_windows();
    title.config(text="Settings Panel");

    #Widgets explicatifs:
    explication = tk.Label(root, text="""Bienvenue dans Motus Game ! 
                Le but est simple, un mot masqué s'affiche à l'écran. 
                C'est à vous de proposer divers mots afin de révéler petit à petit des lettres composant le mot masqué. """
                ,bg='#66B2FF', fg="white" ,font=("Arial",12));
    frSettings = tk.Frame(root, bg='#3399FF', bd=2, relief="solid");

    txtForTry = tk.Label(frSettings, text="Pour définir une limite d'essai, entrer un chiffre ci-dessous.\nSinon cliquer directement sur 'Commencer'."
                ,bg='#3399FF', fg="white" ,font=("Arial",12));

    #Widgets interactif:
    #ajouter au Word.
    try_scale = tk.Scale(frSettings, from_=0, to=10, orient=tk.HORIZONTAL, command=None)
    start = tk.Button(frSettings, text="Commencer", command=lambda : save_settings(try_scale.get()));
    stop = tk.Button(frSettings, text="Quitter", command=root.destroy);

    #Print Widgets:
    title.pack(pady=20);
    explication.pack(pady=50);
    frSettings.pack(pady=20);

    txtForTry.grid(column=0, row=0, pady=10, padx=25, sticky="w");
    try_scale.grid(column=0, row=1, pady=10, padx=25, sticky="ew");
    start.grid(column=1, row=0, padx=5);
    stop.grid(column=1, row=1, padx=5);

def game_panel(hiding_word, rl, wp, wl):
    '''
    Affichage du panneau de jeu. C'est ici que le jeu se déroule.
    Args :
        hiding_word(string)         --> le mot caché en cours de découverte.
        rl(list)                    --> contient les lettres révélées.
        wp(list)                    --> contient les lettres mal placées.
        wl(list)                    --> contient les mauvauses lettres.
    Return :
        None
    '''
    
    #Manage old Widgets:
    clear_windows();
    title.config(text="Game Panel");

    #Widgets explicatives:
    hiding_word_label = tk.Label(root, text=hiding_word,bg="blue", fg="white", font=("Arial", 20)
                           , width=40, height=5, bd=5, relief="ridge");
    
    #Manage Widgets Letters:
    frLetters = tk.Frame(root, bg="#66B2FF", bd=2, relief="solid");
    for i in range(26):
        letter = tk.Label(frLetters, text=chr(97 + i), bg="white", fg="black", font=("Arial",15),bd=1, relief="solid", padx=5, pady=3);
        #Changement de couleur si nécessaire :
        if letter["text"] in rl:
            letter.config(bg='green')
        elif letter["text"]  in wp:
            letter.config(bg='yellow')
        elif letter["text"]  in wl:
            letter.config(bg='red')

        #Positionnement des Widgets des lettres:
        if (i <= 9):
            letter.grid(row=0, column=i, padx=5);
        elif (i > 9 and i <= 19):
            letter.grid(row=1, column=i-10, padx=5);
        else :
            letter.grid(row=2, column=i-18, padx=5);

    frProp = tk.Frame(root, bg='#66B2FF');
    txt = tk.Label(frProp, text="Entrer votre proposition de mot :", bg="#66B2FF", fg="white");

    #Widget interactives :
    proposition = tk.Text(frProp, width=20 ,height=1);
    submit = tk.Button(frProp, text="Valider",command=lambda : update_word(proposition.get("1.0", tk.END).strip(), hiding_word));
    stop = tk.Button(frProp, text="Quitter",command=root.destroy);

    #Print Widgets.
    title.pack(pady=20);
    hiding_word_label.pack();
    frLetters.pack(pady=20);
    frProp.pack();

    txt.grid(column=0, row=0, pady=10, padx=25, sticky="w");
    proposition.grid(column=0, row=1, pady=10, padx=25, sticky="ew");
    submit.grid(column=1, row=1, padx=5);
    stop.grid(column=1, row=0, padx=5);

def end_panel(result):
    '''
    Affichage du panneau de fin. Annonce si le jeu est gagné ou s'il est perdu.
    Args :
        result(bool)            --> résultat de la partie.
    Return :
        None
    '''

    #Manage old Widgets:
    clear_windows();
    congratTxt = tk.Label(root, text=result[1], bg='white', width=100, height=10, bd=5, relief="groove");
    
    #Widgets explicatives:
    frButton = tk.Frame(root, bg='#66B2FF');

    #Widgets interactives:
    restart = tk.Button(frButton, text="Rejouer", command=new_game, width=8, height=2);
    stop = tk.Button(frButton, text="Quitter", command=root.destroy, width=8, height=2);

    #Print Widgets:
    title.pack(pady=20);
    congratTxt.pack();
    frButton.pack(pady=20);
    
    restart.grid(column=0, row=0, pady=5, padx=15);
    stop.grid(column=1, row=0, pady=5, padx=15);

#---------------------------Initialization Global Variables & Widgets--------------------------------#

root.title("Motus Game");
root.config(bg='#66B2FF', bd=5 , relief="solid");

title = tk.Label(root, text="Panel", height=3, width=50, bg="#3399FF" ,fg='white', font=("Arial",20)
                , bd= 5, relief="raised");
hiding_word_txt = fn.getHidingWord();
rl = [];
wp = [];
wl = [];

#Launch
settings_panel();
root.mainloop();