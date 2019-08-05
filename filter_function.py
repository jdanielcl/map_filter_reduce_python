import statistics
import random

data = [
    ('Colombia',5.7),
    ('Argentina',4.3),
    ('Paraguay',3.6),
    ('Canada',6.1),
    ('Chile',5.4)
]
# extraction of values
values = otra_lista = [elem[1] for elem in data]

avg = statistics.mean(values)
print(avg)

l = lambda x: x[1] > avg

# filter function needs a conditional function that returns True or False and
#  the set of data which needs to be evaluated by the function
lista = list(filter(l,data))
countries = [c[0] for c in lista]
print(countries)

# Example #2

countries = ["Colombia","","Brazil","","Venezuela","",""]

valid_countries_list = list(filter(None,countries))

print(valid_countries_list)

# Example #3: even numbers

even = lambda x: x%2==0
odd = lambda x: x%2!=0
numbers = [random.randint(0,30) for _ in range(10)]
print(numbers)
even_numbers = list(filter(even,numbers))
print(even_numbers)
odd_numbers = list(filter(odd,numbers))
print(odd_numbers)
