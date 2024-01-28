monto_consumo = float(input("Ingrese el monto total de su consumo en el restaurante: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

propina = (porcentaje_propina / 100) * monto_consumo

print("La cantidad de propina recomendada es: ${:.2f}".format(propina))
