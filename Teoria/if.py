age = int(input("Enter your age:"))
if age < 0:
    print("Sorry, the age should be positive")
elif age>18:
    print("Sorry, the age should be lower than 18")
    if age >=100:
        print("You are too older")

#hay que tener en cuenta el orden de los ifs, porque pueden dar otros resultados

