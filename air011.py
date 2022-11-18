'''
Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre.


Exemples d’utilisation :
$> ruby exo.rb O 5
    O
   OOO
  OOOOO
 OOOOOOO
OOOOOOOOO


Afficher error et quitter le programme en cas de problèmes d’arguments.

'''

import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l) !=1:
        print("erreur")
        sys.exit()
    else:
        try:
            n=" ".join(l)
            n_int=int(n)
            return n_int
        except:
            print("erreur")
            sys.exit()

# On fais la pyramide : 
def pyramide(n):
    m="O"
    print(" "*(n+1)+m)
    for x in range(n):
        m+="OO"
        print(' '*(n-x)+m)



# Appel des fonctions: 
n=input_data()
pyramide(n)



