adjList = {}
myList = []


def addNode(node):
    if node not in myList:
        myList.append(node)
    else:
        print("Node ", node, " already exists!")


def addEdge(node1, node2):
    temp = []
    if node1 in myList and node2 in myList:
        if node1 not in adjList:
            temp.append(node2)
            adjList[node1] = temp

        elif node1 in adjList:
            temp.extend(adjList[node1])
            temp.append(node2)
            adjList[node1] = temp

    else:
        print("Nodes don't exist!")


def list():
    for node in adjList:
        print(node, " --> ", [i for i in adjList[node]])


addNode('A')
addNode('B')
addNode('C')
addNode('D')
addNode('E')

addEdge('A', 'B')
addEdge('B', 'C')
addEdge('B', 'D')
addEdge('C', 'E')
addEdge('D', 'A')
addEdge('E', 'D')

list()
