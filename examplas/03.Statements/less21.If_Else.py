print("~~~~~~Generate Password~~~~~")
name = input("What is your name ? ")
print("Your password is: ")
if name == "Max":
    print(len(name) + len(name)**10)
else:
    print("123456")

print("Hope use it wisely.....")