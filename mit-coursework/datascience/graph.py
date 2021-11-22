import copy

class Node(object):
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children

    def __str__(self):
        return self.name 

    def print_children(self):
        for child in self.children:
            print(child)

def build_graph(info_dict):
    # build nodes
    nodes = {}
    for k in info_dict.keys():
        nodes[k] = Node(k)

    # build edges
    for k, v in info_dict.items():
        print(k, v)
        children = [nodes[name] for name in v]
        nodes[k].children = children
        # for child_name in v:
        #     print(nodes[k])
        #     nodes[k].children.append(nodes[child_name])
        #     print_nodes(nodes)
            # print(len(nodes[k].children))
            # print(nodes[k].print_children())
    return nodes

def print_graph(nodes):
    for k, v in nodes.items():
        print('{} -> {}'.format(k, v))
        v.print_children()
        print()

def DFS(node, destination, path, shortest):
    path.append(node.name)
    print(path)
    if node.name == destination:
        if not shortest[0] or len(path) < len(shortest[0]):
            shortest[0] = copy.deepcopy(path)
            print(shortest)

    else:
        for child in node.children:
            if child.name not in path:
                DFS(child, destination, path, shortest)
    path.pop()


def BFS(root_node, destination):
    queue = [root_node]
    parent_list = {}
    parent_list[root_node.name] = None

    while queue:
        node = queue.pop(0)
        print(node.name)
        if node.name == destination:
            path = []
            curr = node
            print(parent_list.keys())
            
            while curr.name != root_node.name:
                path.append(curr.name) 
                curr = parent_list[curr.name]
            path.reverse()
            return [root_node.name] + path        
        
        for child in node.children:
            if child.name not in parent_list:
                parent_list[child.name] = node
                queue.append(child)

    return []


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
shortest = [[]]
DFS(nodes['boston'], 'phoenix', [], shortest)
print(shortest[0])

print('\nBFS')
shortest = BFS(nodes['boston'], 'phoenix')
print(shortest)





