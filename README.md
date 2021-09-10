# A*-algorithm-Visualization
A python project to visualize how A* algorithm works for pathfinding work case. Other algorithms can be implemented on the same basis

★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★

A* (A star) algorithm is a shortest path finding algorithm that is used on daily basis in applications such as maps and also in games where there are many obstructions between the start and end point.

This project is built using python3 and PyGame library. The canvas is divided into a large grid made up of small boxes(cubes) which can be used as starting point,end point or obstruction.

This algo takes in 3 paramaters to calculate the shortest path :
 1) F score  : It is sum of g score and f score.
 2) G score  : Movement cost of moving from STARTING point to to a GIVEN Box(cube) on Grid.
 3) H score  : Estimate movement cost of moving form GIVEN box(cube) on grid to Final(end) point on grid. It is refered as heuristic as it is nothing but an apporximate "smart" guess without considering any obstrutctions or whatsoever.


These parameters are then updated to an open set and and later onthey are popped from the set and they smallest route is decided.

Everything else is described step by step in the .py file included. :)

★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★
