
import sys
sys.stdin = open("input.txt")

def func1(list_a):
    num=[]

    for i in range(N-1):
        for j in range(i+1,N):
            num.append(list_a[i]*list_a[j])

    num.sort(reverse=True)
    for i in num:
        if i-int("".join(sorted(str(i)))):
                return i
    return -1


for tc in range(1,int(input())+1):
    N = int(input())
    list_a = list(map(int,input().split()))
    print("#{} {}".format(tc,func1(list_a)))