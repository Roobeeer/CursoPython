#Devuelve los datos introducidos en forma de String
name = input("What is your name?")
age = input("How old are you?") #tambien podemos hacer el casting de int dentro de la funcion int(input("how old are you"))
age = int(age)
age +=1
print(f"Hello {name}, you are {age} years old")