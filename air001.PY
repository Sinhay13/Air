'''
Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.

Votre programme devra intégrer une fonction prototypée comme ceci :
ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
	# votre algorithme
	return (tableau)
}


Exemples d’utilisation :
$> python exo.py 'Crevette magique dans la mer des étoiles' 'la'
Crevette magique dans 
 mer des étoiles

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l)!=2:
      print("erreur")
      sys.exit()
    return l

# On recupere la phrase, et on la coupe, et on affiche le resultat avec une boucle for:
def split(l):
    phrase= l[0]
    phrase_final=phrase.split(l[1])
    for i in phrase_final:
        print(i)

#Appel des fonctions:
list=input_data()
split(list)