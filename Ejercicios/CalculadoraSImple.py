number1 = float(input("Introduce number1 "))
number2 = float(input("Introduce number2 "))
print("Select your option\n1. ADD\n2. SUB\n3. MUL\n4. DIV\n5. Exit")

numero = int(input("Select your option: "))
resultado = 0;
if numero == 1:
    resultado = number1+number2
    print(f"Resultado : {resultado}")
elif numero == 2:
    resultado = number1-number2
    print(f"Resultado : {resultado}")
elif numero == 3:
    resultado = number1*number2
    print(f"Resultado : {resultado}")
elif numero == 4:
    if(number2 == 0):
        print("Error, el denominador no puede ser == 0, introduce otro de nuevo")
        numero3 = float(input("Introduce otro nuevo"))

elif numero == 5:
    print("Exit")

