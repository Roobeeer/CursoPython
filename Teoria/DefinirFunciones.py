def happy_birthday(name,age):#el orden de los parametros importa
    print(f"Happy Birthdya to {name}, you are {age} years old")

def display_invoice(name,amount,due_date):
    print(f"Hello {name}")
    print(f"Your bill of {amount:.2f}€ is due : {due_date}")

happy_birthday("Rober",19)
display_invoice("Rober",19,"01/01")