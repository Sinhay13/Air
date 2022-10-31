'''
Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.


Exemples d’utilisation :
$> python exo.py “Hello milady,   bien ou quoi ??”
Helo milady, bien ou quoi ?


Afficher error et quitter le programme en cas de problèmes d’arguments.

'''

import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l)<=1:
      print("erreur")
      sys.exit()
    p=" ".join(l)
    return p

# On recherche les doublons et on les supprime: 
def inspecteur_doublons(p):
    p_l=list(p)
    for i in range(len(p_l)):
        if i+1 < len(p_l):
            if p_l[i]==p_l[i+1]:
                del p_l[i]
        else:
            return p_l

# resultat final:

def resultat (p_l):
   p_f= "".join(p_l)
   print(p_f)

#appel des fonction: 

phrase=input_data()
phrase_list=inspecteur_doublons(phrase)
resultat(phrase_list)

