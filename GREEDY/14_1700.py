#https://www.acmicpc.net/problem/1700
#멀티탭 스케줄링
#1700

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
n_list = list(map(int, input().split()))

def fun():
    set_list = []
    cnt = 0

    for i in range(k):
        if n_list[i] in set_list:
            continue

        if len(set_list) < n:
            set_list.append(n_list[i])
        else:
            max_use = 0
            index = 0

            for j in range(len(set_list)):
                next_use = 0
                for future_item in n_list[i+1:]:
                    if set_list[j] == future_item:
                        break
                    next_use += 1

                if next_use > max_use:
                    max_use = next_use
                    index= j

            set_list[index] = n_list[i]
            cnt += 1

        print(set_list)

    return cnt

answer = fun()
print(answer)