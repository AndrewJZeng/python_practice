import copy

class Node(object):
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
        
    def __str__(self):
        return self.name
    
    def getChildren(self):
        for c in self.children:
            print(c)

def build_graph(info_dict):
    nodes = {}
    for k in info_dict.keys():
        nodes[k] = Node(k)

    for k, v in info_dict.items():
        children = [nodes[name] for name in v]
        nodes[k].children = children
        
    return nodes

def print_graph(nodes):
    for k, v in nodes.items():
        print(k, ": ")
        v.getChildren()
        print()

def DFS(node, destination, path):

    
    return True



def BFS(root_node, destination):
    pass


data = {
    'boston': ['providence', 'new york'],
    'providence': ['boston', 'new york'],
    'new york': ['chicago'],
    'chicago': ['denver', 'phoenix'],
    'denver': ['phoenix', 'new york'],
    'phoenix': [],
    'los angles': ['boston']
}
nodes = build_graph(data)
print_graph(nodes)

print('\nDFS')
ans = DFS(nodes['boston'], 'phoenix', [])
print(ans)

# print('\nBFS')
# shortest = BFS(nodes['boston'], 'phoenix')
# print(shortest)





