import sys
sys.stdin = open('input.txt')


poket,Q = map(int,input().split())
dict={}
plist=[]
for i in range(poket):
    x = input()
    dict[x] = str(i+1)
    plist.append(x)


for q in range(Q):
    question = input()
    if ord(question[0])>=65: # 문자일떄
        print(dict[question])
    else:
        print(plist[int(question)-1])






