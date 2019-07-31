import statistics

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