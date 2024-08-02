import tkinter as tk
import functions as fn

root = tk.Tk();

def clear_windows():
    '''
    Détruit tous les widgets de l'interface à l'exception du widget contenant le titre.
    '''
    for widget in root.winfo_children():
        if (widget != title):
            widget.destroy();

def settings_panel():

    clear_windows();
    title.config(text="Settings Panel");

    explication = tk.Label(root, text="""Bienvenue dans Motus Game ! 
                Le but est simple, un mot masqué s'affiche à l'écran. 
                C'est à vous de proposer divers mots afin de révéler petit à petit des lettres composant le mot masqué. """
                ,bg='#66B2FF', fg="white" ,font=("Arial",12));
    frSettings = tk.Frame(root, bg='#3399FF', bd=2, relief="solid");

    txtForTry = tk.Label(frSettings, text="Pour définir une limite d'essai, entrer un chiffre ci-dessous.\nSinon cliquer directement sur 'Commencer'."
                ,bg='#3399FF', fg="white" ,font=("Arial",12));
    try_scale = tk.Scale(frSettings, from_=0, to=10, orient=tk.HORIZONTAL, command=None)

    #Buttons
    #ajouter au Word.
    start = tk.Button(frSettings, text="Commencer", command=lambda: (fn.start(try_scale.get()), game_panel));
    stop = tk.Button(frSettings, text="Quitter", command=root.destroy);

    #Print Widgets:
    title.pack(pady=20);
    explication.pack(pady=50);
    frSettings.pack(pady=20);

    txtForTry.grid(column=0, row=0, pady=10, padx=25, sticky="w");
    try_scale.grid(column=0, row=1, pady=10, padx=25, sticky="ew");
    start.grid(column=1, row=0, padx=5);
    stop.grid(column=1, row=1, padx=5);

def game_panel():
    
    #Manage old Widgets:
    clear_windows();
    title.config(text="Game Panel");

    #Create new Widgets:
    hiding_word = tk.Label(root, text="Marron",bg="blue", fg="white", font=("Arial", 20)
                           , width=40, height=5, bd=5, relief="ridge");
    frLetters = tk.Frame(root, bg="#66B2FF", bd=2, relief="solid");
    for i in range(26):
        letter = tk.Label(frLetters, text=chr(65 + i), bg="white", fg="black", font=("Arial",15)
        ,bd=1, relief="solid", padx=5, pady=3);
        if (i <= 9):
            letter.grid(row=0, column=i, padx=5);
        elif (i > 9 and i <= 19):
            letter.grid(row=1, column=i-10, padx=5);
        else :
            letter.grid(row=2, column=i-18, padx=5);
    frProp = tk.Frame(root, bg='#66B2FF');
    
    txt = tk.Label(frProp, text="Entrer votre proposition de mot :", bg="#66B2FF", fg="white");
    proposition = tk.Text(frProp, width=20 ,height=1);
    stop = tk.Button(frProp, text="Quitter",command=end_panel);

    #Print Widgets.
    title.pack(pady=20);
    hiding_word.pack();
    frLetters.pack(pady=20);
    frProp.pack();

    txt.grid(column=0, row=0, pady=10, padx=25, sticky="w");
    proposition.grid(column=0, row=1, pady=10, padx=25, sticky="ew");
    stop.grid(column=1, row=1, padx=5);

def end_panel():

    clear_windows();
    congratTxt = tk.Label(root, text="Ok", bg='white', width=100, height=10, bd=5, relief="groove");
    frButton = tk.Frame(root, bg='#66B2FF');
    restart = tk.Button(frButton, text="Rejouer", command=settings_panel, width=8, height=2);
    stop = tk.Button(frButton, text="Quitter", command=root.destroy, width=8, height=2);

    #Print Widgets:
    title.pack(pady=20);
    congratTxt.pack();
    frButton.pack(pady=20);
    
    restart.grid(column=0, row=0, pady=5, padx=15);
    stop.grid(column=1, row=0, pady=5, padx=15);


root.title("Motus Game");
root.config(bg='#66B2FF', bd=5 , relief="solid");

#Global Widget:
title = tk.Label(root, text="Panel", height=3, width=50, bg="#3399FF" ,fg='white', font=("Arial",20)
                , bd= 5, relief="raised");

settings_panel();

root.mainloop();

#2H30 pour tkinter
#20 pour fusion
#11h30