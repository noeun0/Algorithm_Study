import sys
sys.stdin = open('input.txt')


def func(N,cnt):
    global result

    if N == M:
        result = min(result,cnt)
        return
    if cnt>result:
        return
    if N>1000000 or N<0:
        return

    if N+1 not in list1:
        list1.append(N+1)
        func(N+1, cnt+1)
    if N-1 not in list1:
        func(N-1, cnt+1)
    if N *2 not in list1:
        func(N*2, cnt+1)
    if N-10 not in list1:
        func(N-10, cnt+1)


for tc in range(1,int(input())+1):
    N,M = map(int,input().split())
    list1=[]
    result = 1000
    func(N,0)
    print("#{} {}".format(tc,result))