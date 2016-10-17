import sys
from collections import defaultdict


file = open(sys.argv[1], "r")
data = file.readlines()
graph = []

for i in range(len(data)):
    graph.append(data[i].rstrip('\n').split(' '))

ratCount = 0.0
dragonCount = 0.0
population = 0.0

for i in range(len(graph)):
    for x in range(len(graph[i])):
        if graph[i][x] == "R":
            ratCount += 1
            population += 1
        elif graph[i][x] == "D":
            dragonCount += 1
            population += 1
    print graph[i]

print "Party division in population:"
print "*****************************"
print "R:< {0:.0f}%".format(ratCount/population * 100),">"
print "D:< {0:.0f}%".format(dragonCount/population * 100),">"
print "*****************************"

class city:
    def __init__(self):
        self.numberNodes = 0;
        self.districts = {}

    def __iter__(self):
        return iter(self.n.values())

    def add_district(self, district_num, district):
        self.districts[district_num] = district

    def add_edge(self,frm, to, weight):
        self.n[frm].add_adj(to, weight)
        self.n[to].add_adj(frm, weight)

    def add_heuristic(self, node, heuristic):
        self.n[node].heuristic = heuristic

    def has_key(self, node):
        for i in self.n:
            if node == i:
                return True
        return False

    def get_vertex(self, node):
        if node in self.n:
            return self.n[node]
        else:
            return None

    def getDistricts(self):
        return self.districts

class Neighborhood:
    def __init__(self, x, y, party):
        self.position = (x,y)
        self.party = party
        self.adjacent = defaultdict(list)
        self.distance = sys.maxint
        self.visited = False
        self.parent = None

    def add_adj(self, adjacentNode, weight):
        self.adjacent[adjacentNode] = weight

    def get_weight(self, adjacentNode):
        return self.adjacent[adjacentNode]

    def set_visited(self):
        self.visited = True

    def get_distance(self):
        return self.distance

    def set_distance(self,dist):
        self.distance = dist

def listNeighbors(graph, a = int, b = int):
    print "Neighbors of", (a,b), ": "
    print (a-1, b+1), (a,b+1), (a+1,b+1)
    print (a-1, b), (a,b), (a+1, b)
    print (a-1, b-1), (a, b-1), (a+1, b-1)

firstConfig = city

def initialSolution(graph):
    for x in graph:
        firstConfig.add_vertex()


initialSolution(graph)