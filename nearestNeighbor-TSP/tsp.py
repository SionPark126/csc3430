

file = open("cities.txt","r")
lines = file.read().split("\n")

neighbor =""
visited = []
neighbors = dict()
countCities = 0
totalWeight =0


def nearest(route):
    
    city=""
    minimum = 10000000000000
    for neighbor, weight in route.items():
        weight = int(weight)
        if weight < minimum: #compare distance, if new dist is smaller enter if   
            city = neighbor
            minimum = weight
            #print(minimum)  
    return minimum, city


for line in lines:
    line =line.split()
    neighbor = line[1]
    #print(neighbor)
    if not visited:
        visited.append(neighbor) #add visited city
        print(visited)
    countCities += 1
    
    if line[0] not in visited:
        if line[2] != 0:
            neighbors[line[0]] = line[2]
           # print(line[2])
        
    if countCities == 29:
        #print(neighbors)
        currentWeight, currentNeighbor = nearest(neighbors)
        file = 
        print(currentNeighbor)
        print (currentWeight)
       
        visited.append(currentNeighbor)
        print(visited)
        totalWeight = totalWeight+ currentWeight
        countCities = 0
        neighbors.clear()
        
print(visited)
print(totalWeight)
