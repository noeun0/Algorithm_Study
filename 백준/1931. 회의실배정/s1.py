import sys
sys.stdin = open("input.txt")

def func(s,cnt):
    global result
    if list_h[s][1] > end or s == N:
        result.append(cnt)
        return

    for m in range(s,N):
        if list_h[s][1] <= list_h[m][0]:
            if cnt >= check[m]:
                check[m] = cnt+1
                func(m,cnt+1)
            else:
                return

N  = int(input())
list_h = [[i for i in map(int,input().split())] for i in range(N)]
list_h = sorted(list_h, key =lambda x : x[0])
#print(list_h)
result = []
check = [0]*N
end = list_h[-1][0]
for i in range(2):
    start = list_h[i][0]
    func(i,1)

print(max(result))
