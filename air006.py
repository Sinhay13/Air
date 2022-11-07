'''
Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.

Utilisez une fonction de ce genre (selon votre langage) :
ma_fonction(array_de_strings, string) {
	# votre algorithme
	return (nouvel_array_de_strings)
}


Exemples d’utilisation :
$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “t”
Michel

$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “a”
Michel, Thérèse, Benoit



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

# On range les elements du data:
def orguanisateur(l):
	string=l[-1]
	del l[-1]
	return l, string

# On compare caraterére par carectére : 
def comparateur (word, string):
	for i in range(len(word)):
		if word[i].lower()== string:
			return False
		else:
			return True 
	


# on recherche les mots a suprimer et on les suprimes:
def inspecteur(string,l):
	lf=[]
	for word in l:
		if comparateur(word, string)== True:
			lf.append(word)
	print(lf)
	

	
				



# Appel des fonctions:

list= input_data()
list, string=orguanisateur(list)
print(list)
print(string)
inspecteur(list,string)

