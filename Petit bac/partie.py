from tkinter import *
from time import *
from random import *

class Verification:
    def __init__(self, prenom, capital, pays, fruit, legume, animal):
        self.prenom = prenom
        self.capital = capital
        self.pays = pays
        self.fruit = fruit
        self.legume = legume
        self.animal = animal

    def verif_prenom(self):
        return True
    
    def verif_capital(self):
        capital = []
        for i in range(len(capital)):
            if capital[i] == self.capital:
                return True
        return False
    
    def verif_fruit(self):
        Fruit=["Abricot", "Airelle" ,"Amande" ,"Ananas" ,"Avocat" ,"Banane" ,"Cassis" ,"Cerise" ,"Châtaigne" ,"Citron" 
        ,"Clémentine" ,"Coing" ,"Datte" ,"Figue fraîche" ,"Fraise" ,"Fraise des bois" ,"Framboise" ,"Fruit de la passion" 
        ,"Grenade" ,"Groseille" ,"Groseille à maquereau" , "Kaki" , "Kiwi" ,"Kumquat" ,"Litchi" ,"Mandarine" ,"Mangue" 
        ,"Marron" ,"Melon" ,"Mirabelle" ,"Mûre" ,"Myrtille" ,"Nectarine" ,"Noisette" ,"Noix" ,"Orange" 
        ,"Orange sanguine" ,"Pamplemousse" ,"Papaye" ,"Pastèque" ,"Pêche" ,"Poire" ,"Pomme" ,"Prune" ,"Quetsche" 
        ,"Raisin" ,"Reine-claude" ,"Tomate" ,"Tomate charnue" ,"Tomate Peretti" ]
        for i in range(len(Fruit)):
            if Fruit[i] == self.fruit:
                return True
        return False
    
    def verif_legume(self):
        legume=["Ail" ,"Artichaut" , "Asperge" , "Asperge blanche" , "Asperge verte","Aubergine" ,"Blette", "Betterave" 
        , "Betterave rouge" , "Brocoli" , "Carotte" , "Catalonia" , "Céleri" , "Céleri branche" , "Céleri rave" 
        , "Chou blanc" , "Chou de Bruxelles" , "Chou frisé" , "Chou Romanesco" , "Chou rouge" , "Chou-chinois" 
        , "Chou-fleur", "Chou-rave" , "Cima di Rapa" , "Citrouille" , "Concombre" , "Courge" , "Courgette" , "Cresson" 
        , "Endive" , "Epinard" , "Fenouil" , "Haricot" , "Laitue" , "Laitue romaine" , "Mâche" , "Maïs", "Navet" 
        , "Oignon" , "Panais" , "Pâtisson" , "Oignon" , "Petit oignon blanc" , "Petit pois" , "Poireau", "Pois" 
        , "Pois mange-tout" , "Poivron" , "Pomme de terre" , "Potimarron" , "Potiron" , "Radis" , "Radis long" 
        , "Rhubarbe" , "Salsifis" , "Topinambour"]
        for i in range(len(legume)):
            if legume[i] == self.legume:
                return True
        return False
    
    def verif_pays(self):
        pays=["Afghanistan" ,"Afrique du Sud" , "Albanie" 
        , "Algérie" , "Allemagne" , "Andorre" ,"Angleterre", "Angola" 
        , "Anguilla" , "Antigua-et-Barbuda" , "Antilles" , "Néerlandaises" 
        , "Arabie Saoudite" , "Argentine" , "Arménie" , "Aruba" , "Australie" 
        , "Autriche" , "Azerbaïdjan" , "Bahamas" , "Bahreïn" , "Bangladesh" 
        , "Barbade" , "Belgique" , "Belize" , "Bénin" , "Bermudes" , "Bhoutan" 
        ,"Biélorussie" , "Birmanie" , "Myanmar" , "Bolivie" , "Bosnie-Herzégovine" 
        , "Botswana", "Brésil" , "Brunei" , "Bulgarie" , "Burkina Faso" , "Burundi" , "Cambodge" 
        , "Cameroun" , "Canada" , "Cap-vert" , "Chili" , "Chine" , "Chypre" , "Colombie" , "Comores" 
        , "Corée du Nord" , "Corée du Sud" , "Costa Rica" , "Côte d’Ivoire" , "Croatie" , "Cuba" , "Danemark" 
        , "Djibouti" , "Dominique" , "Égypte" , "Émirats Arabes Unis" , "Équateur" , "Érythrée" , "Espagne" 
        , "Estonie" , "États Fédérés de Micronésie" ,"États-Unis" , "Éthiopie" , "Fidji" , "Finlande" , "France" 
        , "Gabon" , "Gambie" , "Géorgie" , "Géorgie du Sud et les Îles Sandwich du Sud" , "Ghana" , "Gibraltar" 
        , "Grèce" , "Grenade" , "Groenland" , "Guadeloupe" , "Guam" , "Guatemala" , "Guinée" , "Guinée-Bissau" 
        , "Guinée Équatoriale" , "Guyana" , "Guyane Française" , "Haïti" , "Honduras" , "Hong-Kong" , "Hongrie" 
        , "Île Christmas" , "Île de Man" , "Île Norfolk" , "Îles Åland" , "Îles Caïmans" , "Îles Cocos" , "Keeling" 
        , "Îles Cook" , "Îles Féroé" , "Îles Malouines", "Îles Mariannes du Nord" , "Îles Marshall" 
        , "Îles Pitcairn" , "Îles Salomon" , "Îles Turks et Caïques" , "Îles Vierges Britanniques" 
        , "Îles Vierges des États-Unis" , "Inde" , "Indonésie" , "Iran" , "Iraq" , "Irlande" , "Islande" , "Israël" 
        , "Italie" , "Jamaïque" , "Japon" , "Jordanie" , "Kazakhstan" , "Kenya" , "Kirghizistan" , "Kiribati" 
        , "Koweït" , "Laos" , "Le Vatican" , "Lesotho" , "Lettonie" , "Liban" , "Libéria" , "Libye" , "Liechtenstein" 
        , "Lituanie" , "Luxembourg" , "Macao" , "Madagascar" , "Malaisie" , "Malawi" , "Maldives" , "Mali" , "Malte" 
        , "Maroc" , "Martinique" , "Maurice" , "Mauritanie" , "Mayotte" , "Mexique" , "Moldavie" , "Monaco" , "Mongolie" 
        , "Monténégro" , "Montserrat" , "Mozambique" , "Namibie" , "Nauru" , "Népal" , "Nicaragua" , "Niger" 
        , "Nigéria" , "Niué" , "Norvège" , "Nouvelle-Calédonie" , "Nouvelle-Zélande" , "Oman" , "Ouganda" 
        , "Ouzbékistan" , "Pakistan" , "Palaos" , "Panama" , "Papouasie-Nouvelle-Guinée" , "Paraguay" , "Pays-Bas" 
        , "Pérou" , "Philippines" , "Pologne" , "Polynésie Française" , "Porto Rico" , "Portugal" , "Qatar" 
        , "République Centrafricaine" , "République de Macédoine" , "République Démocratique du Congo" 
        , "République Dominicaine" , "République du Congo" , "République Tchèque" , "Réunion" , "Roumanie" 
        , "Royaume-Uni" , "Russie" , "Rwanda" , "Saint-Kitts-et-Nevis" , "Saint-Marin" , "Saint-Pierre-et-Miquelon" 
        , "Saint-Vincent-et-les Grenadines" , "Sainte-Hélène" , "Sainte-Lucie" , "Salvador" , "Samoa" 
        , "Samoa Américaines" , "Sao Tomé-et-Principe" , "Sénégal" , "Serbie" , "Seychelles" , "Sierra Leone" 
        , "Singapour" , "Slovaquie" , "Slovénie" , "Somalie" , "Soudan" , "Sri Lanka" , "Suède" , "Suisse" 
        , "Suriname" , "Svalbard et Jan" , "Mayen" , "Swaziland" , "Syrie" , "Tadjikistan" , "Taïwan" , "Tanzanie" 
        , "Tchad" , "Terres Australes Françaises" , "Thaïlande" , "Timor Oriental" , "Togo" , "Tonga" 
        , "Trinité-et-Tobago" , "Tunisie" , "Turkménistan" , "Turquie" , "Tuvalu" , "Ukraine" , "Uruguay" 
        , "Vanuatu" , "Venezuela" , "Vietnam" , "Wallis et Futuna" , "Yémen" , "Zambie" , "Zimbabwe"]
        for i in range(len(pays)):
            if pays[i] == self.pays:
                return True
        return False
    
    def verif_animal(self):
        animal=["Chien" , "Chat" , "Lapin" , "Souris" , "Hamster" , "Cochon d’inde" , "Aigle" , "Vautour" , "Chouette" 
        , "Hibou" , "Ecureuil" , "Hérisson" , "Poisson" , "Calamar" , "Pieuvre" , "Requin" , "Taureau" , "Vache" , "Moineau" 
        , "Cochon" , "Grue" , "Cigogne" , "Baleine" , "Poule" , "Coq" , "Mouton" , "Chèvre" , "Loup" , "Renard" 
        , "Singe" , "Paresseux" , "Koala" , "Kangourou" , "Diable de Tasmanie" , "Coyote" , "Autruche" 
        , "Chauve-souris" , "Rat" , "Dauphin" , "Perruche" , "Perroquet" , "Paons" , "Faisan" , "Oie" , "Cygne" 
        , "Canard" , "Serpen" , "Lézard" , "Tortue" , "Crocodile" , "Alligator" , "Furet" , "Cheval" , "Girafe" 
        , "Zèbre" , "Lion" , "Hyène" , "Buffle" , "Cerf" , "Faon" , "Chevreuil" , "Ours" , "Corbeau" , "Panda" 
        , "Tigre" , "Lémurien" , "Pingouin" , "Manchot" , "Léopard" , "Puma" , "Sanglier" , "Eléphant" , "Rhinocéros" 
        , "Narval" , "Orque" , "Cachalot" , "Wapiti" , "Capybara" , "Morse" , "Tatou" , "Pangolin" , "Fouine" , "Elan" 
        , "Renne" , "Raton laveur" , "Castor" , "Phoque" , "Lama" , "Tamanoir" , "Fourmilier"]
        for i in range(len(animal)):
            if animal[i] == self.animal:
                return True
        return False

def facile_seul(point_bot):
    def loading(point, point_bot):
        def menu():
            fenetre2 = Tk()
            fenetre2.title("Menu partie")
            fenetre2.geometry("3840x2160")
            fenetre2.config(background = "black")

            frame = Frame(fenetre2, background="black")

            #creer une sous-boite
            right_frame = Frame(frame, bg='black')

            #creer le petit bac
            label_prenom = Label(right_frame, text = "Résultat partie: (1 reponse = 1p | 1 mauvaise réponse = -1p)", font = ("Helvetica", 20), bg="black", fg='white')
            label_prenom.pack()
            label_pays = Label(right_frame, text = "Joueur:", font = ("Helvetica", 20), bg="black", fg='white')
            label_pays.pack()
            label_fruits = Label(right_frame, text = f"{point} points", font = ("Helvetica", 20), bg="black", fg='white')
            label_fruits.pack()
            label_legume = Label(right_frame, text = "Bot: (si sélectionner)", font = ("Helvetica", 20), bg="black", fg='white')
            label_legume.pack()
            label_animal = Label(right_frame, text = f"{point_bot} points", font = ("Helvetica", 20), bg="black", fg='white')
            label_animal.pack()

                                    
            #creation bouton "entrer"
            entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=double_fonction(fenetre2.destroy,facile_seul))
            entrer_button.pack(pady=10)

            #sous boite a droite de la frame
            right_frame.grid(row=0, column=1, sticky=W)

            frame.pack(expand=YES)

            #afficher la fenetre + le bouton quitter
            frame.pack(expand = YES)
            btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
            btn_quitter.pack(side=BOTTOM, fill=X)
            fenetre2.mainloop()
        fenetre2 = Tk()
        fenetre2.title("Menu partie")
        fenetre2.geometry("3840x2160")
        fenetre2.config(background = "black")

        frame = Frame(fenetre2, background="black")

        #creer une sous-boite
        right_frame = Frame(frame, bg='black')

        #creer le petit bac
        label_prenom = Label(right_frame, text = "Vérification des points en cours...", font = ("Helvetica", 20), bg="black", fg='white')
        label_prenom.pack()

                                
        #creation bouton "entrer"
        entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=double_fonction(fenetre2.destroy,menu))
        entrer_button.pack(pady=10)

        #sous boite a droite de la frame
        right_frame.grid(row=0, column=1, sticky=W)

        frame.pack(expand=YES)

        #afficher la fenetre + le bouton quitter
        frame.pack(expand = YES)
        btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
        btn_quitter.pack(side=BOTTOM, fill=X)
        fenetre2.mainloop()
    lettre = ["A", "B", "C", "D", "E", "F", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lettre = choice(lettre)
    fenetre2 = Tk()
    fenetre2.title("Partie démarée")
    fenetre2.geometry("3840x2160")
    fenetre2.config(background = "black")

    frame = Frame(fenetre2, background="black")

    #creer une sous-boite
    right_frame = Frame(frame, bg='black')

    #creer le petit bac
    label_prenom = Label(right_frame, text = f"Lettre choisis: {lettre}", font = ("Helvetica", 20), bg="black", fg='white')
    label_prenom.pack()
    label_prenom = Label(right_frame, text = "Prénom", font = ("Helvetica", 20), bg="black", fg='white')
    label_prenom.pack()
    prenom_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    prenom_joueur.pack(pady=10, fill=X)
    label_pays = Label(right_frame, text = "Pays:", font = ("Helvetica", 20), bg="black", fg='white')
    label_pays.pack()
    pays_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    pays_joueur.pack(pady=10, fill=X)
    label_fruits = Label(right_frame, text = "Fruits:", font = ("Helvetica", 20), bg="black", fg='white')
    label_fruits.pack()
    fruit_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    fruit_joueur.pack(pady=10, fill=X)
    label_legume = Label(right_frame, text = "Légumes:", font = ("Helvetica", 20), bg="black", fg='white')
    label_legume.pack()
    legume_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    legume_joueur.pack(pady=10, fill=X)
    label_animal = Label(right_frame, text = "Animal:", font = ("Helvetica", 20), bg="black", fg='white')
    label_animal.pack()
    animal_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    animal_joueur.pack(pady=10, fill=X)

    def verif():
        point = 0
        prenom = prenom_joueur.get()
        capital = 1
        pays = pays_joueur.get()
        fruit = fruit_joueur.get()
        legume = legume_joueur.get()
        animal = animal_joueur.get()
        verification = Verification(prenom, capital, pays, fruit , legume,animal)
        prenomm = verification.verif_prenom()
        payss = verification.verif_pays()
        fruitt = verification.verif_fruit()
        legumee = verification.verif_legume()
        animall = verification.verif_animal()
        if prenomm == True and prenom[:1] == lettre:
            point += 1
        if payss == True and pays[:1] == lettre:
            point += 1
        if fruitt == True and fruit[:1] == lettre:
            point += 1
        if legumee == True and legume[:1] == lettre:
            point += 1
        if animall == True and animal[:1] == lettre:
            point += 1
        print(point)
        loading(point, point_bot)

    #creation bouton "entrer"
    entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=verif)
    entrer_button.pack(pady=10)

    #sous boite a droite de la frame
    right_frame.grid(row=0, column=1, sticky=W)

    frame.pack(expand=YES)

    #afficher la fenetre + le bouton quitter
    frame.pack(expand = YES)
    btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
    btn_quitter.pack(side=BOTTOM, fill=X)
    fenetre2.mainloop()


def facile_bot():
    point_bot = randint(0,3)
    facile_seul(point_bot)


def normal_seul():
    def loading(point, point_bot):
        def menu():
            fenetre2 = Tk()
            fenetre2.title("Menu partie")
            fenetre2.geometry("3840x2160")
            fenetre2.config(background = "black")

            frame = Frame(fenetre2, background="black")

            #creer une sous-boite
            right_frame = Frame(frame, bg='black')

            #creer le petit bac
            label_prenom = Label(right_frame, text = "Résultat partie: (1 reponse = 1p | 1 mauvaise réponse = -1p)", font = ("Helvetica", 20), bg="black", fg='white')
            label_prenom.pack()
            label_pays = Label(right_frame, text = "Joueur:", font = ("Helvetica", 20), bg="black", fg='white')
            label_pays.pack()
            label_fruits = Label(right_frame, text = f"{point} points", font = ("Helvetica", 20), bg="black", fg='white')
            label_fruits.pack()
            label_legume = Label(right_frame, text = "Bot: (si sélectionner)", font = ("Helvetica", 20), bg="black", fg='white')
            label_legume.pack()
            label_animal = Label(right_frame, text = f"{point_bot} points", font = ("Helvetica", 20), bg="black", fg='white')
            label_animal.pack()

                                    
            #creation bouton "entrer"
            entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=double_fonction(fenetre2.destroy,facile_seul))
            entrer_button.pack(pady=10)

            #sous boite a droite de la frame
            right_frame.grid(row=0, column=1, sticky=W)

            frame.pack(expand=YES)

            #afficher la fenetre + le bouton quitter
            frame.pack(expand = YES)
            btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
            btn_quitter.pack(side=BOTTOM, fill=X)
            fenetre2.mainloop()
        fenetre2 = Tk()
        fenetre2.title("Menu partie")
        fenetre2.geometry("3840x2160")
        fenetre2.config(background = "black")

        frame = Frame(fenetre2, background="black")

        #creer une sous-boite
        right_frame = Frame(frame, bg='black')

        #creer le petit bac
        label_prenom = Label(right_frame, text = "Vérification des points en cours...", font = ("Helvetica", 20), bg="black", fg='white')
        label_prenom.pack()

                                
        #creation bouton "entrer"
        entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=double_fonction(fenetre2.destroy,menu))
        entrer_button.pack(pady=10)

        #sous boite a droite de la frame
        right_frame.grid(row=0, column=1, sticky=W)

        frame.pack(expand=YES)

        #afficher la fenetre + le bouton quitter
        frame.pack(expand = YES)
        btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
        btn_quitter.pack(side=BOTTOM, fill=X)
        fenetre2.mainloop()
    lettre = ["A", "B", "C", "D", "E", "F", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lettre = choice(lettre)
    fenetre2 = Tk()
    fenetre2.title("Partie démarée")
    fenetre2.geometry("3840x2160")
    fenetre2.config(background = "black")

    frame = Frame(fenetre2, background="black")

    #creer une sous-boite
    right_frame = Frame(frame, bg='black')

    #creer le petit bac
    label_prenom = Label(right_frame, text = f"Lettre choisis: {lettre}", font = ("Helvetica", 20), bg="black", fg='white')
    label_prenom.pack()
    label_prenom = Label(right_frame, text = "Capital", font = ("Helvetica", 20), bg="black", fg='white')
    label_prenom.pack()
    prenom_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    prenom_joueur.pack(pady=10, fill=X)
    label_pays = Label(right_frame, text = "Pays:", font = ("Helvetica", 20), bg="black", fg='white')
    label_pays.pack()
    pays_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    pays_joueur.pack(pady=10, fill=X)
    label_fruits = Label(right_frame, text = "Fruits:", font = ("Helvetica", 20), bg="black", fg='white')
    label_fruits.pack()
    fruit_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    fruit_joueur.pack(pady=10, fill=X)
    label_legume = Label(right_frame, text = "Légumes:", font = ("Helvetica", 20), bg="black", fg='white')
    label_legume.pack()
    legume_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    legume_joueur.pack(pady=10, fill=X)
    label_animal = Label(right_frame, text = "Animal:", font = ("Helvetica", 20), bg="black", fg='white')
    label_animal.pack()
    animal_joueur = Entry(right_frame,font = ("Helvetica", 20), bg="black", fg='white')
    animal_joueur.pack(pady=10, fill=X)

    def verif():
        point = 0
        prenom = prenom_joueur.get()
        capital = 1
        pays = pays_joueur.get()
        fruit = fruit_joueur.get()
        legume = legume_joueur.get()
        animal = animal_joueur.get()
        verification = Verification(prenom, capital, pays, fruit , legume,animal)
        prenomm = verification.verif_prenom()
        payss = verification.verif_pays()
        fruitt = verification.verif_fruit()
        legumee = verification.verif_legume()
        animall = verification.verif_animal()
        if prenomm == True and prenom[:1] == lettre:
            point += 1
        if payss == True and pays[:1] == lettre:
            point += 1
        if fruitt == True and fruit[:1] == lettre:
            point += 1
        if legumee == True and legume[:1] == lettre:
            point += 1
        if animall == True and animal[:1] == lettre:
            point += 1
        print(point)
        loading(point, point_bot)

    #creation bouton "entrer"
    entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=verif)
    entrer_button.pack(pady=10)

    #sous boite a droite de la frame
    right_frame.grid(row=0, column=1, sticky=W)

    frame.pack(expand=YES)

    #afficher la fenetre + le bouton quitter
    frame.pack(expand = YES)
    btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
    btn_quitter.pack(side=BOTTOM, fill=X)
    fenetre2.mainloop()

def normal_bot():
    print("ok")

def difficile_seul():
    print("ok")

def difficile_bot():
    print("ok")

    
def double_fonction(*funcs): # fonction permettant de faire 2 actions sur 1 bouton (impossible de base sur tkinter, et trouvé sur internet)
    def double_fonction(*fonct1, **fonct2):
        for f in funcs:
            f(*fonct1, **fonct2)
    return double_fonction


def menuu():
    fenetre2 = Tk()
    fenetre2.title("Menu partie")
    fenetre2.geometry("3840x2160")
    fenetre2.config(background = "black")

    frame = Frame(fenetre2, background="black")

    #creer une sous-boite
    right_frame = Frame(frame, bg='black')

    #creer le petit bac
    label_prenom = Label(right_frame, text = "Résultat partie: (1 reponse = 1p | 1 mauvaise réponse = -1p)", font = ("Helvetica", 20), bg="black", fg='white')
    label_prenom.pack()
    label_pays = Label(right_frame, text = "Joueur:", font = ("Helvetica", 20), bg="black", fg='white')
    label_pays.pack()
    label_fruits = Label(right_frame, text = "{} points", font = ("Helvetica", 20), bg="black", fg='white')
    label_fruits.pack()
    label_legume = Label(right_frame, text = "Bot: (si sélectionner)", font = ("Helvetica", 20), bg="black", fg='white')
    label_legume.pack()
    label_animal = Label(right_frame, text = "{} points", font = ("Helvetica", 20), bg="black", fg='white')
    label_animal.pack()

                            
    #creation bouton "entrer"
    entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=double_fonction(fenetre2.destroy,facile_seul))
    entrer_button.pack(pady=10)

    #sous boite a droite de la frame
    right_frame.grid(row=0, column=1, sticky=W)

    frame.pack(expand=YES)

    #afficher la fenetre + le bouton quitter
    frame.pack(expand = YES)
    btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
    btn_quitter.pack(side=BOTTOM, fill=X)
    fenetre2.mainloop()

def loadiing(point):
    fenetre2 = Tk()
    fenetre2.title("Menu partie")
    fenetre2.geometry("3840x2160")
    fenetre2.config(background = "black")

    frame = Frame(fenetre2, background="black")

    #creer une sous-boite
    right_frame = Frame(frame, bg='black')

    #creer le petit bac
    label_prenom = Label(right_frame, text = "Vérification des points en cours...", font = ("Helvetica", 20), bg="black", fg='white')
    label_prenom.pack()

                            
    #creation bouton "entrer"
    entrer_button = Button(right_frame, text= 'Valider',font = ("Helvetica", 20), bg="white", command=double_fonction(fenetre2.destroy,facile_seul))
    entrer_button.pack(pady=10)

    #sous boite a droite de la frame
    right_frame.grid(row=0, column=1, sticky=W)

    frame.pack(expand=YES)

    #afficher la fenetre + le bouton quitter
    frame.pack(expand = YES)
    btn_quitter = Button(fenetre2, text="MENU PRINCIPAL", bg="white", fg="black", command=double_fonction(fenetre2.destroy, facile_seul))
    btn_quitter.pack(side=BOTTOM, fill=X)
    fenetre2.mainloop()

