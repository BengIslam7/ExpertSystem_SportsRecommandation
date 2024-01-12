from experta import *
import tkinter as tk
from tkinter import PhotoImage
import math
#sports percentages
pfoot=0
phand=0
pbask=0
pvolley=0
pnat=0
pcourse=0
pcyc=0
pgolf=0
pwatp=0
ppaddle=0
pmusc=0
ptennis=0
sel1=0
sel2=0
sel3=0
# Définition des faits
class Sport(Fact):
    pass
# Règles du système expert
class RecommandationSport(KnowledgeEngine):
    @Rule(Sport(dheure=True)|Sport(jeuequipe=True) | Sport(agilite = True) | Sport(endurance = True) | Sport(strategie = True) | Sport(pleinair = True) | Sport(vitesse = True))
    def recommend_football(self):
        pass;
    @Rule(Sport(dheure=True)|Sport(jeuequipe=True) | Sport(agilite = True) | Sport(precision = True) | Sport(strategie = True) | Sport(salle = True) | Sport(flexibilite = True))
    def recommend_handball(self):
        pass;
    @Rule(Sport(theure=True)|Sport(jeuindiv=True) | Sport(agilite = True) | Sport(precision = True) | Sport(endurance = True) | Sport(pleinair = True) | Sport(flexibilite = True))
    def recommend_tennis(self):
        pass;
    @Rule(Sport(dheure=True)|Sport(jeuequipe=True) | Sport(agilite = True) | Sport(reflexe = True) | Sport(strategie = True) | Sport(salle = True) | Sport(flexibilite = True))
    def recommend_volleyball(self):
        pass;
    @Rule(Sport(dheure=True)|Sport(jeuequipe=True) | Sport(agilite = True) | Sport(precision = True) | Sport(strategie = True) | Sport(salle = True) | Sport(flexibilite = True))
    def recommend_basketball(self):
        pass;
    @Rule(Sport(heure=True)|Sport(jeuindiv=True) | Sport(endurance = True) | Sport(force = True))
    def recommend_natation(self):
        pass;
    @Rule(Sport(heure=True)|Sport(jeuindiv=True) | Sport(agilite = True) | Sport(precision = True) | Sport(reflexe = True) | Sport(pleinair = True) | Sport(flexibilite = True))
    def recommend_paddle(self):
        pass;
    @Rule(Sport(heure=True)|Sport(jeuindiv=True) | Sport(strategie = True) | Sport(precision = True) | Sport(pleinair = True) | Sport(flexibilite = True))
    def recommend_golf(self):
        pass;
    @Rule(Sport(heure=True)|Sport(jeuequipe=True) | Sport(agilite = True) | Sport(strategie = True) | Sport(endurance = True) | Sport(pleinair = True) | Sport(flexibilite = True))
    def recommend_waterpolo(self):
        pass;
    @Rule(Sport(heure=True)|Sport(jeuindiv=True) | Sport(agilite = True) | Sport(vitesse = True) | Sport(endurance = True) | Sport(pleinair = True) | Sport(strategie = True))
    def recommend_course(self):
        pass;
    @Rule( Sport(dheure=True)|Sport(jeuindiv=True)|Sport(force=True) | Sport(endurance = True) | Sport(pleinair = True) | Sport(flexibilite = True)  )
    def recommend_musculation(self):
        pass;
    @Rule( Sport(heure=True)|Sport(jeuindiv=True)|Sport(vitesse=True) | Sport(endurance = True) | Sport(pleinair = True) | Sport(agilite = True)  )
    def recommend_cyclisme(self):
        pass;
liste=["jeu en equipe","jeu individuel","stratégie","sport en salle","sport en plein air","agrésivité","réflexe","agilité","endurance","précision","flexibilité","vitesse","renforcement musculaire"]
j=0
def no_click(event):
    global j
    if(j<13):
        j=j+1
        if j==13 :
            #resultat
            res_text="Resultat:\nFootball :"+str(pfoot)+"%\nHandball :"+str(phand)+"%\nBasketball :"+str(pbask)+"%\nVolleyball :"+str(pvolley)+"%\nTennis :"+str(ptennis)+"%\nPaddle :"+str(ppaddle)+"%\nNatation :"+str(pnat)+"%\nWater Polo :"+str(pwatp)+"%\nGolf :"+str(pgolf)+"%\nCourse :"+str(pcourse)+"%\nCyclisme :"+str(pcyc)+"%\nMusculation :"+str(pmusc)+"%"
            frame1.destroy()
            frame2.destroy()
            res.config(text=res_text)
        else :
            quest.config(text=liste[j]+" ?")
def yes_click(event):
    global j , pfoot,phand,pbask,ptennis,pwatp,pmusc,ppaddle,pgolf,pcourse,pcyc,pvolley,pnat
    if( j <13 ):
        if(liste[j]=="jeu en equipe"):
            engine.declare(Sport(jeuequipe=True))
            pfoot+=14.28
            phand+=14.28
            pbask+=14.28
            pvolley+=14.28
            pwatp+=14.28
        if(liste[j]=="jeu individuel"):
            engine.declare(Sport(jeuindiv=True))
            pcyc+=16.66
            pmusc+=16.66
            pgolf+=16.66
            pcourse+=14.28
            pnat+=25
            ppaddle+=14.28
            ptennis+=14.28
        if(liste[j]=="stratégie"):
            engine.declare(Sport(strategie=True))
            pfoot+=14.28
            phand+=14.28
            pvolley+=14.28
            pbask+=14.28
            pgolf+=16.66
            pwatp+=14.28
            pcourse+=14.28
        if(liste[j]=="sport en salle"):
            engine.declare(Sport(salle=True))
            phand+=14.28
            pvolley+=14.28
            pbask+=14.28
        if(liste[j]=="sport en plein air"):
            engine.declare(Sport(pleinair=True))
            pfoot+=14.28
            ptennis+=14.28
            ppaddle+=14.28
            pgolf+=16.66
            pwatp+=14.28
            pcourse+=14.28
            pmusc+=16.66
            pcyc+=16.66
        if(liste[j]=="agrésivité"):
            engine.declare(Sport(agressivite=True))
        if(liste[j]=="réflexe"):
            engine.declare(Sport(reflexe=True))
            pvolley+=14.28
            ppaddle+=14.28
        if(liste[j]=="agilité"):
            engine.declare(Sport(agilite=True))
            pfoot+=14.28
            phand+=14.28
            ptennis+=14.28
            pvolley+=14.28
            pbask+=14.28
            ppaddle+=14.28
            pwatp+=14.28
            pcourse+=14.28
            pcyc+=16.66
        if(liste[j]=="endurance"):
            engine.declare(Sport(endurance=True))
            pfoot+=14.28
            ptennis+=14.28
            pnat+=25
            pwatp+=14.28
            pcourse+=14.28
            pmusc+=16.66
            pcyc+=16.66
        if(liste[j]=="précision"):
            engine.declare(Sport(precision=True))
            phand+=14.2857
            ptennis+=14.2857
            pbask+=14.2857
            ppaddle+=14.2857
            pgolf+=16.666666
        if(liste[j]=="flexibilité"):
            engine.declare(Sport(flexibilite=True))
            phand+=14.28
            ptennis+=14.28
            pvolley+=14.28
            pbask+=14.28
            ppaddle+=14.28
            pgolf+=16.66
            pwatp+=14.28
            pmusc+=16.66
        if(liste[j]=="vitesse"):
            engine.declare(Sport(vitesse=True))
            pfoot+=14.28
            pcourse+=14.28
            pcyc+=16.66
        if(liste[j]=="renforcement musculaire"):
            engine.declare(Sport(force=True))
            pnat+=25
            pmusc+=16.66
        j=j+1
        if j==13 :
            #resultat
            res_text="Resultat en pourcentage : \n\nFootball :"+str(math.ceil(pfoot))+"%\n\nHandball :"+str(math.ceil(phand))+"%\n\nBasketball :"+str(math.ceil(pbask))+"%\n\nVolleyball :"+str(math.ceil(pvolley))+"%\n\nTennis :"+str(math.ceil(ptennis))+"%\n\nPaddle :"+str(math.ceil(ppaddle))+"%\n\nNatation :"+str(math.ceil(pnat))+"%\n\nWater Polo :"+str(math.ceil(pwatp))+"%\n\nGolf :"+str(math.ceil(pgolf))+"%\n\nCourse :"+str(math.ceil(pcourse))+"%\n\nCyclisme :"+str(math.ceil(pcyc))+"%\n\nMusculation :"+str(math.ceil(pmusc))+"%"
            frame1.destroy()
            frame2.destroy()
            res.config(text=res_text)
        else :
            quest.config(text=liste[j]+" ?")
def selection():
    global pfoot,phand,pbask,ptennis,pwatp,pmusc,ppaddle,pgolf,pcourse,pcyc,pvolley,pnat
    global sel1 , sel2 , sel3
    if (var1.get() == 1) & (sel1==0):
        engine.declare(Sport(heure=True))
        pnat+=25
        ppaddle+=14.28
        pgolf+=16.66
        pwatp+=14.28
        pcourse+=14.28
        pcyc+=16.66
        sel1=1
    if (var2.get() == 1) & (sel2==0):
        engine.declare(Sport(dheure=True))
        pfoot+=14.28
        phand+=14.28
        pbask+=14.28
        pvolley+=14.28
        pmusc+=16.66
        sel2=1
    if (var3.get() == 1) & (sel3==0):
        engine.declare(Sport(theure=True))
        ptennis+=14.28
        sel3=1
engine = RecommandationSport()
# Les faits peuvent être ajoutés ici
engine.reset()
root = tk.Tk()
root.geometry("900x400")
l = tk.Label(root, width=27, text='RECOMMANDATION SPORTIVE',font=("Arial", 26),foreground="green")
l.pack(pady=10)
image_path = "sports 3.png"  # Change this to the path of your image file
img = PhotoImage(file=image_path)
# Create a label and set the image
label = tk.Label(root, image=img)
label.pack(side=tk.RIGHT)
# Frame for the first set of widgets (quest, YES, NO)
frame2 = tk.Frame(root)
frame2.pack(padx=2,pady=10)
quest1 = tk.Label(frame2, text="Temps",foreground="green")
quest1.pack(side=tk.LEFT)
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(frame2, text='1 heure',variable=var1, onvalue=1, offvalue=0,command=selection)
c1.pack(side=tk.LEFT)
c2 = tk.Checkbutton(frame2, text='2 heure',variable=var2, onvalue=1, offvalue=0,command=selection)
c2.pack(side=tk.LEFT)
c3 = tk.Checkbutton(frame2, text='3 heure',variable=var3, onvalue=1, offvalue=0,command=selection)
c3.pack(side=tk.LEFT)
# End of frame
# Frame for the second set of widgets (Temps, 1heure, 2heure, 3heure)
frame1 = tk.Frame(root)
frame1.pack()
quest = tk.Label(frame1, text=liste[j] + " ?",foreground="green")
quest.pack(side=tk.LEFT)
button = tk.Button(frame1, text="YES")
button2 = tk.Button(frame1, text="NO")
button.bind("<Button-1>", yes_click)
button2.bind("<Button-1>", no_click)
button.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=5)
# End of frame
# Result frame
frame3 = tk.Frame(root)
frame3.pack()
res = tk.Label(frame3, text="Resultat en pourcentage : \n",borderwidth=2, relief="solid",foreground="green")
res.pack(side=tk.LEFT,pady=20)
# End of result frame
root.mainloop()
engine.run()

