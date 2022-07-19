cars = ["Toyota", "Mazda", "Subaru"]
newcar = "Honda"
cars_empty = []

print(cars)
print(cars_empty)

print(cars[1])

cars[1] = "Mitsubishi"
print(cars)

nums = [1,4,2,5]
print(nums)
print(nums[0] + nums[3])


print("~~~~ Append ~~~~~")
cars.append(newcar)
print(cars)

print("~~~~ Insert ~~~~~")
cars.insert(1, newcar)
print(cars)

print(cars.index("Mitsubishi"))

print("~~~~ pop ~~~~~")
print(cars.pop())
print(cars)

print("~~~~ Remove ~~~~~")
cars.remove("Toyota")
print(cars)

print("~~~~ Sorting ~~~~~")
cars.insert(len(cars), newcar)
cars.insert(0, "Toyota")
print(cars)
cars.sort()
print(cars)