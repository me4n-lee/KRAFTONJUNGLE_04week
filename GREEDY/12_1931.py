#https://www.acmicpc.net/problem/1931
#회의실 배정
#1931

import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for _ in range(n):
    a, b = map(int, input().split())
    n_list.append((a,b))

# print(n_list)

n_list.sort(key = lambda x: (x[1], x[0]))

# print(n_list)

def fun(n_list):

    # start = 0
    end = 0
    cnt = 0

    for node in n_list:

        if end <= node[0]:
            cnt += 1
            # start = node[0]
            end = node[1]    

    return cnt

answer = fun(n_list)
print(answer)
