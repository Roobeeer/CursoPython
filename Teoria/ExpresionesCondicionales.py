#expresiones condicionales son if-else statement(ternarias)

num = 5
a = 6
b = 7
age =14
temperature = 20
user_role = "guest"

print("Positive" if num > 0 else "Negative")
result = "EVEN" if num%2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >=18 else "Child"
weather = "HOT" if temperature>40 else "COLD"

print(result)
print(max_num)
print(min_num)
print(status)
print(weather)
