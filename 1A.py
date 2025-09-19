'''
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
m = int(input())
print(fib(m))
# упражнение 1

def mn(n, mas):
    i = 2
    while n > 1:
        if n % i == 0:
            mas.append(i)
            n = n // i
            i = 2
        else:
            i += 1
    return mas
s = []
k = int(input())
print(*mn(k, s))
# упражнение 2

a, b = map(str, input().split())
a = int(a)
for i in range(1, (a + 1) // 2 + 1):
    print(b*i)
for j in range(a//2, 0, -1):
    print(b*j)
# упражнение 4

s = 'U'
mas = []
n, m = map(int, input().split())
for _ in range(n):
    mas.append([0]*m)
print(mas)
i = 0
j = 0
cnt = 1
while cnt < n*m:
    if s == 'U':
        while j < m - 1:
            if mas[i][j + 1] == 0:
                mas[i][j] = cnt
                cnt += 1
                j += 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        i += 1
        s = 'R'
    elif s == 'R':
        while i < n - 1:
            if mas[i + 1][j] == 0:
                mas[i][j] = cnt
                cnt += 1
                i += 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        j -= 1
        s = 'D'
    elif s == 'D':
        while j > 0:
            if mas[i][j - 1] == 0:
                mas[i][j] = cnt
                cnt += 1
                j -= 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        i -= 1
        s = 'L'
    elif s == 'L':
        while i > 0:
            if mas[i - 1][j] == 0:
                mas[i][j] = cnt
                cnt += 1
                i -= 1
            else:
                break
        mas[i][j] = cnt
        cnt += 1
        j += 1
        s = 'U'
print(mas)
# упражнение 5

'''



