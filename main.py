'''a, b = map(int, (input().split()))
print(a + b, a - b, a * b, sep='\n') # первая задача

n = input()
print(n[-1]) # вторая задача

mas = list(map(int, input().split()))
n = len(mas)
p = 1
for i in range(len(mas)):
    p *= mas[i]
print(p**(1/n)) # третья задача

f = open('input.txt')
mas = f.readlines()
mas[0] = mas[0].split()
if mas[1] == '*':
    summ = int(mas[0][0])
    for i in range(1, len(mas[0])):
        summ *= int(mas[0][i])
elif mas[1] == '+':
    summ = int(mas[0][0])
    for i in range(1, len(mas[0])):
        summ += int(mas[0][i])
elif mas[1] == '-':
    summ = int(mas[0][0])
    for i in range(1, len(mas[0])):
        summ -= int(mas[0][i])
g = open('output.txt', 'w')
g.write(str(summ))

# четвертая задача

N = input()
b = int(input())
c = int(input())
n = 0
for i in range(len(N)):
    n += int(N[-i - 1]) * (b ** i)
s = ''
while n > 0:
    s = str(n % c) + s
    n = n // c
print(s)

# задача 5
'''

mas = list(map(int, input().split()))
s = (mas[0] + 1) * mas[0]/2
print(sum(mas) - 2*mas[0])






















