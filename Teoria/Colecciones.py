frutas = ["manzana","naranja","mandarina","platano"]
vegetables = ["lechuga","rabano","tomate","patatas"]
meat = ["pollo","pescado","carne","cerdo"]

junto = [frutas,vegetables,meat]
#Se puede hacer asi tambien  --> junto = [["manzana","naranja","mandarina","platano"],["lechuga","rabano","tomate","patatas"],["pollo","pescado","carne","cerdo"]]

frutas[0] = "piña"
print(junto[1][2]) ## [][] para acceder a cada elemento
for algo in junto:
    for algoalgo in algo:
        print(algoalgo, end = " ")
    print()

