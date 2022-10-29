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


# on fais un tri a bule pour oguaniser la liste: 
def tri_a_bule(l):
    n = len(l)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
    return l


# on compare une valeur apres l'autre:
    def compare (lt):
        ld=[]
        N=len(lt)
        n=0
        i=0
        I=len(lt)
        while n<N:
            if lt[n]==lt[n+1]:
                ld.append(lt[n])
                n+=1
            else:
                n+=1
        return ld

# on affiche les valeurs en double:
def resultat (ld):
    for i in ld:
        print(i)


