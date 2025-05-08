import PIL as pil
import tkinter as tk
from PIL import Image
import random
from time import *
import tkinter.font as font
from tkinter import messagebox

"""Fonctions interface"""

import tkinter as tk
from time import sleep

def center_window(window, width, height):
    """
    Centre la fenêtre à l'écran.

    Args:
    window (tk.Tk): La fenêtre tkinter à centrer.
    width (int): Largeur de la fenêtre.
    height (int): Hauteur de la fenêtre.
    """
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def menu():
    """
    Affiche le menu principal du jeu avec les boutons 'Quitter' et 'Jouer'.
    Si 'Jouer' est cliqué, retourne True pour démarrer une nouvelle partie.

    Returns:
    bool: Retourne True si le bouton 'Jouer' est cliqué, False sinon.
    """
    def etat_quit():
        """Ferme la fenêtre et retourne l'état du bouton 'Jouer'"""
        fenetrem.destroy()
        return etat_play.set(1)

    fenetrem = tk.Tk()
    fenetrem.title("Menu Blackjack")
    center_window(fenetrem, 800, 600)
    fenetrem.update()
    sleep(1)  
    fenetrem.attributes("-fullscreen", True)

    background = tk.PhotoImage(file="menu.png")
    background_label = tk.Label(fenetrem, image=background)
    background_label.place(x=0, y=0)

    etat_play = tk.BooleanVar(fenetrem)  
    etat_play.set(0)  

    bouton_quitter = tk.Button(fenetrem, text="QUITTER", command=fenetrem.destroy, width=20, height=2, bg='white')
    bouton_quitter.place(x=980, y=500)

    bouton_play = tk.Button(fenetrem, text="JOUER", command=lambda: etat_quit(), width=20, height=2, bg='white')
    bouton_play.place(x=700, y=500)

    myFont = font.Font(family='Comic Sans MS', size=15, weight='bold')
    bouton_quitter['font'] = myFont
    bouton_play['font'] = myFont

    fenetrem.mainloop()
    return etat_play.get()  

def as_menu():
    """
    Affiche une fenêtre demandant à l'utilisateur de choisir la valeur de l'As : 1 ou 11.
    Lorsque le choix est fait, retourne la valeur sélectionnée.

    Returns:
    int: La valeur choisie pour l'As (1 ou 11).
    """
    def etat_quit(valeur):
        """Ferme la fenêtre et retourne l'état de la valeur choisie"""
        fenetreas.destroy()
        return valeur

    def etat_11():
        global valeur
        etat_as = 11
        valeur = etat_quit(etat_as)
        return valeur

    def etat_1():
        global valeur
        etat_as = 1
        valeur = etat_quit(etat_as)
        return valeur

    fenetreas = tk.Tk()
    fenetreas.title("Valeur de l'as")
    background = tk.PhotoImage(file="menu.png")
    background_label = tk.Label(fenetreas, image=background)
    background_label.place(x=0, y=0)
    fenetreas.attributes("-fullscreen", True)
    bouton_quitter = tk.Button(fenetreas, text="X", command=fenetreas.destroy, width=5, bg="red")
    bouton_quitter.place(x=0, y=0)

    myFont = font.Font(family='Comic Sans MS', size=15, weight='bold')

    valeur_as = tk.Label(fenetreas, text="quelle est la valeur de l'as?", width=38, height=2, bg='#228B00', highlightthickness=3, highlightcolor="white")
    bouton_11 = tk.Button(fenetreas, text="AS = 11", command=etat_11, width=20, height=2, bg='white')
    bouton_1 = tk.Button(fenetreas, text="AS = 1", command=etat_1, width=20, height=2, bg='white')
    valeur_as['font'] = myFont
    bouton_11['font'] = myFont
    bouton_1['font'] = myFont
    valeur_as.place(x=728, y=420) 
    bouton_11.place(x=980, y=500)
    bouton_1.place(x=700, y=500)
    fenetreas.mainloop()
    return valeur

def quitter():
    """
    Ferme la fenêtre de jeu actuelle et arrête la partie en cours.
    """
    global etat_remake
    global fenetre
    global Fin
    etat_remake = False
    fenetre.destroy()

def remake():
    """
    Permet de démarrer une nouvelle partie en fermant la fenêtre actuelle et en réinitialisant l'état de la partie.
    """
    global etat_remake
    global fenetre
    fenetre.destroy()
    etat_remake = True

def affichage_carte1_joueur(img_carte):
    """
    Affiche la première carte du joueur à l'écran.

    Args:
    img_carte (tk.PhotoImage): L'image de la carte à afficher.
    """
    label1 = tk.Label(fenetre, image=img_carte)
    label1.place(x=910, y=720)

def affichage_carte1_croupier(img_carte):
    """
    Affiche la première carte du croupier à l'écran.

    Args:
    img_carte (tk.PhotoImage): L'image de la carte à afficher.
    """
    label1 = tk.Label(fenetre, image=img_carte)
    label1.place(x=910, y=80)

def affichage_carte_retournee_croupier(img_carte):
    """
    Affiche la deuxième carte du croupier à l'écran (carte retournée).

    Args:
    img_carte (tk.PhotoImage): L'image de la carte retournée à afficher.
    """
    label1 = tk.Label(fenetre, image=img_carte)
    label1.place(x=931, y=102)

def affichage_carte2_joueur(img_carte):
    """
    Affiche la deuxième carte du joueur à l'écran.

    Args:
    img_carte (tk.PhotoImage): L'image de la carte à afficher.
    """
    label2 = tk.Label(fenetre, image=img_carte)
    label2.place(x=931, y=742)

def affichage_carte_hit(img_carte, x, y):
    """
    Affiche les cartes "hit" du joueur à l'écran.

    Args:
    img_carte (tk.PhotoImage): L'image de la carte à afficher.
    x (int): Position x de la carte à afficher.
    y (int): Position y de la carte à afficher.
    """
    label3 = tk.Label(fenetre, image=img_carte)
    label3.place(x=x, y=y)

def charger_image(carte):
    """
    Charge l'image de la carte et l'ajoute à la liste des images du joueur.

    Args:
    carte (str): Nom de la carte à charger.
    """
    global img
    global liste_images_cartes
    img = tk.PhotoImage(file="cartes/" + str(carte) + ".png")
    liste_images_cartes.append(img)

def charger_image_croupier(carte):
    """
    Charge l'image de la carte et l'ajoute à la liste des images du croupier.

    Args:
    carte (str): Nom de la carte à charger.
    """
    global img
    global liste_images_croupier
    img = tk.PhotoImage(file="cartes/" + str(carte) + ".png")
    liste_images_croupier.append(img)

def stand():
    """
    Permet au joueur de rester sur son choix de cartes (action 'stand').
    Lance ensuite le tour du croupier et fait piocher des cartes si nécessaire.
    """
    global etat_stand
    global liste_images_cartes
    global liste_images_croupier
    global bouton_hit
    global bouton_remake
    global croupier
    global compteur_hit
    global cartealeatoire
    global croupierhit
    global carte
    bouton_hit.config(state="disabled")
    bouton_remake.config(state="normal")
    etat_stand = True
    liste_carte = []
    affichage_carte_retournee_croupier(liste_images_cartes[8])
    if croupier > 16:
        conditions()
    else:
        compteur = 0
        nb = 10
        while croupier <= 16:
            if croupier <= 16:
                c = carte[cartealeatoire[nb]]
                liste_carte.append(c)
                liste_images_croupier.append(charger_image_croupier(afficher_carte(nb)))
                for valeur in liste_carte:
                    if valeur == 12 or valeur == 13 or valeur == 14:
                        croupier = croupier - valeur + 10
                    elif valeur == 11:
                        croupier = croupier - valeur + 1
                else:
                    croupier += c
                    compteur += 1
                    nb += 1
            if compteur == 1:
                affichage_carte_hit(liste_images_croupier[0], 952, 124)
            if compteur == 2:
                affichage_carte_hit(liste_images_croupier[2], 973, 146)
            if compteur == 3:
                affichage_carte_hit(liste_images_croupier[4], 994, 168)
            if compteur == 4:
                affichage_carte_hit(liste_images_croupier[6], 1015, 190)
            if compteur == 5:
                affichage_carte_hit(liste_images_croupier[8], 1036, 212)
            if compteur == 6:
                affichage_carte_hit(liste_images_croupier[10], 1057, 234)
        conditions()
    return etat_stand

def hit():
    """
    Affiche une carte du "hit" (nouvelle carte tirée) pour le joueur.
    Si le score du joueur atteint 21 ou plus, la partie se termine.
    """
    global joueur
    global liste_images_cartes
    global etat_hit
    global bouton_hit
    global croupierhit
    global compteur_hit
    global compteur
    global cartealeatoire
    global carte

    liste_score = []
    compteur_hit += 1
    if joueur < 21:
        cartehit = carte[cartealeatoire[croupierhit]]
        liste_score.append(cartehit)
        liste_images_cartes.append(charger_image(afficher_carte(croupierhit)))
        for valeur in liste_score:
            if valeur == 12 or valeur == 13 or valeur == 14:
                joueur = joueur - valeur + 10
                compteur.config(text='score : ' + str(joueur))
        else:
            joueur += cartehit
            compteur.config(text='score : ' + str(joueur))
            croupierhit += 1
            etat_hit.set(0)

    if compteur_hit == 1:
        sleep(0.2)
        affichage_carte_hit(liste_images_cartes[10], 952, 764)
    elif compteur_hit == 2:
        sleep(0.2)
        affichage_carte_hit(liste_images_cartes[12], 1100, 720)
    elif compteur_hit == 3:
        sleep(0.2)
        affichage_carte_hit(liste_images_cartes[14], 1122, 742)
    elif compteur_hit == 4:
        sleep(0.2)
        affichage_carte_hit(liste_images_cartes[16], 1144, 764)
    elif compteur_hit == 5:
        sleep(0.2)
        affichage_carte_hit(liste_images_cartes[18], 1166, 799)
    elif compteur_hit == 6:
        sleep(0.2)
        affichage_carte_hit(liste_images_cartes[20], 1188, 834)
    if joueur >= 21:
        bouton_hit.config(state="disabled")
        affichage_carte_retournee_croupier(liste_images_cartes[8])
        conditions()

    etat_hit.set(0)
    return compteur_hit

def conditions():
    """
    Détermine les conditions de fin de jeu. Compare les scores du joueur et du croupier pour afficher un message de victoire, égalité ou défaite.
    """
    global Fin
    global joueur
    global croupier
    global bouton_stand
    global bouton_remake

    def desactiver_boutons():
        bouton_stand.config(state="disabled")
        bouton_hit.config(state="disabled")

    bouton_remake.config(state="normal")
    if joueur == 21 and croupier != 21:
        messagebox.showinfo("blackjack!", "Le croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nVous avez gagné")
        Fin = True
        desactiver_boutons()
        return
    if joueur == 21 and croupier == 21:
        messagebox.showinfo("draw!", "Le croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nC'est une égalité")
        Fin = True
        desactiver_boutons()
        return
    if joueur == croupier:
        messagebox.showinfo("draw!", "Le croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nC'est une égalité")
        desactiver_boutons()
        Fin = True
        return
    if (joueur > croupier) or (croupier > 22):
        if joueur > 21:
            desactiver_boutons()
            if croupier > 21:
                messagebox.showinfo("draw!", "Le croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nC'est une égalité")
                Fin = True
                return
            else:
                messagebox.showinfo("lose!", "Le croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nVous avez perdu")
                Fin = True
                return
        else:
            messagebox.showinfo("win!", "\nLe croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nVous avez gagné")
            desactiver_boutons()
            Fin = True
            return
    if croupier > joueur and croupier < 22:
        desactiver_boutons()
        if joueur > 21:
            messagebox.showinfo("draw!", "Le croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nC'est une égalité")
            Fin = True
            return
        else:
            messagebox.showinfo("lose!", "\nLe croupier possède " + str(croupier) + "\nVous avez " + str(joueur) + "\nvous avez perdu")
            Fin = True
            return
    return Fin

def afficher_carte(nb):
    """
    Affiche une carte choisie au hasard et retourne son nom et sa valeur.
    Permet également de vérifier la carte du deck.

    Args:
    nb (int): Le numéro de la carte piochée.

    Returns:
    str: Le nom de la carte (ex: '1_trèfle').
    """
    global carte
    global cartealeatoire
    global symboles
    global deck 
    global joueur
    global croupier
    valeur = carte[cartealeatoire[nb]]
    symbole = random.choice(symboles)
    current_card = valeur, symbole
    if (valeur, "coeur") and (valeur, "trefle") and (valeur, 'carreau') and (valeur, 'pique') not in deck:
        nb += 1
    while current_card not in deck:
        valeur = carte[cartealeatoire[nb]]
        symbole = random.choice(symboles)
        current_card = valeur, symbole
    if current_card[0] == 1:
        valeur = 'As'
        carte_affich = str(valeur) + '_' + str(symbole)
    if current_card[0] == 12 or current_card[0] == 13 or current_card[0] == 14:
        if current_card[0] == 12:
            valeur = "valet"
        elif current_card[0] == 13:
            valeur = "reine"
        elif current_card[0] == 14:
            valeur = "roi"
        deck.remove(current_card)
        current_card = (10, symbole)
        carte_affich = str(valeur) + '_' + str(symbole)
        return carte_affich
    deck.remove(current_card)    
    carte_affich = str(valeur) + '_' + str(symbole)
    return carte_affich

def set_hit():
    """
    Appelle la fonction 'hit' et met à jour l'état de l'action 'hit' du joueur.
    """
    global etat_hit
    hit()
    etat_hit.set(1)
    return

def distribution(condi):
    """
    Distribue les cartes initiales du joueur et du croupier, et met à jour les scores.

    Args:
    condi (int): Indicateur de l'état de la distribution des cartes (0 pour le début du jeu).
    """
    global joueur
    global croupier
    global croupierhit
    global cartealeatoire
    global liste_images_cartes
    global carte
    global etat_hit
    global compteur_hit
    global bouton_remake
    global etat_stand
    global As_val
    liste_score_joueur = []
    liste_score_croupier = []

    def update():
        """Met à jour le score du joueur à l'écran"""
        return compteur.config(text='score : ' + str(joueur))

    if condi == 0:
        bouton_remake.config(state="disabled")
        c1_j = carte[cartealeatoire[0]]
        liste_score_joueur.append(c1_j)
        liste_images_cartes.append(charger_image(afficher_carte(0)))
        affichage_carte1_joueur(liste_images_cartes[0])

        c1_c = carte[cartealeatoire[1]]
        liste_score_croupier.append(c1_c)
        liste_images_cartes.append(charger_image(afficher_carte(1)))
        affichage_carte1_croupier(liste_images_cartes[2])

        c2_j = carte[cartealeatoire[2]]
        liste_score_joueur.append(c2_j)
        liste_images_cartes.append(charger_image(afficher_carte(2)))
        affichage_carte2_joueur(liste_images_cartes[4])

        liste_images_cartes.append(charger_image('dos'))
        affichage_carte_retournee_croupier(liste_images_cartes[6])

        c2_c = carte[cartealeatoire[3]]
        liste_score_croupier.append(c2_c)
        liste_images_cartes.append(charger_image(afficher_carte(3)))

        joueur += c1_j
        joueur += c2_j
        update()

        for valeur in liste_score_joueur:
            if valeur == 12 or valeur == 13 or valeur == 14:
                joueur = joueur - valeur + 10
                update()

        croupier += c1_c
        croupier += c2_c
        nb_as_11 = 0

        for valeur in liste_score_croupier:
            if valeur == 12 or valeur == 13 or valeur == 14:
                croupier = croupier - valeur + 10
            if valeur == As_val and nb_as_11 == 0:
                croupier = croupier - valeur + 11
                nb_as_11 += 1
            elif valeur == As_val and nb_as_11 != 0:
                croupier = croupier - valeur + 1

        if joueur >= 21:
            bouton_hit.config(state="disabled")
            affichage_carte_retournee_croupier(liste_images_cartes[8])
            conditions()
        return
    return

"""Programme principal"""
Fin = False
etat_remake=False
fenetre_menu = menu()

while Fin is not True  or etat_remake == True:
    if fenetre_menu == True:
        As_val = as_menu()
    else:
        As_val = 0
    carte = [As_val, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
    symboles = ['trefle', 'coeur', 'carreau', 'pique']
    deck = [(card,suit) for card in carte for suit in symboles]
    # peut être ajouter le bet
    croupierhit = 4  # carte retourné sur la table
    cartealeatoire = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    joueur = 0
    croupier = 0
    random.shuffle(cartealeatoire)
    tour = 0
    
    if As_val != 0 and fenetre_menu == True:
        
    #creation de la fenetre
        fenetre= tk.Tk()
        fenetre.title("blackjack")
        fenetre.bind('<Escape>', lambda e: fenetre.destroy())
        background= tk.PhotoImage(file="background.png")
        background_label = tk.Label(fenetre, image=background)
        background_label.place(x=0, y=0)
        fenetre.attributes("-fullscreen",True)
        liste_images_cartes=[]
        liste_images_croupier=[]
        #creation des boutons

        bouton_quitter = tk.Button(fenetre, text="X", command=quitter, width=5, bg="red")
        bouton_quitter.grid(column=0,row=0)

        bouton_stand= tk.Button(fenetre, text="STAND", command=stand, width=20, bg='green')
        bouton_stand.place(x=1080, y=980)

        bouton_remake= tk.Button(fenetre, text="REMAKE", command=remake, width=20, bg='green')
        bouton_remake.place(x=700, y=980)

        bouton_hit= tk.Button(fenetre, text="HIT", command= set_hit, width=20, bg='green')
        bouton_hit.place(x=890, y=980)

        # création des labels qui servent de textes

        compteur= tk.Label(fenetre,text='',font=("Lithograph", 14),bg='#228B00')
        compteur.place(x=720,y=800)

        As_valeur = tk.Label(fenetre,text="L'As vaut "+str(As_val)+".",font=("Lithograph", 14),bg='#228B00')
        As_valeur.place(x=720,y=850)


        compteur_hit=0
        
        # creation variable booleen
        etat_hit = tk.BooleanVar(fenetre)  
        etat_hit.set(0) # intialisation de la variable a False
        etat_stand= False

        #on distribue les 1eres cartes
        distribution(joueur)
        fenetre.mainloop()
        
    else:
        Fin = True
    