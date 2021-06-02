def dfs(graph, start):
    a_group = []
    b_group = []
    a_group.append(start)
    visited = [False] * (len(graph) + 1)
    
    def visit(v):
        # print('visiting', v)
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                if v in a_group: b_group.append(w)
                else: a_group.append(w)
                visit(w)
            else:
                if not ((v in a_group and w in b_group) or (v in b_group and w in a_group)):
                    a_group.clear()
                    b_group.clear()
            
    visit(start)
    if len(a_group) == 0 and len(b_group) == 0:
        return ''
    else: 
        return (sorted(a_group), sorted(b_group))

graph = {}

n = int(input())
m = int(input())

# graph = []
# for _ in range(n+1): graph.append([])

for _ in range(m):
    line = input().split()
    i, j = [int(x) for x in line]
    # print('i:', i, 'j:', j)

    # graph[i].append(j)
    # graph[j].append(i)

    if not graph.get(i):
        graph[i] = []
    graph[i].append(j)

    if not graph.get(j):
        graph[j] = []
    graph[j].append(i)
    

# print(graph)
groups = dfs(graph, 1)

if groups == '':
    print('Nelze')
else:
    print(*groups[0])
    print(*groups[1])