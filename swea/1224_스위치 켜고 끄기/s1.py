import sys
sys.stdin = open("input.txt")


N = int(input())
list_a=[]

list_a = list(map(int,input().split()))
#남학생1 여학생2

std = int(input())
for st in range(std):
    who, num = map(int,input().split())
    if who ==1:
        for i in range(num-1,N):#0~7
            if (i+1)%num==0:
                list_a[i]=(list_a[i]+1)%2

    else:
        for i in range(0,N//2+1): # 1차이나는곳부터
            if (num-1-i) in range(N) and (num-1+i) in range(N):
                if list_a[num-1-i] ==list_a[num-1+i]:
                    list_a[num-1 - i],list_a[num-1+i] = (list_a[num-1+i]+1)%2,(list_a[num-1+i]+1)%2
                else:
                    break

for i in range(N):
    print(list_a[i],end= " ")
    if (i+1)%20==0:
        print("")
