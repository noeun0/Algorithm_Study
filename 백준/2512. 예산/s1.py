import sys
sys.stdin = open('input.txt')

N = int(input())
money = [i for i in map(int,input().split())]
goal = int(input())


start = 1
end = max(money)

if sum(money) <= goal:
    print(max(money))
else:
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in money:
            if mid < i:
                total += mid
            else:
                total += i


        if total > goal:
            end = mid-1
        else:
            start = mid+1

    print(end)