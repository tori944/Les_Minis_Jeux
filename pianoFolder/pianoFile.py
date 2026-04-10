from initRoot import *

def piano ():
    """fonction du jeu du piano"""   

    #### création de la fenêtre ####

    window = Toplevel(root)
    window.title("jeu du piano")
    # window.geometry("250x200")

    ## création des touches
    # dans un canvas

    canvas = Canvas(window, width=650, height=300, bg="light yellow")
    canvas.grid(padx=25, pady=25)

    lastColor = ""

    def clicGDown (event):
        global lastColor
        item = canvas.find_withtag("current")[0]  ### alors là par contre je n'ai pas compris
        lastColor = canvas.itemcget(item, "fill")
        canvas.itemconfig(item, fill="red")

        # pour afficher la mote de la touche

        for cle in dicoNT.keys():
            if dicoNT[cle] == item:
                print(f"la note est {cle}")
                break

    
    def clicGUp (event):
        global lastColor
        item = canvas.find_withtag("current")
        canvas.itemconfig(item, fill=lastColor)
        
    
    # les touches

    notes = ["do", "reB", "re", "miB", "mi", "fa", "solB", "sol", "laB", "la", "siB", "si"]
    couleurs = ["green", "yellow", "orange"]

    dicoNT = {}  # dictionnaire key -> Notes= / value -> Touche

    comptCouleur = 0
    x = 50
    y = 25

    xb = 50 + 75//2
    yb = 175

    for note in notes:
        if notes.index(note) in [1, 3, 6, 8, 10]:
            #dicoNT[note] = canvas.create_rectangle((x+75//2)-75-5, y, x+75-5, y+(175//2), fill="black", tags="up", outline="white")
            dicoNT[note] = canvas.create_rectangle(x-(75//3), y, x+(75//3), y+((175*2)//3), fill="black", tags="up")
            # x += 75

        else:
            dicoNT[note] = canvas.create_rectangle(x, y, x+75, y+175, fill=couleurs[comptCouleur])
            x += 75

            if comptCouleur == len(couleurs)-1 :
                comptCouleur = 0
            else:
                comptCouleur += 1

        canvas.tag_bind(dicoNT[note], "<Button-1>", clicGDown)
        canvas.tag_bind(dicoNT[note], "<ButtonRelease-1>", clicGUp)
    
    canvas.tag_raise("up")




    