cantidad_payasos = int(input("Ingrese el número de payasos vendidos: "))
cantidad_muñecas = int(input("Ingrese el número de muñecas vendidas: "))

peso_payaso = 112  # en gramos
peso_muñeca = 75  # en gramos

peso_total = (cantidad_payasos * peso_payaso) + (cantidad_muñecas * peso_muñeca)

print("El peso total del paquete a enviar es: {} gramos".format(peso_total))
