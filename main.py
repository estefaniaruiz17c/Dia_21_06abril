# Gestión y generación de calendarios
print("Gestión y generación de calendarios")

import calendar

print()
# Crearemos un calendario del año 2001 completo
print("Calendario año 2001 completo")

print()
# Creación de la variable del año 2001
year2001 = 2001
# Uso de la función prcal que imprime el calendario de todo el año indicado
print("- Forma 1:")
calendar.prcal(year2001)


print()
print("- Forma 2:")
# Uso de la función prcal que imprime el calendario de todo el año indicado, pero lo mostraremos en forma diferente a la anterior
# w=0, l=0, c=6, m=3; respectivamente, indican: el ancho entre dos columnas, linea en blanco entre dos filas, espacio entre dos meses y número de meses por fila. Esta es la forma que sal por defecto al usar prcal
# En este caso, cambiaremos las dimensiones anteriores por: w=2, l=1, c=10, m=6

calendar.prcal(year2001, w=1, l=2, c=10, m=3)

print()
# Ahora imprimiremos solamente un mes de este mismo año usando prmonth. En el argumento de esta función, se de primero el año y de segundo, el mes que se quiere mostrar
print("- Marzo del año 2001")
print()
calendar.prmonth(year2001,3)

print()

# Ahora veremos el mismo mes de marzo del 2001 pero empezando desde el día miércoles usando TextCalendar y firstweekday()
print()

# Mostraremos el mes de marzo anterior, pero comenzando desde eldía miércoles
print("- Marzo del año 2001 iniciando desde el día miércoles")
print()
# Ahora imprimiremos solamente un mes de este mismo año usando prmonth. En el argumento de esta función, se de primero el año y de segundo, el mes que se quiere mostrar
marzo_mierco = calendar.TextCalendar(firstweekday=2)
# Ahora para hacer el calendario con la condición anterior utilizamos el método formatmonth() que retorna un string multi-línea con el calendario del mes indicado
calend_marzo_mierco = marzo_mierco.formatmonth(year2001, 3)
print (calend_marzo_mierco)

# Otra forma de hacer que un calendario comience desde otro día de la semana es con TextCalendar() y formatmonth()
print("\n- TextCalendar() y formatmonth() para el mes de marzo de 2001 iniciando desde el dia sábado: ")
print()
calen = calendar.TextCalendar(calendar.SATURDAY)

calend_marzo_sabad = calen.formatmonth(2001,3)

print (calend_marzo_sabad)

# Métodos para usar en el calendario
print("\nMétodos de calendario\n")

# iterweekdays(): retorna el iterador de los días de la semana. El número 0 corresponde al día lunes, el número 1 corresponde al día martes, el número 2 corresponde al día miércoles, el número 3 corresponde al día jueves, el número 4 corresponde al día viernes, el número 5 corresponde al sábado y el número 6 corresponde al día domingo
print("\n- iterweekdays():")

# Este será para iterar los días de la semana empezando por el lunes
print("\nIteración empezando por el día lunes\n")

# Creación de la variable y del ciclo for para el recorrido del iterador
calend_iter_1 = calendar.Calendar()
for i in calend_iter_1.iterweekdays():
    print(i)
print()

# Este será para iterar los días de la semana empezando por el viernes, imprimiéndolos de manera horizontal
print("\nIteración empezando por el día viernes impreso de forma horizontal\n")

# Creación de la variable y del ciclo for para el recorrido del iterador
calend_iter_2 = calendar.Calendar(firstweekday = 4)
for i in calend_iter_2.iterweekdays():
    print(i, end=" ")
print()

# monthdatescalendar(): retorna una lista de las semanas de un mes específico de un año dado 
print("\n- monthdatescalendar() del año 2020, del mes de julio:\n")

# Creación de la variable y uso de monthdatescalendar(), con este, se incluyen algunos días antes del mes indicado, y un día despues apenas finaliza el mes indicado
calend_monthdates = calendar.Calendar()
print(calend_monthdates.monthdatescalendar(2020,7))

# itermonthdates(): iteración de los días de un mes dado en el año indicado, se incluyen algunos días antes del mes determinado, y unos días despues apenas finaliza el mes indicado
print("\n- itermonthdates() del año 2012, del mes de diciembre:")

# Creación de la variable y del ciclo for para el recorrido del iterador
calend_itermonth_1 = calendar.Calendar()
for i in calend_itermonth_1.itermonthdates(2012,12):
    print(i, end="  ,  ")
print()

