lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

indices_a_eliminar = [0, 4, 5]
for indice in sorted(indices_a_eliminar, reverse=True):
    del lista_muestra[indice]

print("Resultado esperado:", lista_muestra)
