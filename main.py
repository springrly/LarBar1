# 1. арифметика
from operator import index

print("1. Арифметика")
import math

a = int(123)
b = float(213)

print(a + b, a - b, a * b, a / b, type(a / b))


print("1.1. Круг")

r = 5
s_krug = math.pi * (r^2)
print("Площадь круга: ", round(s_krug, 2))

# 2. работа со строками

print("2. Работа со строками")

text = " Hello Python! "

t1 = text.strip().replace('!', "?").upper()
t2 = t1.lower().strip()
# assert t2 == 'hello python!'
print(t1, t2)

# списки
import copy
print("2. Списки")

numbers = [7,2,5]
numbers.append(4)
numbers.insert(1, 10)
numbers.extend([1,1,1])
numbers.remove(7)
n1 = numbers.pop()
numbers.sort()
numbers.reverse()
numbers.count(2)
d = numbers.index(1)
e = numbers.copy()
copy.deepcopy(numbers)
numbers.clear()
print(numbers, e)

# кортежи
print("4. Кортежи")
t = (1,2,3)
try:
    t[1] = 100
except TypeError:
    print("Error 1")

print(t)

t2 = (4,5)

t3 = t + t2
print(t3, t2.count(3), t2.index(4))

# Множества
print('5. Множества')
values = [3, 1, 3, 2, 1, 5, 2]

unique_values = set(values)
print(unique_values, len(unique_values), len(values) != len(set(values)))

other = {2, 4, 5}

v1 = unique_values & other
v2 = unique_values | other
v3 = unique_values - other
v4 = other - unique_values
print(v1, v2, v3, v4)


# 6. Словари
print("6. Словари")

scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
scores.get("Dave")
scores.pop("Alice")
assert "Alice" not in scores
scores.keys()
scores.values()

print(scores, scores.get("Bob"), scores.get("Dave"), len(scores), scores.keys(), scores.values())





print("7. Комбинированное задание")

text5 = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
text3 = text5.strip()
text3 = text3.lower()
text3 = text3.replace("!", ".")
text3 = text3.split('.')

print(text3)

text3[0] = text3[0].split(' ')

def clean_text(txt):
    txt = txt.strip()
    txt = txt.lower()
    txt = txt.replace('!', '.   ')
    txt = txt.replace('.', '')
    print(txt)

text4 = text3[0].count('python')
bruh = {}
for i in text3[0]:
    bruh[i] = text3[0].count(i)
text3[0] = '-'.join(text3[0])

print(text3[0], text4, text3[0].startswith('python'), text3[0].startswith('python'), len(text3[0]), text3[0].count('a'), text3[0].find("data"))
print(bruh)
print(text3[0])
clean_text(text5)