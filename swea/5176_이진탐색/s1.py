import sys
sys.stdin = open("input.txt")

def tree_func(n):
    global num
    if n<=N:
        tree_func(n*2)
        tree[n] = num
        print(tree)
        num +=1
        tree_func(n*2+1)

for tc in range(1, int(input())+1):
    N= int(input())
    tree=[0 for i in range(N+1)]
    num=1
    tree_func(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
