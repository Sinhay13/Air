'''
Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_quick_sort(array) {
	# votre algorithme
	return (new_array)
}


Exemples d’utilisation :
$> python exo.py 6 5 4 3 2 1
1 2 3 4 5 6



Afficher error et quitter le programme en cas de problèmes d’arguments.


Wikipedia vous présentera une belle description de cet algorithme de tri.

'''

import sys

# Recuperation du data avec teste d'erreur si pas asser d'arguments
def input_data():
    l = sys.argv[1:]
    if len(l) <=1:
      print("erreur")
      sys.exit()
    else:
        return l

# test d'erreur pur voir si c'est bien des chiffres et les mettre en int
def test_erreur (l):
    l2=[]
    try:
        for i in l:
            tmp=int(i)
            l2.append(tmp)
        return l2
    except:
        print("erreur")
        sys.exit()

#init des parametres:
def para(l):
    low=0
    high=len(l)-1
    return l, low, high



#Partition:
def partition(l, low, high):
    pivot= l[high]
    i = low - 1
    for j in range(low, high):
        if l[j]<= pivot:
            i+=1
            (l[i],l[j])=(l[j],l[i])
    (l[i+1],l[high])=(l[high],l[i+1])
    return i+1
    

# QuickSort:
def quicksort(l,low,high):
    if low<high:
        pi= partition(l,low, high)
        quicksort(l,low,pi-1)
        quicksort(l,pi+1,high)
    return l

# Affichage de la nouvelle liste
def result(l):
    l_final=[]
    for i in l:
        l_final.append(str(i))
    r=" ".join(l_final)
    print(r)
    
        



# appell des fonctions:
l=input_data()
l=test_erreur(l)
l,low, high=para(l)
l=quicksort(l, low, high)
result(l)
