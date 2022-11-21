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

#Partition:
def partition(l):
    pivot=l[-1]
    ptr=0
    for i in range(p,r):
        if l[i]<=pivot:
            l[i],l[ptr]=l[ptr],l[i]
            ptr+=1
    l[ptr], l[r]= l[r],l[ptr]
    return l[ptr]

    





# QuickSort:
def quicksort(p=0,r=-1,l=[1]):
    if len(l)==1:
        return l
    if p<r:
        pi=partition(p,r,l)
        quicksort(p,pi-1,l)
        quicksort(pi+1,r,l)
    return l

        



# appell des fonctions:
l=input_data()
l=test_erreur(l)
l=quicksort(l)
print(l)
