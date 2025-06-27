#Écrivez un programme qui demande à l'utilisateur un nombre entier positif et calcule sa factorielle.
#La factorielle de n (notée n!) est le produit de tous les entiers de 1 à n.
#Par exemple, 5! = 5 × 4 × 3 × 2 × 1 = 120.

n = int(input("Rentrer un nombre : "))
r= 1
for n in range(1, n+1):
    r = r*n

    print(r)