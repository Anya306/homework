
# дз 2

mas = list(map(int, input().split()))
s = (mas[0] + 1) * mas[0]//2
print(s - (sum(mas) - mas[0]))
# упражнение 1

n, s = map(str, input().split())
n = int(n)
mas = []
st = []
for i in range(len(s)):
    mas.append(s[i])
for j in range(len(s)//n, len(s) + 1, len(s)//n):
    c = mas[j - len(s)//n:j]
    c.reverse()
    st.extend(c)
for _ in range(len(st)):
    print(st[_], end='')
# задание 2


s = input()
p = True
m = True
z0 = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
z1 = ['E', 'J ', 'S', 'Z']
z2 = ['3', 'L', '2', '5']
for i in range((len(s) + 1) //2):
    if s[i] != s[-i - 1]:
        p = False
        break
for i in range((len(s) + 1) //2):
    if not m:
        break
    if s[i] in z0:
        if s[-i - 1] != z0[z0.index(s[i])]:
            m = False
    elif s[i] in z1:
        if s[-i - 1] != z2[z1.index(s[i])]:
            m = False
    elif s[i] in z2:
        if s[-i - 1] != z1[z2.index(s[i])]:
            m = False
    else:
        m = False
if p:
    if m:
        print(f'{s} is a mirrored palindrome.')
    else:
        print(f'{s} is a regular palindrome.')
else:
    if m:
        print(f'{s} is a mirrored string.')
    else:
        print(f'{s} is not a palindrome.')
# задание 3


mas = list(map(int, input().split()))
for i in range(1, len(mas), 2):
    print(mas[i], mas[i - 1], end=' ')
if len(mas) % 2 == 1:
    print(mas[-1])
#упражнение 4
  
      
mas = list(map(int, input().split()))
print(int(mas[-1]), *mas[:-1])
# упражнение 5


mas = list(map(int, input().split()))
for i in range(len(mas)):
    if mas.count(mas[i]) == 1:
        print(mas[i], end=' ')
# упражнение 6


mas = list(map(int, input().split()))
maxi = 0
max_i = 0
for i in range(len(mas)):
    if mas.count(mas[i]) > maxi:
        maxi = mas.count(mas[i])
        max_i = mas[i]
print(max_i)
# упражнение 7


mas = list(map(int, input().split()))
mv = max(mas)
mn = 0
m = (mv + mn + 1) // 2
mi = len(mas) - 1
ma = 0
while ma != mi:
    m = (mv + mn + 1) // 2
    ma = 0
    mi = 0
    for i in range(len(mas)):
        if mas[i] > m:
            ma += 1
        elif mas[i] < m:
            mi += 1
    print(m, mv, mn, ma, mi)
    if mi > ma:
        mv = m
    elif ma > mi:
        mn = m
print(m)
# упражнение 8 


f = open('input.txt')
s = f.read()
mas = s.split()
print(mas)
cnt = 0
rd = '.!?'
for i in range(len(mas)):
    if mas[i][-1] in rd:
        cnt += 1
print(cnt)
# упражнение 9






