edad_cliente = int(input("Ingrese la edad del cliente: "))

if edad_cliente < 4:
    precio_entrada = 0  # Menores de 4 años entran gratis
elif 4 <= edad_cliente <= 18:
    precio_entrada = 5  # Clientes de 4 a 18 años pagan $5
else:
    precio_entrada = 10  # Clientes mayores de 18 años pagan $10

print("El precio de la entrada es: ${}".format(precio_entrada))
