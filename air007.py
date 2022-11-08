'''
Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant. Le dernier argument est l’élément à ajouter.

Utilisez une fonction de ce genre (selon votre langage) :
sorted_insert(array, new_element) {
	# your algo
	return (new_array)
}


Exemples d’utilisation :
$> ruby exo.rb 1 3 4 2
1 2 3 4

$> ruby exo.rb 10 20 30 40 50 60 70 90 33
10 20 30 33 40 50 60 70 90


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
	

# teste de data pour savoir si c'est int et mettre en int
def Int(l):
	inInt=[]
	try:
		for i in l:
			inInt.append(int(i))
		return inInt
	except:
		print("erreur")
		sys.exit()

# On trie toute la nouvelle liste avec le classique tri a bulle:
def tri_a_bule(l):
    n = len(l)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
    return l


# Affichage des resultats et remétentan les parametre en str à l'aide d'une boucle for:
def final (l):
	inStr=[]
	for i in l:
		inStr.append(str(i))
	reponse= " ".join(inStr)
	print(reponse)

# Appelle des fonctions:
list1=input_data()
list2=Int(list1)
list3=tri_a_bule(list2)
final(list3)


