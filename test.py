import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for _ in range(n):
    w, v = map(int, input().split())
    graph.append([w, v])

# 중복되는 무게의 물품 중 가치가 높은 것만 남기기
unique_graph = []
for i in range(n):
    if graph[i][1] != 0:
        unique_graph.append(graph[i])

dp = [0] * (k+1)

# n = 물품의 수 / k = 버틸수 있는 무게 / unique_graph = (무게, 가치)
def fun(k, unique_graph):
    for i in range(k+1):
        for node in unique_graph:
            weight = node[0]
            value = node[1]

            if i >= weight:
                dp[i] = max(dp[i], dp[i-weight] + value)

    return dp

result = fun(k, unique_graph)
answer = result[k]
print(answer)
