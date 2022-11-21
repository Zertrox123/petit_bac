from tkinter import *
from time import *
from jeu import *

def menu_principal():
    fenetre = Tk()
    fenetre.geometry("3840x2160")
    fenetre.iconbitmap('Image/petit_bac.ico')
    fenetre.title("Petit bac")
    fenetre.minsize(480, 360)
    fenetre.config(background = "black")

    frame = Frame(fenetre, bg='black')

    #creation du sous-titre
    soustitre = Label(frame, text= "Seriez-vous à la hauteur?", bg = "black", fg = "white",font= ("Helvetica",70))
    soustitre.pack(fill='both', side='left', expand='True')

    frame.pack()

    frame2 = Frame(fenetre, bg='black')

    #creation des boutons
    image_nouveau_button =PhotoImage(file='Image/buttons/button-newgame-s1-en-1.png').subsample(3)
    image_nouveau_button = image_nouveau_button.zoom(2)
    nouveau_button = Button(frame2, text = "Commencer", image=image_nouveau_button, command = double_fonction(fenetre.destroy, menu_newgame), highlightthickness = 0, bd = 0, bg= 'black')
    nouveau_button.pack(padx = 20, pady = 20)
    image_charger_button =PhotoImage(file='Image/charger.png').subsample(3)
    image_charger_button = image_charger_button.zoom(2)
    charger_button = Button(frame2, text = "Charger", image= image_charger_button, command= double_fonction(fenetre.destroy, menu_charger), highlightthickness = 0, bd = 0, bg= 'black')
    charger_button.pack(pady=2)
    
    frame2.pack()

    #creation bouton quitter
    btn_quitter = Button(fenetre, text="QUITTER", bg="white", fg="black", command=fenetre.destroy)
    btn_quitter.pack(side= BOTTOM, fill=X)

    fenetre.mainloop()

def double_fonction(*funcs): # fonction permettant de faire 2 actions sur 1 bouton (impossible de base sur tkinter, et trouvé sur internet)
    def double_fonction(*fonct1, **fonct2):
        for f in funcs:
            f(*fonct1, **fonct2)
    return double_fonction

def menu_newgame():
    fenetre2 = Tk()
    fenetre2.title("Nouveau")
    fenetre2.geometry("3840x2160")
    fenetre2.config(background = "black")

    frame = Frame(fenetre2, background="black")

    #creation d'image
    height = 700
    width = 700
    image = PhotoImage(file="Image/new_user.png", master= fenetre2).zoom(1).subsample(2)
    canvas = Canvas(frame, width=width, height=height, bg="black", bd=0, highlightthickness=0 )
    canvas.create_image(width/2, height/2, image= image)
    canvas.grid(row =0, column=0, sticky=W)

    #creer une sous-boite
    right_frame = Frame(frame, bg='black')

    #creer le texte
    label_titel = Label(right_frame, text = "Veuillez creer un compte pour jouer:", font = ("Helvetica", 20), bg="black", fg='white')
    label_titel.pack()
    label_pseudo = Label(right_frame, text = "Pseudo original:", font = ("Helvetica", 20), bg="black", fg='white')
    label_pseudo.pack()

    #creer les champs/inputs
    pseudo_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    pseudo_joueur.pack(pady=10, fill=X)
    label_mdp = Label(right_frame, text = "Mot de Passe (min 5 caractères):", font = ("Helvetica", 20), bg="black", fg='white')
    label_mdp.pack()
    mdp_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    mdp_joueur.pack(pady=10, fill=X)
    error_text = Label(right_frame, text = "Je peux mettre ce que je veux on le verra pas", font = ("Helvetica", 20), bg="black", fg='black')
    error_text.pack(pady=2)
                            
    #creation bouton "entrer"
    entrer_button = Button(right_frame, text= 'Entrer',font = ("Helvetica", 20), bg="white", command=double_fonction(fenetre2.destroy, menu_game))
    entrer_button.pack(pady=10)

    #sous boite a droite de la frame
    right_frame.grid(row=0, column=1, sticky=W)

    frame.pack(expand=YES)

    #afficher la fenetre + le bouton quitter
    frame.pack(expand = YES)
    btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, menu_principal))
    btn_quitter.pack(side=BOTTOM, fill=X)
    fenetre2.mainloop()


def menu_charger():
    fenetre1 = Tk()
    fenetre1.title("Nouveau")
    fenetre1.geometry("3840x2160")
    fenetre1.config(background = "black")

    frame = Frame(fenetre1, background="black")

    #creation d'image
    height = 700
    width = 700
    image = PhotoImage(file="Image/new_user.png", master= fenetre1).zoom(1).subsample(2)
    canvas = Canvas(frame, width=width, height=height, bg="black", bd=0, highlightthickness=0 )
    canvas.create_image(width/2, height/2, image= image)
    canvas.grid(row =0, column=0, sticky=W)

    #creer une sous-boite
    right_frame = Frame(frame, bg='black')

    #creer le texte
    label_titel = Label(right_frame, text = "Veuillez creer un compte pour jouer:", font = ("Helvetica", 20), bg="black", fg='white')
    label_titel.pack()
    label_pseudo = Label(right_frame, text = "Pseudo original:", font = ("Helvetica", 20), bg="black", fg='white')
    label_pseudo.pack()

    btn_quitter = Button(fenetre1, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre1.destroy, menu_principal))
    btn_quitter.pack(side=BOTTOM, fill=X)
    fenetre1.mainloop()


menu_principal()