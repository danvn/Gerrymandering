# Dan Nguyen
# Solving Gerrymandering with Simulated Annealing
# Assignment 5

import math
import sys
import time
import random
file = open(sys.argv[1], "r")
data = file.readlines()
graph = []


class City:
    def __init__(self):
        self.districts = {}
        self.representatives = {}
        self.repub_rep_pct = 0.0
        self.party_vote = ""

    def getDistrict(self, key):
        return self.districts[key]

    def getDistricts(self):
        return self.districts

    def setDistricts(self, R):
        self.districts = R

    def setRepresentatives(self):
        repubdist = 0
        demdist = 0
        none = 0
        for key in self.districts:
            # print "District", key
            R = 0
            D = 0
            for voter in self.districts[key].getNodes():
                v = self.districts[key].getNode(voter)
                if v == 'R':
                    R = R + 1
                elif v == 'D':
                    D = D + 1
            if (R > D):
                self.representatives[key] = 'R'
                repubdist = repubdist + 1
                self.party_vote = 'R'
            if (D > R):
                self.representatives[key] = 'D'
                demdist = demdist + 1
                self.party_vote = 'D'
            if (D == R):
                # print "TIE"
                self.representatives[key] = None
                none = none + 1
            # print "Republicans: ", R
            # print "Democrats: ", D
        self.repub_rep_pct = float(repubdist) / float(repubdist + demdist)

    def getRepresentatives(self):
        return self.representatives

    def getRepubRepPct(self):
        return self.repub_rep_pct


class District:
    def __init__(self):
        self.nodes = {}
        self.adjacent = {}
        self.valid = True

    def isLegal(self):
        legal = False
        nodescopy = self.nodes
        if (nodeDFS(list(self.nodes.keys())[0], self.adjacent, nodescopy) == True):
            return True
        else:
            return False

    def addNode(self, i, j):
        self.nodes[(i, j)] = graph[i][j]


    def createAdjList(self):
        a = self.nodes
        for node in self.nodes:
            x1 = node[0]
            y1 = node[1]
            for node2 in a:
                # z = node.split(',')
                x2 = node2[0]
                y2 = node2[1]
                # print "examining ",(x1,y1),(x2,y2)
                # print (x1,y1),(x2,y2)
                if (self.isNeighbor(x1, y1, x2, y2)):
                    if not (x1, y1) in self.adjacent:
                        self.adjacent[(x1, y1)] = [(x2, y2)]
                    else:
                        if (x2, y2) not in self.adjacent[(x1, y1)]:
                            self.adjacent[(x1, y1)].append((x2, y2))
                    if not (x2, y2) in self.adjacent:
                        self.adjacent[(x2, y2)] = [(x1, y1)]
                    else:
                        if (x1, y1) not in self.adjacent[(x2, y2)]:
                            self.adjacent[(x2, y2)].append((x1, y1))
                            # self.adjacent[(i,j)] = []
                            # self.adjacent[(i,j)].append((a,b))
                            # self.adjacent[(i,j)].append((a,b))

    def deleteNode(self, i, j):
        if (self.nodes[i, j]):
            del self.nodes[i, j]

    def getSize(self):
        return len(self.nodes)

    def getNode(self, key):
        # print key
        x1 = key[0]
        y1 = key[1]
        return self.nodes[x1, y1]

    def getNodes(self):
        return self.nodes

    def getCoordinates(self):
        return self.nodes.keys()

    def getAdjacency(self):
        return self.adjacent

    def isNeighbor(self, a, b, c, d):
        if (a == c and b == d):
            return False
        else:
            x = abs(a - c)
            y = abs(b - d)
            if x > 1 or y > 1 or x + y > 2:
                return False
            return True


def nodeDFS(start, adjlist, nodeslist):
    if (len(nodeslist) > 0):
        for nodes in adjlist[start]:
            if (nodes in nodeslist):
                del nodeslist[nodes]
                nodeDFS(nodes, adjlist, nodeslist)
        if (len(nodeslist) != 0):
            return False
        else:
            return True
    else:
        return True

def fitness(city):
    return city

def simulatedAnnealing(initialcity,city, fitnessFunction):
    s = fitness(initialcity) #generate initial solution
    T = sys.maxint # Set initial temp
    k = .8
    Tmin = .00001 #minimum temperature for the algorithm, tunable parameter
    alpha = 0.9 # temperature adjustment, tunable parameter
    while T > Tmin:
        while T != 0:
            s = city
            fitnessDiff = fitness(initialcity) - fitness(city)
            if fitnessDiff < fitness(initialcity):
                initialcity = city
            else:
                if s == math.exp(fitnessDiff / (k * T)):
                    T = T * alpha
    return s

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

print "\nParty division in population:"
print "*************************************"
print "R:< {0:.0f}%".format(ratCount/population * 100),">"
print "D:< {0:.0f}%".format(dragonCount/population * 100),">"
print "*************************************"


# Initial Solution Set
R = {} # Set of District Solutions by row
initialcity = City()
i = 0
Repub = 0



i = 0
while i < len(graph[0]):
    R[i] = District()
    j = 0
    while j < len(graph[0]):
        R[i].addNode(i, j)
        j = j + 1
    i = i + 1

initialcity.setDistricts(R)

# initialcity.setRepresentatives()
# print initialcity.getRepresentative()
# print initialcity.getDistrict(district).getAdjacency()
# print initialcity.getDistrict(district).isLegal()

initialcity.setRepresentatives()
initial_represenatives = initialcity.getRepresentatives()

r_votes = 0
d_votes = 0
ties = 0
for district in initial_represenatives:
    if initial_represenatives[district] == "R":
        r_votes += 1
    elif initial_represenatives[district] == "D":
        d_votes += 1
    else:
        ties += 1

print "\nNumber of districts with a majority for each party:"
print "*************************************"
print "R:", r_votes
print "D:", d_votes
print "*************************************"

print "\nLocations assigned to each district:"
print "*************************************"
time.sleep(4)
for district in initialcity.getDistricts():
    print "District",district+1,":",initialcity.getDistrict(district).getCoordinates()
print "*************************************"

print "\n*************************************"
print "Algorithm Applied: Simulated Annealing"
print "*************************************"

print "\n*************************************"
print "Number of States Explored:", sys.getsizeof(graph)
print "*************************************"
init_dist = initialcity.getDistrict(1)

