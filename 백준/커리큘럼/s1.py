from collections import deque
import copy
import sys
sys.stdin = open('input.txt')

V= int(input())
inde = [0] *(V+1)
graph = [[] for i in range(V+1)]
time = [0] *(V+1)

for i in range(1, V+1):
    data = list(map(int, input().split()))
    time[i] =  data[0]
    for x in data[1:-1]: # 마지막 -1제외
        inde[i] +=1
        graph[x].append(i)

print(graph, inde, time)

def sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,V+1):
        if inde[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            inde[i]-=1
            if inde[i]==0:
                q.append(i)
    for i in range(1,V+1):
        print(result[i])

sort()