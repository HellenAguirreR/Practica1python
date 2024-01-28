hora_input = input("Ingrese la hora en formato HH:MM: ")

hours, minutes = map(int, hora_input.split(":"))

hora_decimal = hours + minutes / 60

rango_desayuno = (7.0, 8.0)
rango_almuerzo = (12.0, 13.0)
rango_cena = (18.0, 19.0)

if rango_desayuno[0] <= hora_decimal <= rango_desayuno[1]:
    print("Es hora de desayunar.")
elif rango_almuerzo[0] <= hora_decimal <= rango_almuerzo[1]:
    print("Es hora de almorzar.")
elif rango_cena[0] <= hora_decimal <= rango_cena[1]:
    print("Es hora de cenar.")
else:
    print("No es hora de comer.")
