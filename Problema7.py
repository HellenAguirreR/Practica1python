numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("\nSeleccione una opción:")
print("1. Mostrar suma")
print("2. Mostrar resta (el primero menos el segundo)")
print("3. Mostrar multiplicación")
opcion = input("Ingrese el número de la opción deseada (1, 2, o 3): ")

if opcion == '1':
    resultado = numero1 + numero2
    print("La suma es:", resultado)
elif opcion == '2':
    resultado = numero1 - numero2
    print("La resta es:", resultado)
elif opcion == '3':
    resultado = numero1 * numero2
    print("La multiplicación es:", resultado)
else:
    print("Opción no válida. Por favor, seleccione 1, 2, o 3.")
