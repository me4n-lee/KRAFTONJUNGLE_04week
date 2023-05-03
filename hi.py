INF = int(1e9)  # 무한대 값을 표현하기 위해 10억으로 설정
# 노드 개수, 간선 개수 입력받기
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에게 가는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 모든 간선 정보 입력받기
for _ in range(m):
    # u에서 v로 가는 비용 c
    u, v, c = map(int, input().split())
    graph[u][v] = c

# Floyd-Warshall 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 모든 정점에서의 최단 거리 비용 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[i][j], end=' ')
            print()
