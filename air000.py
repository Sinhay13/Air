'''
Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).

Votre programme devra utiliser une fonction prototypée comme ceci :
ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
	# votre algorithme
	return (tableau)
}


Exemples d’utilisation :
$> python exo.py “Bonjour les gars”
Bonjour
les
gars

Afficher error et quitter le programme en cas de problèmes d’arguments.

'''
import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l)<1:
      print("erreur")
      sys.exit()
    return l

#On fais une boucle for pour afficher le resultat: 
def afficher_liste(list):
    for i in list:
        print(i)


#appel des fonctions:
l=input_data()
afficher_liste(l)

# integret le separateur !!!!