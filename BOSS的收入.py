from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
in_dep = [0]*(n+1)
total_money = [0]*(n+1)
for _ in range(n):
    a ,leader, salary  = tuple(map(int, input().split()))
    graph[a].append(leader)
    total_money[a] = salary
    in_dep[leader]+=1

q = deque([i for i, d in enumerate(in_dep) if d==0])

root = 0
while q:
    node = q.popleft()
    if graph[node] == []:
       root = node
       break
    leader = graph[node][0]
    total_money[leader]+=total_money[node]//100*15
    in_dep[leader]-=1
    if in_dep[leader]==0:
        q.append(leader)

print(total_money[root])