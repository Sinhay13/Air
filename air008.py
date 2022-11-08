'''
Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”.

Utilisez une fonction de ce genre (selon votre langage) :
sorted_fusion(array1, array2) {
	# your algo
	return (new_array)
}


Exemples d’utilisation :
$> ruby exo.rb 10 20 30 fusion 15 25 35
10 15 20 25 30 35


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

# On range ne donner a notre covenance:
def organisateur(l):
    t1=[]
    t2=[]
    n=0
    N=len(l)
    z=len(l)
    while n<N:
        if l[n] == "fusion":
            z=n
            n+=1
        elif l[n]!="fusion" and n<z:
            t1.append(l[n])
            n+=1
        elif l[n]!="fusion" and n>z:
            t2.append(l[n])
            n+=1
    return t1, t2


# teste de data pour savoir si c'est int et mettre en int
def Int(l):
	inInt=[]
	try:
		for i in l:
			inInt.append(int(i))
		return inInt
	except:
		print("erreur")
		sys.exit()

# On trie toute la nouvelle liste avec le classique tri a bulle:
def tri_a_bule(l):
    n = len(l)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]
    return l

# On trie et on fusione !
def sorted_fusion(t1,t2):
    for i in t1:
        t2.append(i)
    t3=tri_a_bule(t2)
    return t3

# Affichage des resultats et remétentan les parametre en str à l'aide d'une boucle for:
def final (l):
	inStr=[]
	for i in l:
		inStr.append(str(i))
	reponse= " ".join(inStr)
	print(reponse)


#Appels des fonction :
l=input_data()
tab1,tab2=organisateur(l)
tab1_int=Int(tab1)
tab2_int=Int(tab2)
tab3=sorted_fusion(tab1_int,tab2_int)
final(tab3)


