#https://www.acmicpc.net/problem/9084
#동전
#9084

# import sys
# input = sys.stdin.readline

t = int(input())

# # n = 동전의 가지수 / coin = 각 동전의 개수 / m = 만들어야 하는 금액
# n = int(input())
# coin = list(map(int, input().split()))
# m = int(input())

# # print(n)
# # print(coin)
# # print(m)

# dp = [0] * (m+1)

def fun(n, coin, m):

    for i in range(n):
        for j in range(m+1):
            if j == coin[i]:
                dp[j] += 1
            elif j > coin[i]:
                dp[j] += dp[j-coin[i]]

    return dp

# result = fun(n, coin, m)
# answer = result[m]
# print(answer)

for _ in range(t):
    # n = 동전의 가지수 / coin = 각 동전의 개수 / m = 만들어야 하는 금액
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    
    dp = [0] * (m+1)
    result = []

    result = fun(n, coin, m)
    print(result[m])
    