print("~~~Number aggregation~~~")
# result = 1+2+3+4....
num = input("Enter a number: ")
result = 0
i = 1

while i <= int(num):
 #   result = result + i
 result += i
 #   i = i + 1
 i += 1


print("The sum is :", result)
