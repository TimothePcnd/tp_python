p = input("Ecrivez une phrase : ")

c = 0
v = 0

voyelle = ['a','e','i','o','u','y']
consonne = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

for l in p:
    if l in voyelle:
        v+=1

    if l in consonne:
        c+=1

print(f"Dans la phrase vous avez {v} de voyelles et {c} de consonnes")