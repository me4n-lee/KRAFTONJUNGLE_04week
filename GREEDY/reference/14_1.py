#https://www.acmicpc.net/problem/1700
#멀티탭 스케줄링
#1700

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# print(n_list)

def fun():

    set_list = []
    cnt = 0

    for i in range(k):

        visit = [0] * k
        # if n_list[i] in set_list:
        #     continue
        if len(set_list) < n:
            set_list.append(n_list[i])
            # continue

        # if n_list[i] in set_list:
        #     continue

        else:
            if n_list[i] in set_list:
                continue

            else:
                for j in range(i, k):
                    
                    if n_list[j] in set_list:
                        visit[j] = 1
                    
                    else:
                        set_list.remove
        print(visit)
    return cnt

answer = fun()
print(answer)