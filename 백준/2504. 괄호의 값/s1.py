import sys
sys.stdin = open('input.txt')

str= input()
stack = []
zero= False

for i in str:
    if zero == True:
        break
    if i == '(':
        stack.append(i)
    if i == '[':
        stack.append(i)
    if i ==')':
        if not stack:
            zero=True
            break
        top = stack[-1]
        if top=='(':
            stack.pop(-1)
            stack.append(2)
        elif top in [')',']','[']:
            zero = True
            break
        else:
            temp = 0
            while stack and stack[-1] != '(' and type(stack[-1])== int:
                top = stack.pop(-1)
                temp += top
            if stack and stack[-1]=='(':
                stack.pop(-1)
                stack.append(temp*2)
            else:
                zero = True
                break
    elif i ==']':
        if not stack:
            zero=True
            break
        top = stack[-1]
        if top=='[':
            stack.pop(-1)
            stack.append(3)
        elif top in [')',']','(']:
            zero = True
            break
        else:
            temp = 0
            while stack and stack[-1] != '[' and type(stack[-1])== int:
                top = stack.pop(-1)
                temp += top
            if stack and stack[-1]=='[':
                stack.pop(-1)
                stack.append(temp*3)
            else:
                zero = True
                break

for i in stack:
    if type(i) != int or zero == True:
        print(0)
        break
else:
    print(sum(stack))