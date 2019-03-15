
file = open("cities_cp.txt","r")
lines = file.read().split("\n")

neighbor =""
visited = []
route = []
neighbors = dict()
cities = dict()
countCities = 0
totalWeight =0

def nearestNeighbor(city):

    route = cities[city]
    #print(route)
    shortestDistance = 10000000000000
    for neighbor, weight in route.items():
        weight = int(weight)

        if weight < shortestDistance and neighbor not in visited: #compare distance, if new dist is smaller enter if
            city = neighbor
            shortestDistance = weight

    print(shortestDistance)
    return shortestDistance, city

def map(lines):
    global countCities
    for line in lines:
        line =line.split()
        if countCities ==0 or countCities%30 ==0:
            neighbor = line[0]
            cities[neighbor]= dict()
            cities[neighbor][line[1]] = line[2]
            countCities =0
        else:
            cities[neighbor][line[1]] = line[2]
        countCities += 1
        # if neighbor in
    return cities

def tsp(city):
    global totalWeight
    if len(visited) ==30:
        lastDistance = int(cities[visited[29]][visited[0]])
        totalWeight += lastDistance
        visited.append(visited[0])
        return visited, totalWeight
    else:
        minimumDistance, closestCity = nearestNeighbor(city)
        visited.append(closestCity)
        totalWeight += minimumDistance
        tsp(closestCity)

#put cities into a map
map(lines)
print(cities)
#starting city
tsp("SanFrancisco")
print (visited, totalWeight)
