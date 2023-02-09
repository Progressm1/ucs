class PQueue():
    def __init__(self):
        self.dict = {}
        self.keys = []
        self.sorted = False
        
    def push(self, k, v):
        self.dict[k] = v
        self.sorted = False
        
    def _sort(self):
        self.keys = sorted(self.dict, key=self.dict.get)
        self.sorted = True
        
    def pop(self):
        try:
            if not self.sorted:
                self._sort()
            key = self.keys.pop(0)
            value = self.dict[key]
            self.dict.pop(key)
            return key, value
        except:
            return None
        
def path_costs(path):
    c = {}
    with open(path, 'r') as file:
        for line in file:
            line = line.split(", ")
            v = int(line.pop())
            e1 = line.pop()
            e2 = line.pop()
            if e1 not in c:
                c[e1] = {}
            if e2 not in c:
                c[e2] = {}
            c[e1][e2] = c[e2][e1] = v
    return c

def ucs(start, goal, g):
    frontier = PQueue()
    # pushing path and cost to pqueue
    frontier.push(start, 0)
    while True:
        # poping path with least cost
        path, cost = frontier.pop()
        if path is None:
            return None
        # splitting out end node in path
        end = path.split("->")[-1]
        if goal == end:
            return path, cost
        for node, weight in g[end].items():
            # adding edge weight(cost) to total cost
            new_cost = cost + weight
            new_path = path + "->" + node
            # adding new path and cost to pqueue
            frontier.push(new_path, new_cost)

graph = path_costs('/home/Paths.txt')
start = 'Arad'
goal = 'Bucharest'
path, cost = ucs(start, goal, graph)
if path is not None:
    print("Path: ", path)
    print("Cost: ", cost)
else:
    print("No path found from {} to {}".format(start, goal))
