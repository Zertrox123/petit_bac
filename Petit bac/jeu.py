from tkinter import * 
from main import *
from partie import *

def menu_game():
    point = 0
    erreur = 0
    juste = 0
    fenetres = Tk()
    fenetres.geometry("3840x2140")
    fenetres.iconbitmap('Image/petit_bac.ico')
    fenetres.title("Petit bac")
    fenetres.minsize(100, 100)
    fenetres.config(background = "black")
    frame = Frame(fenetres, bg='black')

    #creer une sous-boite
    right_frame = Frame(frame, bg='black')

    #creer le texte
    label_titel = Label(right_frame, text = "Veuillez choisir votre mode de jeu ainsi que les joueurs:", font = ("Helvetica", 20), bg="black", fg='white')
    label_titel.pack()
    label_diff = Label(right_frame, text = "Facile | Normal | Difficile", font = ("Helvetica", 20), bg="black", fg='white')
    label_diff.pack()

    #creer les champs/inputs
    diff_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    diff_joueur.pack(pady=10, fill=X)
    label_mode = Label(right_frame, text = "Seul | Bot", font = ("Helvetica", 20), bg="black", fg='white')
    label_mode.pack()
    mode_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    mode_joueur.pack(pady=10, fill=X)
    error_text = Label(right_frame, text = "Je peux mettre ce que je veux on le verra pas", font = ("Helvetica", 20), bg="black", fg='black')
    error_text.pack(pady=2)

    def verif():
        diff = diff_joueur.get()
        mode = mode_joueur.get()
        if diff == "Facile":
            if mode == "Seul":
                point_bot = 0
                facile_seul(point_bot)
            elif mode == "Bot":
                facile_bot()
            else:
                error_text.config(fg = "red", text = "Vous devez utiliser un mode valide: 'Seul' | 'Bot' ")
        elif diff == "Normal":
            if mode == "Seul":
                normal_seul()
            elif mode == "Bot":
                normal_bot()
            else:
                error_text.config(fg = "red", text = "Vous devez utiliser un mode valide: 'Seul' | 'Bot' ")
        elif diff == "Difficile":
            if mode == "Seul":
                difficile_seul()
            elif mode == "Bot":
                difficile_bot()
            else:
                error_text.config(fg = "red", text = "Vous devez utiliser un mode valide: 'Seul' | 'Bot' ")
        else:
            error_text.config(fg = "red", text = "Vous devez utiliser une difficulté valide: 'Facile' | 'Normal' | 'Difficile' ")

    entrer_button = Button(right_frame, text= 'Entrer',font = ("Helvetica", 20), bg="white", command=verif)
    entrer_button.pack(pady=10)

    #sous boite a droite de la frame
    right_frame.grid(row=0, column=1, sticky=W)

    frame.pack(expand = YES)
    btn_quitter = Button(fenetres, text="MENU PRINCIPAL", bg="white", fg="black", command=fenetres.destroy)
    btn_quitter.pack(side=BOTTOM, fill=X)
    fenetres.mainloop()

def double_fonction(*funcs): # fonction permettant de faire 2 actions sur 1 bouton (impossible de base sur tkinter, et trouvé sur internet)
    def double_fonction(*fonct1, **fonct2):
        for f in funcs:
            f(*fonct1, **fonct2)
    return double_fonction
    

menu_game()