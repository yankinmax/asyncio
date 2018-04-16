import random

numbers = []
numbers_size = random.randint(10, 15)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))
#print(numbers)

numbers.sort()
print(numbers)

half_size = int(len(numbers) / 2)

if (numbers_size % 2) != 0:
    print(numbers[half_size])
else:
    print(sum(numbers[half_size - 1:half_size + 1])/2)

import statistics

print(statistics.median(numbers))