class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []
            
    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
            
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))
        
    def display(self):
        for node,neightbour in self.graph.items():
            print(f"{node}:{neightbour}")
            
            
g = Graph()
n = int (input("How many edges in the graph?" ))
for i in range (n):
    n1 = input("Enter the first node: ")
    n2 = input("Enter the second node: ")
    w = int(input("Enter the weight of the edge: "))
    g.add_edge(n1, n2, w)
    
g.display()