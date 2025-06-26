prenom = input('Votre prénom : ')
nom = input('Votre nom : ')
naissance = int(input('Votre année de naissance : '))
age  = 2025 - naissance

print('Bonjour', prenom.capitalize(), nom.upper(),'vous avez', age, 'ans')