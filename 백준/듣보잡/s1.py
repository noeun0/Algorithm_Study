import sys
sys.stdin = open('input.txt')


N,M = map(int,input().split())
Nlist = set()
Mlist = set()
for i in range(N):
    Nlist.add(input())

for i in range(M):
    Mlist.add(input().rstrip())

s1 = set(Nlist) & set(Mlist)

print(len(s1))
for i in sorted(list(s1)):
    print(i)