import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    N, B = map(int,input().split())
    clerks = [i for i in map(int,input().split())]
    #print(clerks)
    anw=100000


    for i in range(1<<len(clerks)):
        result = 0
        for j in range(len(clerks)):
            if i & (1<<j):
                result+=clerks[j]
        if result>=B:
            anw = min(anw,result-B)

    print("#{} {}".format(tc,anw))