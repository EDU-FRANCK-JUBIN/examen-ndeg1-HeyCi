import turtle
import random

# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue à  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)


# Declarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
michelangelo = turtle.Turtle()
michelangelo.color("orange")
michelangelo.shape("turtle")
michelangelo.goto(-650, 320)

leonardo = turtle.Turtle()
leonardo.color("deep sky blue")
leonardo.shape("turtle")
leonardo.goto(-650, 167)

raphael = turtle.Turtle()
raphael.color("red")
raphael.shape("turtle")
raphael.goto(-650, 0)

splinter = turtle.Turtle()
splinter.color("dark slate gray")
splinter.shape("turtle")
splinter.goto(-650, -300)

donatello = turtle.Turtle()
donatello.color("orchid")
donatello.shape("turtle")
donatello.goto(-650, -150)

# Demander de saisir dans la console les prédictions des joueurs 1 et 2 dans le format 1,2,3
prono1 = input("Joueur 1, vos pronostics sur les 3 premiers ? ")
liste_prono_j1 = prono1.split(",")
prono2 = input("Joueur 2, vos pronostics sur les 3 premiers ? ")
liste_prono_j2 = prono2.split(",")

print("j1 : {0}".format(liste_prono_j1))


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui représente le nombre de pixels du déplacement vers la droite
turtle_list = [michelangelo, leonardo, raphael, donatello, splinter]
winner_list = []
while len(turtle_list) > 0:
    for tortue in turtle_list:
        avancee = random.randint(0, 5)
        tortue.forward(avancee)
        if tortue.xcor() > 680:
            turtle_list.remove(tortue)
            winner_list.append(tortue)




# Comparer les résultats de la course avec les pronostics des joueurs
# et afficher le résultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0


turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur 1 a  gagné", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()