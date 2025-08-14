# Bucles

## Ejercicio 1
``` 
INICIO
    LEER peso_avion
    LEER peso_combustible
    LEER peso_carga
    
    peso_total ← peso_avion + peso_combustible + peso_carga
    
    SI peso_total <= 10 TON ENTONCES
        MOSTRAR "La aeronave está lista para despegar"
    SINO
        MOSTRAR "Debe reducir carga o combustible"
    FIN SI
FIN
```
![Diagrama](/imagenes/DiagramadeBucle4.jpg)

# Bucle

## Ejercicio 2
```
INICIO
    LEER nivel_combustible   // en porcentaje
    tiempo ← 0               // en minutos
    
    MIENTRAS nivel_combustible >= 10 HACER
        tiempo ← tiempo + 1
        LEER nivel_combustible
    FIN MIENTRAS
    
    MOSTRAR "Tiempo total de operación: ", tiempo, " minutos"
FIN
``

![Diagrama](/imagenes/DiagramadeBucle5.jpg)