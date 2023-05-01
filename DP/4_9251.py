#https://www.acmicpc.net/problem/9251
#LCS
#9251

import sys
input = sys.stdin.readline

first_list = list(map(str, input().strip()))
second_list = list(map(str, input().strip()))

# print(first_list)
# print(second_list)

a = len(first_list)
b = len(second_list)

#first 를 second 로 확인
#세로 가로를 확실하게 체크하지 않으면 인덱스 에러 발생
dp = [[0] * (b+1) for _ in range(a+1)]

# print(dp)


def fun():
    for i in range(1, a+1):
        for j in range(1, b+1):
            
            # if first_list[i] == 0 or second_list[j] == 0:
            #     continue

            if first_list[i-1] == second_list[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp


result = fun()
print(result)
answer = result[a][b]
print(answer)