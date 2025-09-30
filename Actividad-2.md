# Actiividad 2

# Ejercicio 2
Construye un algoritmo que, al recibir como datos el ID del empleado y los seis primeros sueldos del año, calcula el ingreso total semestral y el promedio mensual, e imprime el ID del empleado, el ingreso total y el promedio mensual.

## Solucion
```
Pseudocódigo
Inicio
Leer ID, S1, S2, S3, S4, S5, S6
Total = S1 + S2 + S3 + S4 + S5 + S6
Promedio = Total / 6
Escribir ID, Total, Promedio
Fin
```

![Diagrama1](/imagenes/Ejercicio2.png)


# Ejercicio 3

Un curso se evalúa con 7 notas, conoce 6 notas, las cuales valen el 70% del curso. Se le pide al usuario las primeras 6 notas, y se calcula cuanto debe sacar en la evaluación final para aprobar, minimo, con 3.0.

# Solucion

## Analisis
Variables de entrada: N1, N2, N3, N4, N5, N6 Proceso: Calcular Promedio de N1 a N6, reiniciar 3.0 del Promedio x 0.7 y dividirlo por 0.3 Variables de Salida: Promedio de N1 a N6 y Nota Final
```
Pseudocódigo
Inicio
Leer N1, N2, N3, N4, N5, N6
Promedio = (S1 + S2 + S3 + S4 + S5 + S6) / 6
Nota final = 3.0 - (Promedio * 0.7) / 0.3
Si Promedio > 3.0, Aprobar
Sino, Reprobar
Escribir Promedio, Nota Final, Aprueba o no Aprueba
Fin
```

![Diagrama2](/imagenes/Ejercicio3.png)


# Ejercicio 4

Realice un algoritmo para determinar cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de $85 cada uno; de lo contrario, el precio es de $90. Represéntelo con el pseudocódigo y el diagrama de flujo.

# Solucion

## Analisis
Variables de entrada: Cantidad de Lapices

Variable intermedia: Valor unidad

Proceso: Contar cantidad y aplicar precio

Variables de Salida: Cantidad de Lápices, Precio

```
Pseudocódigo
Inicio
Leer Cantidad_Lapices
Si Cantidad_Lapices >= 1000
    Valor_Unidad = 85
Si no
    Valor_Unidad = 90
Fin si
Costo = Cantidad_Lapices * Valor_Unidad
Escribir "El valor total es:", Costo
Fin 
```

![Diagrama3](/imagenes/Diagramadeflujo1.png)

# Ecercicio 5

Un almacen de compra tiene una promoción: por compras superiores a $250000 se les aplicará un descuento del 15%, de caso contrario, solo se aplicará un 8%. Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar en dicho almacén y de cuanto es el decuento que obtendrá.

# Solucion

## Analisis
Variables de entrada: Valor de compra

Proceso: Aplicar descuento según aplica

Variable de salida: Descuento, Valor Final

```
Pseudocódigo
Inicio
Leer Valor_Compra
Si Valor_Compra > 250000
    Descuento = Valor_Compra * 0.15
Si no
    Descuento = Valor_Compra * 0.08
Fin si
Valor_Total = Valor_Compra - Descuento
Escribir "Valor a pagar:", Valor_Total
Fin
```

![Diagrama4](/imagenes/Ejercicio6.png)

# Jercicio 6

## Analisis
El director de una escuela esta organizando un viaje de estudios, y requiere determinar cuanto debe cobrar a cada alumno y cuanto debe pagar a la compañia de viajes por el servivio. La forma de cobrar es la siguiente: Si son 100 alumnos o más, el costo de cada alumno es de $65.00; de 50 a 99 alumnos, el costo es de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de alquiler del autobus es de $4000.00, sin importar el número de alumnos.

# Solucion

## Analisis
Variables de entrada: Alumnos

Proceso: Aplicar el costo de cada alumno según la cantidad

Variable de salida: Costo de Alumno, Costo Total
```
Pseudocódigo
Inicio
Leer Alumnos
Si Alumnos >= 100
    Costo_Alumno = 65
Si no 
    Si Alumnos >= 50
        Costo_Alumno = 70
    Si no
        Costo_Alumno = 90
    Fin si
Fin si 
```
![Diagrama5](/imagenes/Ejercicio6.png)
