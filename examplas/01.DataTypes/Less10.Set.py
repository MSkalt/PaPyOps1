nums_list = [1,2,3,3]
nums_set = {1,2,3,3}

print(nums_list)
print(nums_set)

# cars = {"Toyota","Mazda", "Fiat"}
# print(cars)

# print(len(cars))
#
# cars.remove("Fiat")
# print(cars)
#
# cars.remove("Fiat")
# cars.discard("Fiat")
# print(cars)
#
# cars.pop()
# print(cars)
# cars.clear()
# print(cars)
#
# del  cars
# print(cars)

cars = {"Toyota","Mazda", "Fiat"}
print(cars)
cars_new = {"Mitsubishi", "BMW", "Fiat"}
print(cars_new)
cars_full = cars.union(cars_new)
print(cars_full)
print(cars.difference(cars_new))
