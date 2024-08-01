import tkinter as tk

root = tk.Tk();

def clear_windows():
    for widget in root.winfo_children():
        if (widget != title and widget != frame):
            widget.destroy();
    for widget in frame.winfo_children():
        widget.destroy();

def settings_panel():

    title.config(text="Settings Panel");

    explication = tk.Label(root, text="""Bienvenue dans Motus Game ! 
                    Le but est simple, un mot masqué s'affiche à l'écran. 
                    C'est à vous de proposer divers mots afin de révéler petit à petit des lettres composant le mot masqué. """
                    ,bg='lightblue' ,font=("Arial",12));

    txtForTry = tk.Label(frame, text="Pour définir une limite d'essai, entrer un chiffre ci-dessous.\nSinon cliquer directement sur 'Commencer'."
                ,bg='lightblue' ,font=("Arial",12));
    try_scale = tk.Scale(frame, from_=1, to=10, orient=tk.HORIZONTAL, command=None)

    #Buttons
    start = tk.Button(frame, text="Commencer", command=game_panel);
    stop = tk.Button(frame, text="Quitter", command=root.destroy);

    #Print Widget
    explication.pack(pady=10);
    txtForTry.grid(column=0, row=0, padx=200);
    try_scale.grid(column=0, row=1);
    start.grid(column=1, row=0);
    stop.grid(column=1, row=1);

def game_panel():
    
    #Manage old Widgets:
    clear_windows();
    title.config(text="Game Panel");

    #Create new Widgets:
    hiding_word = tk.Label(root, text="Marron",bg="blue", fg="white", font=("Arial", 20), width=40, height=5);
    frLetters = tk.Frame(root, bg="white");
    for i in range(26):
        letter = tk.Label(frLetters, text=chr(65 + i), bg="lightblue", fg="white", font=("Arial",12));
        if (i <= 9):
            letter.grid(row=0, column=i);
        elif (i > 9 and i <= 19):
            letter.grid(row=1, column=i-10);
        else :
            letter.grid(row=2, column=i-18);
    
    txt = tk.Label(frame, text="Entrer votre propostion de mot :");
    proposition = tk.Text(frame, width=20 ,height=1);
    stop = tk.Button(frame, text="Quitter",command=end_panel);

    #Print Widgets.
    hiding_word.pack();
    frLetters.pack(pady=20);
    txt.grid(column=0, row=0);
    proposition.grid(column=0, row=1, pady=5);
    stop.grid(column=1, row=0);

def end_panel():

    clear_windows();
    congratTxt = tk.Label(root, text="Ok");
    frButton = tk.Frame(root);
    restart = tk.Button(frame, text="Rejouer", command=None);
    stop = tk.Button(frame, text="Quitter", command=root.destroy);

    #Print Widgets:
    congratTxt.pack();
    frButton.pack();
    restart.grid(column=0, row=0);
    stop.grid(column=1, row=0);


root.title("Motus Game");
root.config(bg='lightblue');

#Global Widget:
title = tk.Label(root, text="Panel", height=3, width=50, bg="black" ,fg='white', font=("Arial",20));
frame = tk.Frame(root, bg='red', bd=50);
title.pack();
frame.pack();
settings_panel();

root.mainloop();

#1H30
#10h56