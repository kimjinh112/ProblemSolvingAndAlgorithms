graph = {'A': ['E', 'C', 'B'],
         'B': ['F', 'D', 'A'],
         'C': ['G', 'A'],
         'D': ['B'],
         'E': ['F', 'A'],
         'F': ['E', 'B'],
         'G': ['G']
         }


def BFS(graph, root):
  # Queue 선언
    visit = []

  # 초기 조건 (root를 스택에 넣습니다.)
    stack = [root]

  # 스택에 원소가 있을 동안 반복
    while stack:

      # 방문할 꼭지점 v  = stack.pop()
        to_visit_node = stack.pop(0)

        if to_visit_node in visit:
            continue
      #방문
        visit.append(to_visit_node)
        
      #v의 자손 노드들, 단 방문한 노드 제외
        child = graph[to_visit_node]
    
        for c in child:
            if c not in visit:
                stack.append(c)

    print(visit)

BFS(graph, 'A')
