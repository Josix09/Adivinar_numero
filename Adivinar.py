#input
import random

usu=int(input("digite su número: "))

#processing

maq=random.randint(1,100)

i=1

while usu!=maq:

    if usu<maq:
        print("fallaste, el número a adivinar es mayor, intenta de nuevo")
        usu=int(input("digite su número: "))
        i=i+1

    else:
        print("fallaste el número es menor, intenta de nuevo")
        usu=int(input("digite su número: "))
        i=i+1


if usu==maq:
    print("adivinaste, te tomó: " +str(i)+    " intentos")




    

