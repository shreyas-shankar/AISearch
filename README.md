# AISearch
Implementation of BFS, DFS, A* and UCS Search for CSCI 561 (Fundamentals of AI) at USC

There are 4 Search Algorithms that have been implemented here.

1. Breadth First Search
2. Depth First Search
3. Uniform Cost Search
4. A* Search.

The algorithms have been implemented keeping in mind the input format specification. 

#Input Format

<ALGO>
<START STATE>
<GOAL STATE>
<NUMBER OF LIVE TRAFFIC LINES>
<... LIVE TRAFFIC LINES ...>
<NUMBER OF SUNDAY TRAFFIC LINES>
<... SUNDAY TRAFFIC LINES ..

SUNDAY TRAFFIC LINES provide the heuristic to be used for the A* Algorithm.

#Output Format
<STATE>
<ACCUMULATED TRAVEL TIME FROM START STATE UNTIL NEXT NODE>
