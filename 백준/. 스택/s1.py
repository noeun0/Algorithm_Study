import sys
sys.stdin = open("input.txt")


N = int(input())
stack = []
for _ in range(N):
    a = input()
    if a[:4] == 'push':
        stack.append(a[5:])

    elif a == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif a == 'size':
        print(len(stack))
    elif a == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    else:
        if stack:
            print(stack[-1])
        else:
            print('-1')