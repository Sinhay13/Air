'''
Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste.


Exemples d’utilisation :
$> ruby exo.rb 1 2 3 4 5 “+2”
3 4 5 6 7

$> ruby exo.rb 10 11 12 20 “-5”
5 6 7 15


L’opération à appliquer sera toujours le dernier élément.


Afficher error et quitter le programme en cas de problèmes d’arguments.

'''


import sys

# Recuperation du data avec teste d'erreur si pas d'argument
def input_data():
    l = sys.argv[1:]
    if len(l)<=1:
      print("erreur")
      sys.exit()
    else:
        return l

# on recupere le data quon a besion dans les variables qu'on a besion:
def prepa (data):
    coef_ope=data[-1]
    coef=coef_ope[0]
    ope=coef_ope[1:]
    del data[-1]
    return data, coef, ope

# on teste les errors argument pour que ce sois  bien des int et on les transforme en int
def test_argument(data,coef):
    try:
        coef_int=int(coef)
        data_int=[]
        for i in data:
            data_int.append(int(i))
        return data_int, coef_int
    except:
        print("erreur")
        sys.exit()

            
# on verifi l'operateur + on fais les calculs + on les stock dans une nouvelle liste
def calculs (data, coef, ope):
    data_final=[]
    i=0
    n=len(data)
    while i<n:
        if ope=="+":
            data_final.append(str(data[i]+coef))
            i+=1
        elif ope=="-":
            data_final.append(str(data[i]-coef))
            i+=1
        else:
            print("erreur")
            sys.exit()
    return data_final
    

   

# On imprime le resultat
def resultat(data):
    result=" ".join(data)
    print(result)
    

    



#Appel des fonctions:
data=input_data ()
data, ope, coef =prepa(data)
data, coef=test_argument(data, coef)
data_final=calculs(data, coef, ope)
resultat(data_final)
