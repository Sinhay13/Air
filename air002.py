'''
Créez un programme qui transforme un tableau de chaînes de caractères en une seule chaîne de caractères. Espacés d’un séparateur donné en dernier argument au programme.

Utilisez une fonction de ce genre (selon votre langage) :
ma_fonction(array_de_strings, separateur) {
	# votre algorithme
	return (string)
}


Exemples d’utilisation :
$> python exo.py 'je' 'teste' 'des' 'trucs' ' '
Je teste des trucs


Afficher error et quitter le programme en cas de problèmes d’arguments.

'''

import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l)<=1:
      print("erreur")
      sys.exit()
    return l


#Creation du'une phrase en prenant le separateur:

def Phrase(l):
	separateur=l[-1]
	list_complete=l
	del list_complete[-1]
	phrase = separateur.join(list_complete)
	print(phrase)


#apelle des fonctions: 

entree= input_data()
Phrase(entree)
