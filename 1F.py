from collections import deque

s = input()
deque0 = deque(s)
deque02 = deque(s)
deque1 = deque()
deque12 = deque()
res2 = deque()
res = []
zn = ['-', '+', '*', '/']
zn2 = ['-', '+', '*', '/', '(', ')']

while len(deque0) > 0:
    if deque0[0] == '(':
        deque1.appendleft(deque0[0])
        deque0.popleft()
    elif deque0[0] == ')':
        deque0.popleft()
        while deque1[0] != '(':
            res.append(deque1[0])
            deque1.popleft()
        deque1.popleft()
    elif deque0[0] in zn:
        if len(deque1) > 0:
            if deque1[0] == '*':
                while len(deque1) > 0 and deque1[0] != '(':
                    res.append(deque1[0])
                    deque1.popleft()
                deque1.appendleft(deque0[0])
                deque0.popleft()
            elif deque1[0] == '+' and (deque0[0] == '+' or deque0[0] == '-'):
                while len(deque1) > 0 and deque1[0] != '(':
                    res.append(deque1[0])
                    deque1.popleft()
                deque1.appendleft(deque0[0])
                deque0.popleft()
            else:
                deque1.appendleft(deque0[0])
                deque0.popleft()
        else:
            deque1.appendleft(deque0[0])
            deque0.popleft()
    else:
        res.append(deque0[0])
        deque0.popleft()
while len(deque1) > 0:
    res.append(deque1[0])
    deque1.popleft()
print(*res)

while len(deque02) > 0:
    if deque02[-1] == ')':
        deque12.appendleft(deque02[-1])
        deque02.pop()
    elif deque02[-1] == '(':
        deque02.pop()
        while deque12[0] != ')':
            res2.appendleft(deque12[0])
            deque12.popleft()
        deque12.popleft()
    elif deque02[-1] in zn:
        if len(deque12) > 0:
            if (deque12[0] == '*' or deque12[0] == '/') and (deque02[-1] == '+' or deque02[-1] == '-'):
                while len(deque12) > 0 and (deque12[0] == '*' or deque12[0] == '/'):
                    res2.appendleft(deque12[0])
                    deque12.popleft()
                deque12.appendleft(deque02[-1])
                deque02.pop()
            else:
                deque12.appendleft(deque02[-1])
                deque02.pop()
        else:
            deque12.appendleft(deque02[-1])
            deque02.pop()
    else:
        res2.appendleft(deque02[-1])
        deque02.pop()

while len(deque12) > 0:
    res2.appendleft(deque12[0])
    deque12.popleft()
print(*res2)
