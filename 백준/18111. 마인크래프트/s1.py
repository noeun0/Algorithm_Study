import sys
sys.stdin = open("input.txt")

# 인벤토리에서 꺼내서 쌓는건 1초 / 제거하는건 2초
# 땅크기 n*m의 배수가 되야한다..!!!!!!지금 꺼의 합의 가장 가까운 배수를 구하고..(0포함)
# 그럼 위하나 아래하나 구할까?
N, M, B = map(int,input().split())

list_a=[]
sum_a = 0
num=0
for _ in range(N):
    input_list=list(map(int,input().split()))
    list_a =list_a+input_list
    sum_a+=sum(input_list)

for i in range(100000):
    if sum_a<=(N*M)*i:
        num=i
        break
#num, num-1을 곱했을때 둘중 하나가 답이다.  그리고 각각은 높이를 뜻함..

result_1=0
result_2=0


if sum_a-(N*M)*(num-1)+B <=64*10**6:
    for i in list_a:
        if num-1-i >=0:
            result_2+=(num-1)-i
        else:
            result_2+=2*(i-(num-1))



if (N*M)*num<=sum_a+B:
    for i in list_a:
        if num-i >=0:
            result_1+=num-i
        else:
            result_1+=2*(i-num)
else:
    result_1=result_2+1

if result_1<result_2:
    print(result_1, num)

elif result_1>result_2:
    print(result_2, num-1)


else:
    print(result_2,num)


