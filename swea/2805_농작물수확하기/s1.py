
import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N = int(input())
    mid = N//2
    list_a =[]
    for _ in range(N):
        list_a.append( list(map(int,input())))

    result = 0
    for i in range(N):
        result+=sum(list_a[i][abs(mid-i):N-abs(mid-i)])

    print("#{} {}".format(tc,result))
