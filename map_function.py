
a = [1,2,3,4,5]
b = [6,7,8,9,10]

names = ['DANIEL','felipe','SANDRA','oscar','FANNY']

def square(number):
    return number**2

def addition(a,b):
    return a+b

# Map use a function and an interator, send the values accross the function
# and then return the values.
result_square = map(square,a)
print(result_square)

# You can send different numbers of iterators

result_addition = map(addition,a,b)
print(result_addition)

# Also you can use Lambda's functions

capitalize_names = lambda x : x.strip().title()
cleaned_names = map(capitalize_names,names)
print(names)
print(cleaned_names)

initial_letter = lambda x : x.strip().title()[0]
letters = map(initial_letter,names)
print(letters)

print(initial_letter('hello world!'))
