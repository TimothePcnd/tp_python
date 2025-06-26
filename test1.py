#print('tjrs OK')

#x = input('donner une valeur')

#print('tjrs OK, vous avez donné : ', x)

prenom = input('Votre prénom : ')
nom = input('Votre nom : ')
naissance = int(input('Votre année de naissance : '))
age  = 2025 - naissance

print('Bonjour', prenom.capitalize(), nom.upper(),'vous avez', age, 'ans')