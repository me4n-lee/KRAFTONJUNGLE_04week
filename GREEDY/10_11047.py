#https://www.acmicpc.net/problem/11047
#동전 0
#11047

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    a = int(input())
    coins.append(a)

# print(coins)

coins.sort(reverse=True)

# print(coins)

def fun(k):

    cnt = 0

    for coin in coins:
        if coin <= k:
            count =  k // coin
            k = k % coin
            cnt = cnt + count
            # cnt += 1
    
    return cnt

answer = fun(k)
print(answer)