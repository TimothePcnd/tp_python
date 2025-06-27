prenom = input('Votre prénom : ')
nom = input('Votre nom : ')
naissance = input('Votre année de naissance : ')

if naissance.isdigit():
    naissance=int(naissance)
    age=2025-naissance

    print(f"Bonjour {prenom.capitalize()} {nom.upper()}, vous avez {age} ans")

else:
    print(f"{naissance} n'est pas un nombre")