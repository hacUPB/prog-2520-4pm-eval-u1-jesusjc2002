'''
1
12
123
124
12345

i                 j
1 hasta n         1 hasta i
'''
numero = int(input("Ingrese el numero entero posotivo: "))

for i in range(1, numero + 1):
    for j in range(1, numero + 1):
        for j in range(1, i+1):
            print(i,end=' ')
        print()
