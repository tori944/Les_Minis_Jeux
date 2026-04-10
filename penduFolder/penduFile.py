# from ..init import *
from random import randint
from re import sub      # revoir ce module
from initRoot import *


def pendu ():
    """fonction du jeu du pendu"""

    ### création de la fenêtre ###

    window = Toplevel(root)
    window.title("jeu du pendu")
    window.geometry("400x350")

    motTk = StringVar()
    lettresTk = StringVar()
    erreurTk = IntVar()
    serieTk = IntVar()

    global serie
    serie = 0
    serieTk.set(serie)

    def rejouer ():
        jouer()
        btnR.grid_forget()


    btnR = Button(window, text="rejouer !", command=rejouer)
    
    def defMot ():
        global listeLettresMot
        global mot
        """définit le mot à trouver"""

        f = open("penduFolder/mots.txt", "r", encoding='utf-8')

        ligne = randint(1,330)
        i = 1

        for l in f :
            if i == ligne:
                mot = sub(r'[\n]', '', l)
                break
            i += 1

        f.close()
        
        listeLettresMot = list(mot)
    
    def configColor (color):
        window.config(bg=color)
        text1.config(bg=color)
        text2.config(bg=color)
        text3.config(bg=color)
        text4.config(bg=color)
        text5.config(bg=color)
        text6.config(bg=color)
        frame2.config(bg=color)
        frame1.config(bg=color)
        frame3.config(bg=color)


    def jouer ():
        global lettresDejaDonne, erreur

        lettresDejaDonne = []  
        erreur = 0 
        

        lettresTk.set(lettresDejaDonne)
        erreurTk.set(erreur)
        
        
        defMot()
        revelation()
        window.bind('<KeyPress>', keyPress)
        configColor("#F0F0F0")
        
    def lose ():
        window.unbind('<KeyPress>')

        configColor("red")
        
        motTk.set(mot)
        btnR.grid(column=1, row=1)

    def win ():
        window.unbind('<KeyPress>')
        configColor("light green")

        btnR.grid(column=1, row=1)

    def revelation (): # donné la lettre en argument de la revelation ??
        global erreur, listeLettresMot, serie
        motVar = "" # la varriable du mot affiché avec les _
        compt = 0

        oldMotVar = motTk.get()

        for i in listeLettresMot:
            if compt == 0 or compt == len(listeLettresMot)-1 or i in lettresDejaDonne :
                motVar = motVar + i
            else :
                motVar = motVar + '_'
            compt += 1
        motTk.set(motVar)

        if motVar == oldMotVar:
            erreur += 1
            erreurTk.set(erreur)
            if erreur == 9:
                serie = 0
                serieTk.set(serie)
                lose()

        if motVar == mot:
            serie += 1
            serieTk.set(serie)
            win()


    def newLettre (lettre):
        """ajouter une lettre à la liste et révélé"""

        if len(lettre) > 1:
            for l in lettre :
                lettresDejaDonne.append(l)
        else:
            lettresDejaDonne.append(lettre)

        lettresTk.set(lettresDejaDonne)
        revelation()


    def keyPress (event):
        """si une lettre du clavier est pressé"""
        lettre = event.keysym

        if lettre not in lettresDejaDonne:

            if lettre.isalpha() and len(lettre) == 1:

                if lettre == "e":
                    lettre = ["e", "é", "è", "ê"]
                elif lettre == "c":
                    lettre = ["c", "ç"]
                elif lettre == "a":
                    lettre = ["a", "à"]

                newLettre(lettre)

    
    frame1 = Frame(window)                              # frame du mot et des lettres
    frame1.grid(padx=25, pady=25, column=0, row=0)
 
    text1 = Label(frame1, textvariable=motTk, font=("Courier New", 25)) # le mot afficher avec les _
    text1.grid(padx=25, pady=25)

    text2 = Label(frame1, textvariable=lettresTk)       # les lettres echoués
    text2.grid(padx=25, pady=25)

    frame2 = Frame(window)                              # frame des erreurs
    frame2.grid(padx=25, pady=25, column=0, row=1)

    text3 = Label(frame2, text="Nb erreur :", font=("",20))
    text3.grid()

    text4 = Label(frame2, textvariable=erreurTk, font=("",15))        # le nombre d'erreur
    text4.grid()

    frame3 = Frame(window)                              # frame des series
    frame3.grid(padx=25, pady=25, column=1, row=0)

    text5 = Label(frame3, text="série", font=("",20))
    text5.grid()
    
    text6 = Label(frame3, textvariable=serieTk, font=("",15))
    text6.grid()


    jouer()
 

