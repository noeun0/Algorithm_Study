import sys
sys.stdin = open('input.txt')

def dfs(cnt,num):
    global mnum
    if cnt >= len(N)-1 and cnt>=1:
        if mnum > abs(num-int(N))+len(str(num)):
            mnum=abs(num-int(N))+len(str(num))
    if cnt >len(N):
        return
    for i in numlist:
        num+=int(i)*10**cnt
        dfs(cnt+1,num)
        num-=int(i)*10**cnt

N = input()
M = int(input())
numlist = ['0','1','2','3','4','5','6','7','8','9']
if M !=0:
    errlist = list(input())
    numlist = list(set(numlist) - set(errlist))

nnum = int(N)
mnum=abs(nnum-100)
dfs(0,0)
print(mnum)

