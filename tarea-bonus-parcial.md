```
Inicio
Leer dia_nacimiento, mes_nacimiento, año_nacimiento, dia_actual, mes_actual, año_actual
Si dia_actual < dia_nacimiento
    dia_actual = dia_actual + 30
    mes_actual = mes_actual - 1
Fin Si
dias = dia_actual - dia_nacimiento
Si mes_actual < mes_nacimiento
    mes_actual = mes_actual + 12
    año_actual = año_actual - 1
Fin Si
meses = mes_actual - mes_nacimiento
años = año_actual - año_nacimiento
dias_vividos = (años * 365) + (meses * 30) + dias
Escribir "Edad: ", años, " años, ", meses, " meses, ", dias, " días"
Escribir "Has vivido: ", dias_vividos, " días"
Si dia_nacimiento = dia_actual Y mes_nacimiento = mes_actual Entonces
    Escribir "¡Feliz cumpleaños!"
Fin Si
Fin
```