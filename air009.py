'''
Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.

Utilisez une fonction de ce genre (selon votre langage) :
ma_rotation(array) {
	# votre algorithme
	return (new_array)
}


Exemples d’utilisation :
$> python exo.py “Michel” “Albert” “Thérèse” “Benoit”
Albert, Thérèse, Benoit, Michel


Afficher error et quitter le programme en cas de problèmes d’arguments.

'''
import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l) <=1:
      print("erreur")
      sys.exit()
    else:
        return l

#On modifi le tableau en saugardant ine valeur temporaire qu'ond reasigne:
def left(l):
	l2=[]
	n=0
	N=len(l)
	while n<N:
		l2.append("x") # Je créer une liste qui a le meme nombre d'argument de la liste originel.
		n+=1
	for i in range(len(l)):# on copi chaque valeur d'arguments de l dans l2 en decalan de 1 ver la gauche. 
		if i!=0:
			l2[i-1]=l[i]
		else:
			l2[-1]=l[i]
	return l2




# On affiche le resulta a partire de la liste modifier:
def result(l):
	phrase=", ".join(l)
	print(phrase)


# appel des fonctions : 
l= input_data()
l2=left(l)
result(l2)





