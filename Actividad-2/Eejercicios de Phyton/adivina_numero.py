#import random
from random import randint

#num_aleatorio = random.randit(0,50)
num_aleatorio = randint(1,100)
intento = 0 
numero = -1#obliga al whle a entrar por primera vez

while numero != num_aleatorio:
    numero = int(input("Adivine el numero entre 1 y 100: "))
    intento += 1
    if numero > num_aleatorio:
        print(" Tu numero es mayor")
    elif numero < num_aleatorio:
        print("Tu numero es menor")
    else:
        print("El numero es correcto, adivinaste..")
print(f"Adivinaste en: {intento} intentos")

              