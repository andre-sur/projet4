import tkinter as tk

from tkinter import messagebox


def options_exclu():
    def enregistrer_resultats():
    # Fonction pour afficher les résultats dans la console
        for i, var in enumerate(list_vars):
            print(f"Choix {i+1}: {var.get()}")  # Affiche 0 ou 1 pour chaque choix

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Labels avec choix binaires")

    # Liste pour stocker les variables de chaque Checkbutton
    list_vars = []

    # Nombre de labels (questions)
    n_labels = 3  # Exemple avec 3 labels

    # Créer des Checkbuttons pour chaque label, avec deux choix côte à côte
    for i in range(n_labels):
        # Créer une frame pour chaque label et ses choix binaires
        frame = tk.Frame(root)
        frame.pack(pady=10, anchor="w")  # Pack la frame avec un peu de marge

        label = tk.Label(frame, text=f"Label {i+1}: Choisir une option")
        label.pack(side=tk.TOP, anchor="w")

        # Variables associées à chaque Checkbutton
        var1 = tk.IntVar()  # Valeur 0 ou 1 pour la première option
        var2 = tk.IntVar()  # Valeur 0 ou 1 pour la deuxième option

        # Ajouter les choix côte à côte dans la même frame
        check1 = tk.Checkbutton(frame, text="Option 1", variable=var1)
        check2 = tk.Checkbutton(frame, text="Option 2", variable=var2)
        
        # Pack les deux options côte à côte
        check1.pack(side=tk.LEFT, padx=10)
        check2.pack(side=tk.LEFT, padx=10)

        # Ajouter les variables à la liste pour pouvoir enregistrer plus tard
        list_vars.append((var1, var2))

    # Bouton pour enregistrer les résultats
    enregistrer_btn = tk.Button(root, text="Enregistrer les résultats", command=enregistrer_resultats)
    enregistrer_btn.pack(pady=10)

# Lancer la boucle principale de l'interface graphique
    root.mainloop()
#CECI EST UN ESPACE DE TEST INDEPENDANT DU PROGRAMME PRINCIPAL
#AFIN DE PREPARER DES "VUES" ET LES TESTER

def input_datas(texte):

    def quit_window():
        root.quit()

    root = tk.Tk()
    root.title("Demande d'Input")  # Titre de la fenêtre
    root.geometry("400x200")  # Dimensions de la fenêtre

    # Texte à afficher dans le label - voir paramètre
    
    # Création du Label pour afficher le texte
    label_instruction = tk.Label(root, text=texte, font=("Arial", 14))
    label_instruction.pack(pady=10)  # Espacement vertical autour du label

    # Champ de saisie pour l'utilisateur
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=10)  # Espacement vertical autour du champ de saisie

    # Bouton pour valider l'entrée
    button = tk.Button(root, text="Valider", font=("Arial", 12),command=root.quit)
    button.pack(pady=10)  # Espacement vertical autour du bouton

    # Label pour afficher le résultat de la saisie
    label_resultat = tk.Label(root, text="", font=("Arial", 14))
    label_resultat.pack(pady=10)  # Espacement vertical autour du label résultat

    # Lancer la boucle principale de l'application
    root.mainloop()
    return(entry.get())

def show_text(text):
      # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Affichage de Texte")  # Titre de la fenêtre
    root.geometry("400x400")  # Dimensions de la fenêtre

    # Texte à afficher
    texte = text

    # Création du Label pour afficher le texte
    label = tk.Label(root, text=texte, font=("Arial", 10), anchor="w",justify="left")
    label.pack(padx=20, pady=50)  # Ajoute le label à la fenêtre avec un espacement vertical

    # Lancer la boucle principale de l'application
    root.mainloop()


def show_message(titre,information):

# Fonction pour afficher le message et fermer la fenêtre

    messagebox.showinfo(titre, information)
   
def choice_yesno (titre,message):
    response = messagebox.askyesno(titre,message)
    return(response)

def data_input_option(liste_options):
        entry=[]
        label=[]
        entrypad=[]
        labelpad=[]
    # Création de la fenêtre principale
        root = tk.Tk()
        root.title("Fenêtre avec Inputs Variables")  # Titre de la fenêtre
        root.geometry("400x300")  # Dimensions de la fenêtre
        for x in range (0,len(liste_options)):
            entry.append(f"entry{x} = tk.Entry(root)")
            label.append(f"label{x}  = tk.Label(root, text=text1, font=('Arial', 12)")
            labelpad.append("label"+x+".pack(pady=10)")
            entrypad.append("entry"+x+".pack(pady=5)")

        for y in range(0,len(liste_options)):
            exec(label[y])
            exec(labelpad[y])
      
 # Afficher le troisième champ
              # Espacement vertical autour du label
        # Masquer tous les champs d'entrée avant de choisir lesquels afficher

        button = tk.Button(root, text="Valider", font=("Arial", 12),command=root.quit)
        button.pack(pady=10)  # Espacement vertical autour du bouton

        # Lancer la boucle principale de l'application
        root.mainloop()
        return(entry1.get(),entry2.get(),entry3.get())

def choice_scroll(options) :

    def afficher_selection():
        choix = variable.get()  # Récupère la sélection actuelle du menu déroulant
        label_resultat.config(text=f"Vous avez sélectionné : {choix}")
        root.quit()
        
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Menu Déroulant")  # Titre de la fenêtre
    root.geometry("400x200")  # Dimensions de la fenêtre

    # Liste d'options pour le menu déroulant
    

    # Variable pour stocker la sélection de l'utilisateur
    variable = tk.StringVar(root)
    variable.set(options[0])  # Définir l'option par défaut (ici la première option)

    # Création du widget OptionMenu avec la liste d'options
    option_menu = tk.OptionMenu(root, variable, *options)
    option_menu.pack(pady=20)

    # Bouton pour afficher la sélection
    button = tk.Button(root, text="Valider", font=("Arial", 12), command=afficher_selection)
    button.pack(pady=10)

    # Label pour afficher le résultat de la sélection
    label_resultat = tk.Label(root, text="", font=("Arial", 14))
    label_resultat.pack(pady=10)

    # Lancer la boucle principale de l'application
    root.mainloop()
    return(variable.get())

def action_choix1():
        
        answer=input_datas("écris un mot")
        code=show_message("xxx","Tu as répondu  "+answer)
        x,y,z=data_input_option(2,"choix premier","un autre choix","le dernier")
        code=show_message("aaa","Tu as répondu  "+x+" mais aussi "+y)

def action_choix2():
        print ("action choix 2 kjkjslfkjdf")
        choix=choice_yesno("confirmation","tu veux le 2 ?")
        if choix:
                show_message("confirme","tu as dis oui ?")
        else:
                show_message("non","tant pis")

def action_choix3():
        options_exclu()

def action_choix4():
        options = ["Tuyau", "Verrou", "table", "Chien", "Option 5"]
        choix=choice_scroll(options)
        show_message("abcd","Tu as répondu  "+choix)


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
        root.geometry("300x200")

        # Création du bouton

        for choice in list_of_choice:
            button = tk.Button(root, text=choice, command=lambda n=choice: on_button_click(n))
            buttons.append(button)

        # Placement du bouton dans la fenêtre (ici centré)
        for i in range(0,len(list_of_choice)):
            buttons[i].pack(pady=5)

        # Lancer la boucle principale
        root.mainloop()

    #DEFINITION DU CONTENU DU MENU ET DES FONCTIONS ASSOCIEES

t="un titre"
loc=["manger","dormir","penser","prendre un bain"]
f=[action_choix1,action_choix2,action_choix3,action_choix4]



tournois=[[(['Albert', 0.5], ['BÃ©atrice', 0.5]), (['Carole', 0], ['Denis', 1]), (['Edouard', 0], ['FranÃ§ois', 1]), (['GÃ©rard', 1], ['Hector', 0]), (['Isabelle', 1], ['Jules', 0]), (['Karl', 0], ['Louis', 1])], [(['Denis', 0.5], ['FranÃ§ois', 0.5]), (['FranÃ§ois', 0.5], ['Isabelle', 0.5]), (['Louis', 1], ['Albert', 0]), (['BÃ©atrice', 0], ['Carole', 1]), (['BÃ©atrice', 0.5], ['Hector', 0.5]), (['Jules', 0.5], ['Karl', 0.5])]]
texte_complet=""
for t in range(0,len(tournois)):
        print("ROUND #"+str(t))
        print("-----------------")
        for u in range(0,len(tournois[t])):
            texte_complet+="#"+str(u+1)+" "+tournois[t][u][0][0]+" vs "+tournois[t][u][1][0]+" => "+str(tournois[t][u][0][1])+" - "+str(tournois[t][u][1][1])+"\n"
           
show_text(texte_complet)




menu (t,loc,f)


