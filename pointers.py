#integer - are immutable - can change the pointer position but cannot change the location of the integer once it is created
num1 = 11 # creating an integer 11 somewhere in the memory and pointing the variable num1 to that location
num2 = num1 # num2 is pointing to the same location as num1 in the memory

print("Before num2 value is updated:")
print("num1", num1)
print("num2",num2)

print("num1 is pointing to the location:", id(num1))
print("num2 is pointing to the location:", id(num2))

num2 = 22 # an integer 22 is created in another memory location and num2 points to that location

print("After num2 value is updated:")
print("num1", num1)
print("num2",num2)

print("num1 is pointing to the location:", id(num1))
print("num2 is pointing to the location:", id(num2))

#dictionary

dict1 = {'value' : 11}
dict2 = dict1 # dict2 points to the same location as dict1

print("Before value is updated:")
print("dict1", dict1)
print("dict2",dict2)

print("dict1 is pointing to the location:", id(dict1))
print("dict2 is pointing to the location:", id(dict2))

dict2['value'] = 22

print("After value is updated:")
print("dict1", dict1)
print("dict2",dict2)

print("dict1 is pointing to the location:", id(dict1))
print("dict2 is pointing to the location:", id(dict2))

