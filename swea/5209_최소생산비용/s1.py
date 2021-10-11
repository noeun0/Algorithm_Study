import sys
import itertools
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    board = [[i for i in map(int,input().split())] for j in range(N)]
    case = [i for i in range(N)]
    clist = list(itertools.permutations(case))
    ans = 100000
    for case in clist:
        result = 0
        for num in range(N):
            result +=board[num][case[num]]
        ans = min(ans,result)
    print("#{} {}".format(tc,ans))