import sys

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
