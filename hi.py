# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    if u < v:
        parent[v] = u
    else:
        parent[u] = v

# 노드 개수와 간선 개수 입력받기
v, e = map(int, input().split())
parent = list(range(v+1)) # 부모 테이블에서 부모를 자기 자신으로 초기화
edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용을 담을 변수
# 모든 간선에 대한 정보 입력

for _ in range(e):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))

edges.sort() # 간선을 비용순으로 정렬

for edge in edges: # 간선을 하나씩 확인
    cost, u, v = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += cost
        
print(result)