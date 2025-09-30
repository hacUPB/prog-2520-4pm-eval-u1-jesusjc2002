'''
numero = 1
while numero >= 5:
    print(numero)
    numero += 1      
numero = 20
# imrprimrir numeros pares del 20 al 80
while nuemro <= 80:
    if numero % 2 == 0:
         print(numero)
    numero +=  1 
'''

'''
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

if num1 > num2:
    mayor = num1 
    menos = num2
else:
    mayor = num2
    menos = num1

while menos <= mayor:
    if menor % 2 == 1:
        print(menor)
        
     menor += 1   
'''    

# imprimir los multiplos de 7 entre 0 y 100
'''
numero = 100
while numero <= 100:
    if numero % 7 == 0:
        print(numero)
    numero += 1
'''

# Solicitar un numero al usauario e imprimir sutabla de 
# multiplicar hasta 15

numero = int(input("Porfavor ingrese un numero: "))
i = 1
while i <= 15:
    resultado = numero * i  
    print(f"{numero} x {i} = {numero * i}")
    i += 1