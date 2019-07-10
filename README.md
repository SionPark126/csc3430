# csc3430-projects

This repository includes two separate projects: ADAA and nearestNeighbor-TSP


### Project Description

Write a GUI Program in Java using the GraphStream (Links to an external site.) library. The program should have the following functionalities:

Load a graph from file. The file format will be an edge list, each edge will be in a single line. The following list is an example of a graph in a file with this format:
```
a, b, 2
a, c, 1
b, a, 4
c, d, 1
d, a, 3
```
Draw the graph. This functionality should allow the user to select different layouts.
Find Minimum Spanning Tree, this should be draw over the displayed graph, showing the edges in a different color
Find the shortest path from node A to node B. The user specifies the start node, A, and the destination node, B. The program finds the shortest path, and colors it in the displayed graph.
Clear the previous operation, should clear the colored graph and return the graph to its default visualization.

### Run the program

```
$ java -jar adaa.jar inputfile.txt
```
* The program reads the input file and draws a graph in the program as seen below

![image](/images/image1.png)

* User can pick from two different layouts. (The default one and the layout2)
![image](/images/image2.png)

* Then user can find minimum spanning tree of the graph by clicking "Minimum Spanning Tree" button. 
![image](/images/image3.png)

* User also can put the start and end node to find the shortest path between two nodes.
![image](/images/image4.png)

## NearestNeighbor-TSP

The project solves a TSP using Nearest Neighbor algorithm. 

### Project Description

Read the description:

https://github.com/SionPark126/csc3430/blob/master/nearestNeighbor-TSP/TSP.pdf

### Run the program

```
$ python3 tsp.py [filename] 
```

The file has to be in txt file and the format should follow, 

location1 location2 distance
location1 location3 distance 
...
location3 location2 distance 


