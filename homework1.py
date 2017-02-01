from Node import Node
from algorithms import BFS, DFS, UCS, ASTAR
from collections import deque

#Read data from input.txt
input_data = open("input1.txt")
ALGO = input_data.readline().rstrip()
START_STATE = input_data.readline().rstrip()
GOAL_STATE = input_data.readline().rstrip()
T_LINES = int(input_data.readline().rstrip())

# Create a set of unique intersections.
#Read the next T_LINES. Find the first two words in each line and add them to a set.
#The set then gives the unique intersections.
INTERSECTIONS = []
TRAFFIC_LINES = []
for i in range(0,T_LINES):
    traffic_data = input_data.readline().rstrip()
    TRAFFIC_LINES.append(traffic_data)
    temparray = traffic_data.split(" ")
    temparray2 = temparray[:2]

    for element in temparray2:
        INTERSECTIONS.append(element)

print TRAFFIC_LINES

#Convert INTERSECTIONS from LIST to SET to get rid of duplicates.
INTERSECTIONS = set(INTERSECTIONS)
# print "INTERSECTIONS = ",INTERSECTIONS
n = len(INTERSECTIONS)


#From INTERSECTIONS, create objects for each intersection. Add object to NODE_LIST
NODE_LIST = {}
i = 0
for i in INTERSECTIONS:
    tempname = i
    tempname = Node()
    tempname.name = i
    NODE_LIST[i] = tempname

#Add Sunday traffic heuristics for A*
if ALGO == "A*":
    sunday_traffic_lines = input_data.readline().rstrip()
    print "sunday traffic lines = ", sunday_traffic_lines
    if sunday_traffic_lines:
        for i in range(1,int(sunday_traffic_lines)):
            tempstring = input_data.readline().rstrip()
            temparray = tempstring.split(" ")
            NODE_LIST[temparray[0]].heuristic = int(temparray[1])
# for obj in NODE_LIST:
#     print obj.name

#Add children to each node in NODE_LIST. Read traffic_data. Split it as <from> <to> <distance>
#Add <to> and <distance> to the children dictionary of the object if <from> = obj.name
for line in TRAFFIC_LINES:
    temparray = line.split(" ")
    # print temparray
    #tempstring =
    NODE_LIST[temparray[0]].children.append(temparray[1] +" "+temparray[2])


for node in NODE_LIST:
    print node, NODE_LIST[node].children

print ALGO

if ALGO == "BFS":
    BFS(NODE_LIST, START_STATE, GOAL_STATE)

elif ALGO == "DFS":
    DFS(NODE_LIST, START_STATE, GOAL_STATE)

elif ALGO == "UCS":
    UCS(NODE_LIST, START_STATE, GOAL_STATE)

elif ALGO == "A*":
    ASTAR(NODE_LIST, START_STATE, GOAL_STATE)
