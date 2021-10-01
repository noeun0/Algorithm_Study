import sys
sys.stdin = open("input.txt")
def dfs(N,count):
    global max
    if N ==0 or count==0:
        temp = int(''.join(num_list))
        if temp > max:
            max = temp
            return
    else:
        # 01 -> (01, 02, 03,..)02 03 04 05 06
        for i in range(len(num_list)):
            for j in range(i+1, len(num_list)):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                if int(''.join(num_list)) == imax and N%2==0:
                    max = int(''.join(num_list))
                c_num = int(''.join(num_list))

                if c_num not in visited:
                    visited.append(c_num)
                    dfs(N-1,count-1)
                elif N%2==0:
                    dfs(N - 1, count - 1)
                num_list[i], num_list[j] = num_list[j], num_list[i]

for tc in range(1, int(input())+1):
    num , N = input().split()
    num_list= list(num)
    visited=[]
    imax = int(''.join(sorted(num_list,reverse=True)))
    max=0
    dfs(int(N),10)
    print("#{} {}".format(tc,max))

