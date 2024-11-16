#List = [] ordenado y mutable
# Set = {}  no ordenados e inmutables
# Tupla = () ordenados e inmutables

#fruit = ["apple","orange","banana","coconut"]
#print(dir(fruit)) ##muestra losmetodos que podemos emplear
#print(help(fruit)) ##muestra la descripción de los metodos que podemos emplear
#fruit.append("pineapple")
#fruit.remove("apple")
#fruit.insert(0,"orange")
#fruit.sort()
#fruit.reverse()
#fruit.clear()
#print(fruit.index("orange"))
#print(fruit.count("orange"))
#fruit[0] = "pineapple"
#for x in fruit:
 #   print(x)

#for x in fruit:
 #   print(x)

 #En el set, se ordenan aleatoriamente siempre y son inmutables pero podemos añadir y quitar. No duplicados
#cars = {"mazda", "ferrari", "lambo", "ford"}
#cars.add("audi")
#cars.remove("audi")
#cars.pop() #elimina el primer elemeto pero será random

#for x in cars:
  #  print(x)


  #TUPLAS ORDENADAS E INCAMBIABLES. Pueden haber valores duplicados y son más rapdios
cars = ("mazda", "ferrari", "lambo", "ford")
#SOLO HAY 2 METODOS
print(cars.index("mazda"))
print(cars.count("mazda"))
for x in cars:
    print(x)