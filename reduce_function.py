from functools import reduce
import statistics

# Example 1, calculate avg

data = [
    ('Colombia',5.7),
    ('Argentina',4.3),
    ('Paraguay',3.6),
    ('Canada',6.1),
    ('Chile',5.4)
]

values = [n[1] for n in data]
adition = lambda x , y: x + y

sum = reduce(adition,values)
avg = sum / len(values)
avg_2 = statistics.mean(values)
print(avg)
print(avg_2)

# other way without using reduce

total = 0
for x in values:
    total = total + x

print(total)