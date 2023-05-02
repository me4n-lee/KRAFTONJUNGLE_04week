#https://www.acmicpc.net/problem/1946
#신입 사원
#1946

import sys
input = sys.stdin.readline

t = int(input())


def fun(n, n_list):

    cnt = 1
    value = n_list[0][1]
    for i in range(1, n):

        if n_list[i][1] < value:
            # if n_list[i][1] < n_list[i-1][1]:
            cnt += 1
            value = n_list[i][1]

    return cnt


for _ in range(t):
    n = int(input())
    n_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        n_list.append([a,b])

    # print(n_list)

    #n_list.sort(key = lambda x: x[0])
    n_list.sort(key = lambda x: (x[0], x[1]))
    # print(n_list)

    answer = fun(n, n_list)
    print(answer)

