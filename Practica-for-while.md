# Bucles

## Ejercicio 1
Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6
años? ¿Qué salario ha recibido en cada uno de los 6 años? Realice el
algoritmo y represente la solución mediante el diagrama de flujo, el
pseudocódigo y el diagrama N/S, utilizando el ciclo apropiado.

## Pseudocodigo

```
Inicio
ano=1
sal=1500
total=0
MIentras ano <= 6:
    Anual = sal *1.1
    sal = anual
    ano = ano +1
    Mostrar anual 
Fin miestras
Mostrar total
Fin
```
![Diagrama](/imagenes/DiagramadeBucle.png)


# Bucles
## Ejercicio 2

Se requiere un algoritmo para determinar, de N cantidades, cuántas
son cero, cuántas son menores a cero, y cuántas son mayores a cero.
Realice el diagrama de flujo, el pseudocódigo y el diagrama N/S para
representarlo, utilizando el ciclo apropiado.

## Pseudocodigo
```
Inicio
    Escribir "Ingrese la cantidad de números (N):"
    Leer N

    contadorPositivos ← 0
    contadorNegativos ← 0
    contadorCeros ← 0

    Para i ← 1 Hasta N Con Paso 1 Hacer
        Escribir "Ingrese el número ", i, ":"
        Leer numero

        Si numero > 0 Entonces
            contadorPositivos ← contadorPositivos + 1
        Sino
            Si numero < 0 Entonces
                contadorNegativos ← contadorNegativos + 1
            Sino
                contadorCeros ← contadorCeros + 1
            FinSi
        FinSi
    FinPara

    Escribir "Cantidad de números mayores a cero: ", contadorPositivos
    Escribir "Cantidad de números menores a cero: ", contadorNegativos
    Escribir "Cantidad de ceros: ", contadorCeros
Fin
```

![Diagrama](/imagenes/DiagramadeBucle2.drawio.png)

# Bucles
## Ejercico 3

Realice el algoritmo para determinar cuánto pagará una persona que
adquiere N artículos, los cuales están de promoción. Considere que
si su precio es mayor o igual a $200 se le aplica un descuento de 15%,
y si su precio es mayor a $100 pero menor a $200, el descuento es de
12%; de lo contrario, sólo se le aplica 10%. Se debe saber cuál es el
costo y el descuento que tendrá cada uno de los artículos y finalmente cuánto se pagará por todos los artículos obtenidos. Represente la
solución mediante el diagrama de flujo, el pseudocódigo y el diagrama N/S.

# Pseudocodigo
```
Inicio
    Escribir "Ingrese la cantidad de artículos (N):"
    Leer N
    total_pagar ← 0

    Para i ← 1 Hasta N Hacer
        Escribir "Ingrese el precio del artículo ", i, ":"
        Leer precio

        Si precio >= 200 Entonces
            descuento ← precio * 0.15
        Sino
            Si precio > 100 Entonces
                descuento ← precio * 0.12
            Sino
                descuento ← precio * 0.10
            FinSi
        FinSi

        precio_final ← precio - descuento
        total_pagar ← total_pagar + precio_final

        Escribir "Artículo ", i, ": Precio = $", precio, ", Descuento = $", descuento, ", Precio final = $", precio_final
    FinPara

    Escribir "Total a pagar por todos los artículos: $", total_pagar
Fin
```