'''
Créez un programme qui affiche le contenu d’un fichier donné en argument.


Exemples d’utilisation :
$> cat a.txt
Je danse le mia
$> ruby exo.rb “a.txt”
Je danse le mia


Afficher error et quitter le programme en cas de problèmes d’arguments ou de fichier inaccessible.

'''

import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l) !=1:
      print("erreur")
      sys.exit()
    else:
        name=" ".join(l)
        return name

# Lecture et affichage du contenu fichier + test d'érreurs :
def reader(name):
    try:
        fichier = open(name, "r")
        print (fichier.read())
        fichier.close()
    except:
        print("error")

# Appels des fonctions: 
name=input_data()
reader(name)


