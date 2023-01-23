# Introduction to python data structures.
# Variables-- multiple assignment
a, b, c = 5, 6, 7
# print(a, b, c)

# tuple
my_data = (1, "Denzel", [11, 12, 13])
# print(my_data[1][2])
# Changing the mutable items inside the tuple
my_data[2][1] = 20
# print(my_data)

# Dictionaries
a = {1:"Hi", 2:"Denzel", "age":21}
print(a[1], a["age"])