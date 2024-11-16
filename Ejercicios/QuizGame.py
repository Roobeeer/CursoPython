import math

(questions) = (("Cuántos elementos tiene la tabla periódica?"),
             ("Cuál es el gas más abundante en la Tierra?"),
             ("Cuántos huesos hay en el cuerpo humano?"))

options = (("A. 116 ","B. 117","C. 118 "),
           ("A. Hidrógeno ","B. Oxígeno","C. Nitrógeno "),
           ("A. 205","B. 206 ","C. 207 "))

answers = ("C","A","B")
guesses = []
question_num = 0
score = 0

for question in questions:
    print(question)
    print("------------------------------------------")
    for option in options[question_num]:
        print(option)
    guess = input("Introduce la respuesta correcta (A,B,C)").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECTO")
    else:
        print("INCORRECTO")
        print(f"La respuesta correcta era la {answers[question_num]}")
    question_num += 1


print("-------------------------------------")
print("             RESULTADOS              ")
print("-------------------------------------")
print(f"Tus marcas : ", end  = " ")
for x in guesses:
    print(x, end = " ")


print(f"\nOpciones correctas : ", end = " ")
for y in answers:
    print(y, end = " ")

score = math.ceil((score/(len(questions)))*100)

print(f"\nPuntuación : {score}%")

