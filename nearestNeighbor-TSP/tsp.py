

file = open("cities.txt","r")
lines = file.read().split("\n")

neighbor =""
visited = []
route = []
neighbors = dict()
cities = dict()
countCities = 0
totalWeight =0


def nearest(city):

    route= cities[city]
    #print(city)
    minimum = 10000000000000
    for neighbor, weight in route.items():
        weight = int(weight)
        #print(neighbor)
        if weight < minimum and neighbor not in visited: #compare distance, if new dist is smaller enter if
            city = neighbor
            minimum = weight
            # print("ATLANA CLOSEST")
            # print(city)
    return minimum, city

#
# for line in lines:
#     line =line.split()
#
#     neighbor = line[1]
#     #print(neighbor)
#     if not visited:
#         visited.append(neighbor) #add visited city
#         print(visited)
#     countCities += 1
#
#     if line[0] not in visited:
#         if line[2] != 0:
#             neighbors[line[0]] = line[2]
#            # print(line[2])
#
#     if countCities < 29:
#         #print(neighbors)
#         currentWeight, currentNeighbor = nearest(neighbors)
#         file =
#         print(currentNeighbor)
#         print (currentWeight)
#
#         visited.append(currentNeighbor)
#         print(visited)
#         totalWeight = totalWeight+ currentWeight
#         countCities = 0
#         neighbors.clear()

for line in lines:
    line =line.split()
    if countCities ==0 or countCities%29 ==0:
        neighbor = line[1]
        print(neighbor)
        cities[neighbor]= dict()
        cities[neighbor][line[0]] = line[2]
        if (countCities ==29):
            countCities =0
    else:
        #print(neighbors)
        cities[neighbor][line[0]] = line[2]

        # currentWeight, currentNeighbor = nearest(neighbors)
        # file =
    countCities += 1
print(cities)
        # print(currentNeighbor)
        # print (currentWeight)
        # visited.append(currentNeighbor)
        # print(visited)
        # totalWeight = totalWeight+ currentWeight
        # countCities = 0
        # neighbors.clear()

def closest(city):
    global totalWeight

    visited.append(city)
    # print(visited)
    if len(visited) ==30:
        return visited, totalWeight
    else:
        print("entereed")
        minimum, closestCity = nearest(city)
        # print(minimum)
        # print(closestCity)
        totalWeight += minimum
        closest(closestCity)
        # print(visited)
        # print(totalWeight)




closest("GulfShores")
print (visited, totalWeight)
    # neighbor = line[1]
    #print(neighbor)
    # if not visited:
    #     visited.append(neighbor) #add visited city
    #     print(visited)


    # if line[0] not in visited:
    #     if line[2] != 0:
    #         neighbors[line[0]] = line[2]
           # print(line[2])
