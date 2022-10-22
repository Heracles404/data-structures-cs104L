import collections

def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        next = queue.popleft()
        print(next)

        for neighbour in graph[next]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4:[], 5:[], 6:[], 7:[]}
    print("Breadth-First Traversal: ")
    bfs(graph, 1)
