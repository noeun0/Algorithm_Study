import sys
import itertools
sys.stdin = open('input.txt')

def sumf(set):
    asum = 0
    for i in range(N//2):
        for j in range(N//2):
            asum+=board[set[i]][set[j]]
    return asum

for tc in range(1,int(input())+1):

    N = int(input())
    board = [[i for i in map(int,input().split())] for _ in range(N)]
    rlist = list(itertools.combinations((i for i in range(N)),N//2))
    result =100000

    for rset in rlist[:len(rlist)//2]:
        lset = list(set(i for i in range(N))-set(rset))
        result = min(result,abs(sumf(lset)-sumf(rset)))
    print("#{} {}".format(tc,result))


