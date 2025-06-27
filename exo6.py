n = input("Ecrivez un nombre : ")

if int(n)<= 1:
    print(f"{n} n'est pas premier")

for i in range(2, n):
    if n % i == 0:
        print("N'est pas premier")
print("c'est un nombre premier")


