
# 4부 / 12장 그래프 탐색 

# 그래프 A가 있을 때, 정점을 모두 방문하는 '그래프 순회'를 DFS/BFS는 각각 어떻게 해결하는지 알아보자.

graph = {1: [2,3,4],
         2: [5],
         3: [5],
         4: [],
         5: [6,7],
         6: [],
         7: [3]}

# DFS(재귀구조.Ver)
# 결과는 [1,2,5,6,7,3,4]로 나온다.
# DFS는 최대한 깊게 들어간 후, 더 이상 길이 없으면 다시 후퇴하는 백트래킹 방식을 쓰기 때문.

def recursive(vertex, discover=[]):
    discover.append(vertex)
    for new_way in graph[vertex]:
        if new_way not in discover:
            recursive(new_way, discover)
        
    return discover
    
print(recursive(1))


# DFS(스택을 활용한 반복 구조.Ver)
# 결과는 [1,4,3,5,7,6,2]로 나온다. 재귀구조와 결과값이 상이하다.
# 그 이유는 스택으로 구현했기 때문
# 스택의 특징 : 맨 뒤에 넣은 것을 가장 먼저 뺀다(후입선출)

def stack(start_vertex):
    discover = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in discover:
            discover.append(vertex)
            for new_way in graph[vertex]:
                stack.append(new_way)
                
    return discover
    
print(stack(1))


# BFS(큐를 활용한 반복 구조.Ver)
# 결과는 [1,2,3,4,5,6,7]
# 언뜻 보기에는 DFS(스택)과 코드가 흡사해보이지만, 디버깅를 해보면 다름을 인지할 수 있다.
# DFS와 달리 조금이라도 먼저 찾은 인접 접점을 무조건 선방문한다. 
# 따라서 위에서부터 쭉 훑으며 내려가는 모습을 볼 수 있다.

def queue(start_vertex):
    discover = [start_vertex]
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        for new_way in graph[vertex]:
            if new_way not in discover:
                discover.append(new_way)
                queue.append(new_way)
    
    return discover

print(queue(1))

        