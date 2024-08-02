import tkinter as tk

root = tk.Tk();

def clear_windows():
    '''
    
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
                ,bg='lightblue' ,font=("Arial",12));
    frSettings = tk.Frame(root, bg='red');

    txtForTry = tk.Label(frSettings, text="Pour définir une limite d'essai, entrer un chiffre ci-dessous.\nSinon cliquer directement sur 'Commencer'."
                ,bg='lightblue' ,font=("Arial",12));
    try_scale = tk.Scale(frSettings, from_=1, to=10, orient=tk.HORIZONTAL, command=None)

    #Buttons
    start = tk.Button(frSettings, text="Commencer", command=game_panel);
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
    frLetters = tk.Frame(root, bg="lightblue");
    for i in range(26):
        letter = tk.Label(frLetters, text=chr(65 + i), bg="lightblue", fg="white", font=("Arial",15)
        ,bd=1, relief="solid", padx=5);
        if (i <= 9):
            letter.grid(row=0, column=i, padx=5);
        elif (i > 9 and i <= 19):
            letter.grid(row=1, column=i-10, padx=5);
        else :
            letter.grid(row=2, column=i-18, padx=5);
    frProp = tk.Frame(root, bg='red');
    
    txt = tk.Label(frProp, text="Entrer votre propostion de mot :");
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
    congratTxt = tk.Label(root, text="Ok");
    frButton = tk.Frame(root, bg='red');
    restart = tk.Button(frButton, text="Rejouer", command=settings_panel);
    stop = tk.Button(frButton, text="Quitter", command=root.destroy);

    #Print Widgets:
    title.pack(pady=20);
    congratTxt.pack();
    frButton.pack();
    
    restart.grid(column=0, row=0);
    stop.grid(column=1, row=0);


root.title("Motus Game");
root.config(bg='lightblue', bd=5 , relief="solid");

#Global Widget:
title = tk.Label(root, text="Panel", height=3, width=50, bg="#3399FF" ,fg='white', font=("Arial",20)
                , bd= 5, relief="raised");

settings_panel();

root.mainloop();

#2H 
#10h20