# Create variable of type String
from typing import FrozenSet


string_is = 'String'
print(string_is)
print(type(string_is))

#Create variable of type Integer
integer_is = 5
print(integer_is)
print(type(integer_is))

#Create variable of type Float
float_is = 5.0
print(float_is)
print(type(float_is))

#Create variable of type Bytes
bytes_is = bytes('ghjgjghjhg','UTF-8')
print(bytes_is)
print(type(bytes_is))

#Create variable of type List
list_is = ['JavaScript', 'Python', 'C++', 'C#', 'PHP']
print(list_is)
print(type(list_is))

#Create variable of type Tuple
tuple_is = (integer_is, "sdfsdf", (3, 'a'))
print(tuple_is)
print(type(tuple_is))

#Create variable of type Set
set_is = {'String', 'Integer', 'Float','Bytes', 'List','6'}
print(set_is)
print(type(set_is))

#Create variable of type  Frozen set
frozenSet_is = frozenset({"apple", "banana", "cherry"})
print(frozenSet_is)
print(type(frozenSet_is))


#Create variable of type Dict
dict_is = dict(name='Nata', age=39)

test_dict = dict()

test_dict["name"]="Nata"
dict_is['age'] = 18

print(test_dict)

print(dict_is)
print(type(dict_is))


# Create 2 String variables, create a variable  which you sum these variables in. Output to the console.
x = 'Hello'
y = 'World!'
print(x + ' ', y)

# Create 2 Integer variables, create a variable  which these variables are summed in. Output to the console
a =13
b = 7
result_1 = a + b
print(result_1)

result_2 = a // b
print(result_2)

result_3 = a * b
print(result_3)

result_4 = a % b
print(result_4)
