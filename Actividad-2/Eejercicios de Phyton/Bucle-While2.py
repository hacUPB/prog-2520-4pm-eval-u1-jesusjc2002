
# Utilizamos una variable tipo booleana -> una bandera 
# control = True


while control == True:
    print("1. Entradas\n2.  Platos fuertes\n3.  Bebidas" \
    "\n4.  Postres\n5. Salir ")
    opcion = int(input("Elija una opcion: "))
    match opcion:
       case 1:
          print("1. Patocna con salchichon")
          print("2. salchi papa")
          print("3. yuca con Guinepo")
          opc1 = int(input("Ingrese su elleccion: "))
       case 2:
          print("1. Bistec a caballo" )
          print("2. Chuleta valluna")
          print("3. Pollo a la plancha")  
       case 3:
          print("1. bandeja pasiada")
          print("2. carne asada")
          print("3. pescado frito")
       case 4:
          print("1. Limonada")        
          print("2. Jugo de mango")
          print("3. Jugo de maracuya")    
       case 5:
          control = False
       case _:
            print("Opcion no valida")
            print()