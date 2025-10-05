import numpy as np



mas = list(map(str, input().split('student_')))[1:]
num = []
summ = []
for i in range(len(mas)):
    num.append(mas[i][:3])
    summ.append(int(mas[i][3:]))
print(num)
print(summ)
maxi = max(summ)
for j in range(len(mas)):
    if summ[j] == maxi:
        print(num[j], end=" ")
# задача 1


n, l = map(int, input().split())
k = 2 * np.pi * n
if k * 1000 % 10 >= 5:
    k = (k * 100 + 1) // 1 / 100
else:
    k = (k * 100) // 1 / 100
p = np.pi * (n ** 2) / (l ** 2) * 100
if p * 1000 % 10 >= 5:
    p = (p * 100 + 1) // 1 / 100
else:
    p = (p * 100) // 1 / 100
print(f"Длина окружности равно {k}. Площадь круга составляет {p} % от площади квадрата")
# задача 2


s1, s2 = map(str, input().split())
s3 = s1[1] + s1[0] + s1[2:]
s4 = s2[1] + s2[0] + s2[2:]
print(s3, s4, sep="-")
# задача 3


s = input()
cnt = 0
for i in range(min(4, len(s))):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        cnt += 1
if len(s) >= 4:
    if cnt >= 3:
        print(s.upper())
    else:
        print(s)
else:
    print(s)
# задача 4


t = input()
s = input()
tag = ['a', 'abbr', 'b', 'body', 'caption', 'cite', 'code', 'div', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'i', 's']
if t in tag:
    print(f"<{t}>{s}</{t}>")


s = input()
if len(s) <= 2:
    print(ord(s[0]))
elif len(s) < 10:
    print(ord(s[0]), ord(s[(len(s) - 1) // 2]), ord(s[-1]))
else:
    print(ord(s[-1]))

''' Спасибо интернету за поиск функции, позволяющей выводить номер элемента в таблице аски 
задача 6
'''

