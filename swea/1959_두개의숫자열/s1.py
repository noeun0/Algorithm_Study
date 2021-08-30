
import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N1,N2 = map(int,input().split())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))

    if N1>N2:
        N1,N2 = N2,N1
        list1,list2 = list2,list1
    ans =0
    for si in range(0,N2-N1+1):
        result = 0
        for idx in range(N1):
            result+=list1[idx]*list2[si+idx]

        ans= max(ans,result)

    print("#{} {}".format(tc,ans))