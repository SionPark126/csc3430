

file = open("cities.txt","r")
lines = file.read().split("\n")

neighbor =""
visited = set()
totalWeight =0
currentWeight = 0


for line in lines:
    line =line.split()
    neighbor = line[1]
    visited.add(line[1]) #add visited city
    min = float("inf")
    if line[0] not in visited:
        while()# need to group neighbors first
        if (line[2] < min): #compare distance, if new dist is smaller enter if
            global totalWeight, currentWeight
            print("entered")
            neighbor = line[0]
            currentWeight = line[2]
            min = line[2]
            visited.add(neighbor)
            totalWeight = totalWeight+ currentWeight
    # print(visited)
    # print(totalWeight)
