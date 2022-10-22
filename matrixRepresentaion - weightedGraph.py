def addVertex(v):
    global graph
    global verticesNo
    global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        verticesNo = verticesNo + 1
        vertices.append(v)
        if verticesNo > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(verticesNo):
            temp.append(0)
        graph.append(temp)


def addEdge(v1, v2, e):
    global graph
    global verticesNo
    global vertices
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e


def printGraph():
    global graph
    global verticesNo
    for i in range(verticesNo):
        for j in range(verticesNo):
            if graph[i][j] != 0:
                pass


vertices = []
verticesNo = 0
graph = []

addVertex(0)
addVertex(1)
addVertex(2)
addVertex(3)
addVertex(4)


addEdge(0, 1, 2)
addEdge(0, 2, 3)

addEdge(1, 0, 2)
addEdge(1, 2, 15)
addEdge(1, 3, 2)

addEdge(2, 0, 3)
addEdge(2, 1, 15)
addEdge(2, 4, 13)

addEdge(3, 1, 2)
addEdge(3, 4, 9)

addEdge(4, 2, 13)
addEdge(4, 3, 9)

printGraph()

v = 0
for v in range(5):
    print(graph[v])
    v = v + 1
