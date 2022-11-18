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
    if len(l) !=2:
        print("erreur")
        sys.exit()
    else:
        try:
            n=l[1]
            m=l[0]
            n_int=int(n)
            return m, n_int
        except:
            print("erreur")
            sys.exit()

# On fais la pyramide : 
def pyramide(m,n):
    m2=m+m
    print(" "*(n+1)+m)
    for x in range(n):
        m+=m2
        print(' '*(n-x)+m)



# Appel des fonctions: 
m,n=input_data()
pyramide(m,n)



