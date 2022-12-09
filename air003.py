'''
Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.


Exemples d’utilisation :
$> python exo.py 1 2 3 4 5 4 3 2 1
5

$> python exo.py bonjour monsieur bonjour
monsieur


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

# On passe à int : 
def str_to_int(l):
    l_int=[]
    for i in l:
        l_int.append(int(i))
    return l_int


# on fais un tri par insertion: 
def tri_insertion(l):
    N = len(l)
    for n in range(1,N):
        cle = l[n]
        j = n-1
        while j>=0 and l[j] > cle:
            l[j+1] = l[j] # decalage
            j = j-1
        l[j+1] = cle
    return l



# on affiche la derniere valeur qui la valeur qui n'a pas de per apres verif:
def resultat (l):
    if l[-2]!=l[-1]:
        print(l[-1])
    else:
        print("error")




# appel des fonction:
l=input_data()
l_int=str_to_int(l)
lt=tri_insertion(l_int)
resultat(lt)
