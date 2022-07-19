a = "Max "
b = "Spiral Solutions"

print(a)
print(b)

print(a + b)
print(a + "" +b)

c = "Max works at 'Spiral solutions' as QA"
print(c)

cc = 'Max works at "Spiral solutions" as QA'
print(cc)

ccc = "Max works at \"Spiral solutions\" as QA"
print(ccc)

print("~~~ Upper / Lower / Lengh ~~~")
greeting = "Hello World"
print(greeting.lower())
print(greeting.upper())
print(len(greeting))
print(greeting.replace('l', '*'))
print(greeting.replace('Hell', '***'))
print(greeting.replace('l', '*', 1))

print("~~~ SubS tring ~~~")
print(greeting)
print(greeting[0])
print(greeting[2])
print(greeting[-1])
print(greeting)
print(greeting[2:5])
print(greeting[2:])
print(greeting * 2)
print(greeting + " Hello my king")
print(greeting [::2])

print("~~~  String formatting  ~~~")
name = "Max"
location = "Kafar Vradim"
contry = "Israel"

output = "Hello my name is " + name + " I live in " + location
print(output)

output = "Hello my name is %s and I live in %s and the contry is %s" %(name, location, contry)
print(output)