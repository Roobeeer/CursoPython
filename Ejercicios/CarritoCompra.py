comidas  = []
precios = []
total = 0
while True:
    comida = input("Introduce los alimentos(q to quit)")
    if comida.lower() == "q":
        break
    else:
        precio = float(input(f"Introduce el precio de {comida}: "))
        comidas.append(comida)
        precios.append(precio)

print("--- TU CARRITO ---")
for x in comidas:
    print(x,end = " ")

for y in precios:
    total += y

print()
print(f"Tu precio total es : {total}€")

