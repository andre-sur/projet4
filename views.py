import tkinter as tk
from tkinter import ttk
from datetime import datetime,date,time,timedelta

from tkinter import messagebox

#VUES TKINTER MODELE PARAMETRABLE

def choice_elements(elements):
    def fermer():
        fenetre.destroy() 
                  
    # Liste des éléments
    #elements = ["Élément 1", "Élément 2", "Élément 3", "Élément 4", "Élément 5"]

    # Créer la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Sélection d'éléments")

    # Créer une liste pour les variables de chaque case à cocher
    var = []

    # Créer une case à cocher pour chaque élément de la liste
    listbox = []
    for element in elements:
        var_element = tk.IntVar()  # Variable pour savoir si la case est cochée (1) ou non (0)
        var.append(var_element)
        checkbox = tk.Checkbutton(fenetre, text=element, variable=var_element)
        checkbox.pack(anchor="w")  # Ajouter la case à cocher à la fenêtre
        listbox.append(element)  # Ajouter l'élément à la liste des éléments

    # Bouton pour enregistrer les sélections
    button_enregistrer = tk.Button(fenetre, text="Enregistrer", command=fermer)
    button_enregistrer.pack()
    
    # Lancer la boucle principale de la fenêtre
    fenetre.mainloop()
    return([listbox[i] for i in range(len(listbox)) if var[i].get() == 1])
    

def choice_three_options (list_of_choice) :
    liste_retour=[0]*10
    def enregistrer_resultats():
    # Fonction pour afficher les résultats dans la console
        for i, var in enumerate(scores):
            print(f"Choix {i+1}: {var.get()}")
            if var.get()==1:
                liste_retour[i*2]=1
            if var.get()==2:
                liste_retour[i*2+1]=1
            if var.get()==3:
                liste_retour[i*2]=0.5
                liste_retour[i*2+1]=0.5
                 
            print(liste_retour)
        #return(liste_retour)
        root.destroy()
        return(liste_retour)
        
        

    root = tk.Tk()
    root.title("Choix entre trois options")
    root.geometry("700x700")

    # Variable liée aux boutons radio
    var = tk.StringVar()
    var.set(2)
    # Création des trois boutons radio
    scores=[]
    fin_boucle=int(len(list_of_choice)/2)
    for choice in range(0,fin_boucle+2,2):
        frame = tk.Frame(root)
        frame.pack(pady=10, anchor="w") 
        label = tk.Label(frame, text=list_of_choice[choice]+ " vs "+list_of_choice[choice+1], font=("Arial", 12))
        label.pack(side=tk.TOP, anchor="w")
        var = tk.IntVar()
        radio1 = tk.Radiobutton(frame, text=list_of_choice[choice], variable=var, value=1)
        radio2 = tk.Radiobutton(frame, text=list_of_choice[choice+1], variable=var, value=2)
        radio3 = tk.Radiobutton(frame, text="match nul", variable=var, value=3)
        
        radio1.pack(side=tk.LEFT, padx=10)
        radio2.pack(side=tk.LEFT, padx=10)
        radio3.pack(side=tk.LEFT, padx=10)

        scores.append(var)

        # Placement du bouton dans la fenêtre (ici centré)
      #  for i in range(0,len(list_of_choice)):
       #     buttons[i].pack(pady=5)
    

    enregistrer_btn = tk.Button(root, text="Enregistrer les résultats", command=enregistrer_resultats)
    enregistrer_btn.pack(pady=10)

# Lancer la boucle principale de l'interface graphique
    root.mainloop()
    return(liste_retour)

def choice_yesno (titre,message):
    response = messagebox.askyesno(titre,message)
    return(response)

def about_tournament(tournament_data):
        choix = scroll_menu("Choisir un tournoi",options)  # Récupère la sélection actuelle du menu déroulant
        print("choisi "+choix)
        i=options.index(choix)
        date_start=format_date(tournament_data[i].start)
        date_end=format_date(tournament_data[i].end)
        location=tournament_data[i].location
        text=(f"Vous avez sélectionné : {choix} \n Lieu : {location} \n date début {date_start} \n date fin {date_end}")
        show_text("Détails à propos d'un tournoi",text)

def scroll_menu(titre,options):
    def exit():
        root.quit()
        return(variable.get())
        
        
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title(titre)  # Titre de la fenêtre
    root.geometry("400x200")  # Dimensions de la fenêtre

    # Liste d'options pour le menu déroulant
    

    # Variable pour stocker la sélection de l'utilisateur
    variable = tk.StringVar(root)
    variable.set(options[0])  # Définir l'option par défaut (ici la première option)

    # Création du widget OptionMenu avec la liste d'options
    option_menu = tk.OptionMenu(root, variable, *options)
    option_menu.pack(pady=20)

    # Bouton pour afficher la sélection
    button = tk.Button(root, text="Valider", font=("Arial", 12), command=exit)
    button.pack(pady=10)

    # Lancer la boucle principale de l'application
    root.mainloop()
    return(variable.get())

class FormulaireSaisie:
    def __init__(self, elements):
        # Liste des éléments pour le formulaire (par exemple, ['Nom', 'Âge', 'Ville', 'Email'])
        self.elements = elements
        self.valeurs_saisies = []  # Variable d'instance pour stocker les valeurs saisies
        self.entries = []  # Liste pour stocker les widgets d'entrées (Entry)
        
        # Créer la fenêtre tkinter
        self.root = tk.Tk()
        self.root.title("Formulaire de saisie")
        
        # Créer les champs de saisie pour chaque élément de la liste
        for idx, element in enumerate(self.elements):
            # Créer un label pour chaque élément
            label = tk.Label(self.root, text=element)
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
            
            # Créer un champ de saisie (Entry) pour chaque élément
            entry = tk.Entry(self.root)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            
            # Ajouter l'entrée à la liste des entrées
            self.entries.append(entry)

        # Ajouter un bouton pour enregistrer les données
        enregistrer_button = tk.Button(self.root, text="Enregistrer", command=self.enregistrer)
        enregistrer_button.grid(row=len(self.elements), column=0, columnspan=2, pady=10)

    def enregistrer(self):
        # Récupérer les valeurs des inputs et les stocker dans l'attribut d'instance
        self.valeurs_saisies = [entry.get() for entry in self.entries]
        
        # Fermer la fenêtre après l'enregistrement
        self.root.destroy()

    def afficher_valeurs(self):
        # Afficher les valeurs saisies après la fermeture de la fenêtre
        return self.valeurs_saisies

    def lancer(self):
        # Démarrer la boucle principale de l'interface
        self.root.mainloop()
       

def show_text(titre,text):
      # Création de la fenêtre principale
    root = tk.Tk()
    root.title(titre)  # Titre de la fenêtre
    root.geometry("450x150")  # Dimensions de la fenêtre

    # Texte à afficher

    # Création du Label pour afficher le texte
    #label = tk.Label(root, text=text, font=("Arial", 10), anchor="w",justify="left")
   # label.pack(padx=20, pady=50)  # Ajoute le label à la fenêtre avec un espacement vertical

    text_widget = tk.Text(root, wrap=tk.WORD, height=10, width=40)
    text_widget.pack(side=tk.LEFT, fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    # Lier la scrollbar au widget Text
    text_widget.config(yscrollcommand=scrollbar.set)

    text_widget.insert(tk.END, text)
    #button = tk.Button(root, text="OK, Merci", command=root.destroy())
    #button.pack (pady=15)     

    # Lancer la boucle principale de l'application
    root.mainloop()


def data_input_option(titre,n,text1,text2,text3):   

    # Création de la fenêtre principale
        root = tk.Tk()
        root.title(titre)  # Titre de la fenêtre
        root.geometry("400x300")  # Dimensions de la fenêtre
        entry1 = tk.Entry(root, font=("Arial", 10))
        label_1 = tk.Label(root, text=text1, font=("Arial", 12))
        entry2 = tk.Entry(root, font=("Arial", 10))
        label_2 = tk.Label(root, text=text2, font=("Arial", 12))
        entry3 = tk.Entry(root, font=("Arial", 10))
        label_3 = tk.Label(root, text=text3, font=("Arial", 12))


        entry1.pack_forget()
        entry2.pack_forget()
        entry3.pack_forget()
        
         # Afficher le nombre d'inputs demandé
        if n >= 1:
            label_1.pack(pady=10)
            entry1.pack(pady=5)  # Afficher le premier champ
           
        if n >= 2:
            label_2.pack(pady=10) 
            entry2.pack(pady=5)  # Afficher le deuxième champ
            
        if n == 3:
            label_3.pack(pady=10)
            entry3.pack(pady=5)  # Afficher le troisième champ
              # Espacement vertical autour du label
        # Masquer tous les champs d'entrée avant de choisir lesquels afficher

        button = tk.Button(root, text="Valider", font=("Arial", 12),command=root.quit)
        button.pack(pady=10)  # Espacement vertical autour du bouton

        # Lancer la boucle principale de l'application
        root.mainloop()
        return(entry1.get(),entry2.get(),entry3.get())

def show_text(titre,text):
      # Création de la fenêtre principale
    root = tk.Tk()
    root.title(titre)  # Titre de la fenêtre
    root.geometry("450x150")  # Dimensions de la fenêtre

    # Texte à afficher

    # Création du Label pour afficher le texte
    #label = tk.Label(root, text=text, font=("Arial", 10), anchor="w",justify="left")
   # label.pack(padx=20, pady=50)  # Ajoute le label à la fenêtre avec un espacement vertical

    text_widget = tk.Text(root, wrap=tk.WORD, height=10, width=40)
    text_widget.pack(side=tk.LEFT, fill="both", expand=True)

    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    # Lier la scrollbar au widget Text
    text_widget.config(yscrollcommand=scrollbar.set)

    text_widget.insert(tk.END, text)
    #button = tk.Button(root, text="OK, Merci", command=root.destroy())
    #button.pack (pady=15)     

    # Lancer la boucle principale de l'application
    root.mainloop()

def menu (titre,list_of_choice,function):
        buttons=[]
        choices_to_function=dict(zip(list_of_choice,function))
        # Fonction appelée lorsqu'on clique sur le bouton
        def on_button_click(list_of_choice):
            print(f"{list_of_choice} cliqué !")
            if list_of_choice in choices_to_function:
                choices_to_function[list_of_choice]()  # Appelle la fonction associée au choix      

        # Création de la fenêtre principale
        root = tk.Tk()
        root.title(titre)

        # Dimensions de la fenêtre
        root.geometry("400x400")

        # Création du bouton

        for choice in list_of_choice:
            button = tk.Button(root, text=choice, command=lambda n=choice: on_button_click(n))
            buttons.append(button)

        # Placement du bouton dans la fenêtre (ici centré)
        for i in range(0,len(list_of_choice)):
            buttons[i].pack(pady=5)

        # Lancer la boucle principale
        root.mainloop()

#FORMATAGE DE DATE
def format_date(date_str):
    jour = int(date_str[6:8])   # 01
    mois = int(date_str[4:6])    # 01
    annee = int(date_str[0:4])

    date_obj = datetime(annee, mois, jour)

# Définir le format souhaité
    format_choisi = "%d %B %Y"

    return(date_obj.strftime(format_choisi))