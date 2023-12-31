import re
import math
nama = input()

nama = re.sub("[^a-zA-Z]+", "", nama)
nama = nama.lower()
if (len(nama) > 6):
    nama = nama[:6]

def counting_combination(word):
    sum = 0
    for i in range(len(word)+1):
        sum += math.factorial(len(word)) / (math.factorial(len(word)-i) * math.factorial(i))
    return sum

print(counting_combination(nama))
