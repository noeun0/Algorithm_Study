import sys
sys.stdin = open('input.txt')
n = int(input())
arr = list(map(int,input().split()))
m = int(input())

left = 1
right = max(arr)
max_val = 0
while(left<=right):
    mid = (left+right)//2
    res=0
    for i in arr:
        if(i<=mid):
            res+=i
        else:
            res+=mid

    if(res>m):
        right = mid-1
    if(res<=m):
        left = mid+1

print(right)