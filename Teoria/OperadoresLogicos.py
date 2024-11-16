#or
#and
#not


temp = int(input("Que temperatura hace?"))
is_raining = input("Is raining?(yes/no)").strip().lower()
if temp > 35 or temp <0 or is_raining == "yes":
    print("La salida se cancela")
else :
    print("La salida no se cancela")