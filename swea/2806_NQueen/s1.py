import sys
sys.stdin = open('input.txt')

def func(r):
    global result
    if r==N:
        result+=1
        #print(checkc,checkcr,checkrc)
        return
    # x,y 를 고르는 경우

    for c in range(N):
        if c not in checkc and r-c not in checkrc and c+r not in checkcr:
            checkc.append(c)
            checkrc.append(r - c)
            checkcr.append(c + r)
            func(r+1)
            checkc.remove(c)
            checkrc.remove(r - c)
            checkcr.remove(c + r)


for tc in range(1,int(input())+1):
    result =0
    # N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
    # 보드를 따로 만들지 말고, 들어온 부분을 리스트로 저장하고,, 없다면 추가하는 방식으로 해보자
    # 같은 대각선 상에 있는값은 x,y차이가 같다! 그대신 따로 생각해줄것
    N = int(input())
    checkc=[]
    checkrc=[]
    checkcr=[]

    func(0)
    print("#{} {}".format(tc,result))

