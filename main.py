# Python basics

# Some basic data types:
int_var = 1                   # an int
float_var = 5.0               # a floating point number
string_var = "string"         # a string - piece of text
boolean_var = True            # boolean (True or False)

# print function
input("Printing variables!")
print(int_var)
print(float_var)
print(string_var)
print(boolean_var)

# Collections - multiple values in the same variable

input("List: multiple values in order")
list_var = [1, 2, 3, 3, 3, 4]
input(list_var)
list_var.append(5)
input(list_var)
list_var.remove(1)
input(list_var)
list_var[1] = 10
input(list_var)

for v in list_var:
    pass

input("Set: multiple unique values")
set_var = {1, 2, 3, 3, 3}
input(set_var)
set_var.add(3)
input(set_var)
set_var.add(4)
input(set_var)

input("1 in set_var?")
print(1 in set_var)

for v in set_var:
    pass

input("Dict: association between keys and values")
dict_var = {"a": 1, "b": 2, "c": 3}
input(dict_var)
dict_var["d"] = 4
input(dict_var)
input("'a' in dict_var?")
print('a' in dict_var)
input("'z' in dict_var?")
print('z' in dict_var)

for k in dict_var:
    pass

for k, v in dict_var.items():
    print(k, v)

input("Operators...")
input("5 + 2")
print(5+2)

input("5 - 3")
print(5-3)

input("5 * 4")
print(5*4)

input("20 / 4")
print(20 / 4)

input("2 ** 3")
print(2 ** 3)

input("5 > 4")
print(5 > 4)

input("(2 * 10) == (4 * 5)")
print((2 * 10) == (4 * 5))

print("5 != 4")
print(5 != 5)

input("Control structures...")


input("IF statements")
if 4 > 3:
    print("This is printed...")
else:
    print("This is not!")

input("WHILE loops")
i = 0
while i < 10:
    print(i)
    i = i + 1

input("FOR loops")
for i in range(10):
    print(i)


input("Functions...")

def function(a, b, c)
    return a + b * c

