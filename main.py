from initRoot import *
from penduFolder.penduFile import *
from pianoFolder.pianoFile import *


def startPendu ():
    pendu()

def startPiano ():
    piano()

root.columnconfigure(1,weight=1)

frame1 = Frame(root)
frame1.grid(padx=25, pady=25, columnspan=2)

frame2 = Frame(root)
frame2.grid(padx=25, pady=25, columnspan=2)

titre = Label(frame1, text="Mini Jeux", font=("Ink Free",25))
titre.pack()

btn1 = Button(frame2, text="pendu", command=startPendu)
btn1.grid()

btn2 = Button(frame2, text="piano", command=startPiano)
btn2.grid()


# startPiano()

root.mainloop()

