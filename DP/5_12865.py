#https://www.acmicpc.net/problem/12865
#평범한 배낭
#12865

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
    w, v = map(int, input().split())
    graph.append([w,v])

# print(graph)

dp = [0] * (k+1)


# n = 물품의 수 / k = 버틸수 있는 무게 / graph = (무게, 가치)
def fun(k, graph):

    for node in graph:
        weight = node[0]
        value = node[1]

        #k 부터 1 까지 역순으로 for문을 돌린다 / 독립성을 보장하기 위해서
        for i in range(k, 0, -1):
            if i < weight:
                continue
            if i >= weight:
                dp[i] = max(dp[i], dp[i-weight]+value)

    return dp


result = fun(k, graph)
# print(result)
answer = result[k]
print(answer)

# for i in range(n):
#     for j in range(n):
#         if graph[i][0] == graph[j][0]:
#             if graph[i][1] > graph[j][1]:
#                 graph[j][1] = 0
#             elif graph[i][1] < graph[j][1]:
#                 graph[i][1] = 0
            # else:
            #     graph[j][1] = 0