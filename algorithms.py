from collections import deque

# BFS Implementation
def BFS(NODE_LIST, START_STATE, GOAL_STATE):
    """Run Breadth First Search on NODE_LIST"""
    #Create an empty queue
    queue = deque()
    #Add Start node to queue
    queue.append(NODE_LIST[START_STATE])
    NODE_LIST[START_STATE].visited = True
    while len(queue) != 0:
        current_node = queue.popleft()
        current_node.visited = True
        print " Current node is ", current_node.name
        if current_node.name == GOAL_STATE:
            print_solution(current_node, START_STATE, NODE_LIST)
            break
        #enqueue children of current_node
        for child in current_node.children:
            print current_node.children
            split = child.split(" ")
            node = NODE_LIST[split[0]]
            #Tie breaking
            # If the node has never been visited/added to the queue
            # Add it to the queue
            # If the node has been visited and is present in the queue
            # Check for cumulativecost. If new cumulativecost < existing cumulativecost
            # replace the cumulativecost and parent.
            if node.visited != True:
                if node in queue:
                    if (current_node.cumulativecost + 1) < node.cumulativecost:
                        node.cumulativecost = current_node.cumulativecost + 1
                        node.parent = current_node.name
                else:
                    queue.append(node)
                    node.cumulativecost = current_node.cumulativecost + 1
                    node.parent = current_node.name
        for elem in queue:
            print elem.name, "parent is", elem.parent

# DFS Implementation
def DFS(NODE_LIST, START_STATE, GOAL_STATE):
    """Run Depth First Search on NODE_LIST"""
    #Create an empty queue
    queue = deque()
    #Add Start node to queue
    queue.append(NODE_LIST[START_STATE])
    NODE_LIST[START_STATE].visited = True
    while len(queue) != 0:
        current_node = queue.popleft()
        current_node.visited = True
        print " Current node is ", current_node.name
        if current_node.name == GOAL_STATE:
            print_solution(current_node, START_STATE, NODE_LIST)
            break
        tempqueue = deque()
        #enqueue children of current_node
        for child in current_node.children:
            print current_node.children
            split = child.split(" ")
            node = NODE_LIST[split[0]]
            #Tie breaking
            # If the node has never been visited/added to the queue
            # Add it to the queue
            # If the node has been visited and is present in the queue
            # Check for cumulativecost. If new cumulativecost < existing cumulativecost
            # replace the cumulativecost and parent.
            if node.visited != True:
                if node in queue:
                    if (current_node.cumulativecost + 1) < node.cumulativecost:
                        node.cumulativecost = current_node.cumulativecost + 1
                        node.parent = current_node.name
                else:
                    tempqueue.append(node)
                    node.cumulativecost = current_node.cumulativecost + 1
                    node.parent = current_node.name
        print "Tempqueue"
        for elem in tempqueue:
            print elem.name, "parent is", elem.parent
        while len(tempqueue) > 0:
            tempnode = tempqueue.pop()
            queue.appendleft(tempnode)
        print "Queue"
        for elem in queue:
            print elem.name, "parent is", elem.parent

#Uniform Cost Search Implementaiton
def UCS(NODE_LIST, START_STATE, GOAL_STATE):
    """Run Uniform Cost Search on NODE_LIST"""
    #Create an empty queue.
    #USING A LIST HERE INSTEAD OF DEQUE!
    queue = []
    #Add Start node to queue
    queue.append(NODE_LIST[START_STATE])
    NODE_LIST[START_STATE].visited = True
    while len(queue) != 0:
        current_node = queue.pop(0)
        current_node.visited = True
        print " Current node is ", current_node.name
        if current_node.name == GOAL_STATE:
            print_solution(current_node, START_STATE, NODE_LIST)
            break
        #enqueue children of current_node
        for child in current_node.children:
            print current_node.children
            #split array contains 2 strings. [0] -> Name of child [1] -> Distance to child
            split = child.split(" ")
            node = NODE_LIST[split[0]]
            #Tie breaking
            # If the node has been visited and is present in the queue
            # Check for cumulativecost. If new cumulativecost < existing cumulativecost
            # replace the cumulativecost and parent.
            if node.visited != True:
                if node in queue:
                    if (current_node.cumulativecost + int(split[1])) < node.cumulativecost:
                        node.cumulativecost = current_node.cumulativecost + int(split[1])
                        node.parent = current_node.name
                        node.cumulative_heuristic = node.cumulativecost + node.heuristic
                        #First delete this node from the list
                        queue.remove(NODE_LIST[node.name])
                        #Then append the node at the right location using appendsort()
                        appendsort(queue, node)
                else:
            # It is a new node and so add it to the list using appendsort()
                    node.cumulativecost = current_node.cumulativecost + int(split[1])
                    node.parent = current_node.name
                    node.cumulative_heuristic = node.cumulativecost + node.heuristic
                    appendsort(queue, node)
                    print("Queue: ", [item.name for item in queue]);
        for elem in queue:
            print elem.name, "parent is", elem.parent, " cumulativecost is ", elem.cumulativecost

#A* Implementation
def ASTAR(NODE_LIST, START_STATE, GOAL_STATE):
    """Run A* Search on NODE_LIST"""
    #Create an empty queue.
    #USING A LIST HERE INSTEAD OF DEQUE!
    queue = []
    #Add Start node to queue
    queue.append(NODE_LIST[START_STATE])
    NODE_LIST[START_STATE].visited = True
    while len(queue) != 0:
        current_node = queue.pop(0)
        current_node.visited = True
        print " Current node is ", current_node.name
        if current_node.name == GOAL_STATE:
            print_solution(current_node, START_STATE, NODE_LIST)
            break
        #enqueue children of current_node
        for child in current_node.children:
            print current_node.children
            #split array contains 2 strings. [0] -> Name of child [1] -> Distance to child
            split = child.split(" ")
            node = NODE_LIST[split[0]]
            #Tie breaking
            # If the node has been visited and is present in the queue
            # Check for cumulativecost. If new cumulativecost < existing cumulativecost
            # replace the cumulativecost and parent.
            if node.visited != True:
                if node in queue:
                    if (current_node.cumulativecost + int(split[1])) < node.cumulativecost:
                        node.cumulativecost = current_node.cumulativecost + int(split[1])
                        node.cumulative_heuristic = node.cumulativecost + node.heuristic
                        node.parent = current_node.name
                        #First delete this node from the list
                        queue.remove(NODE_LIST[node.name])
                        #Then append the node at the right location using appendsort()
                        appendsort(queue, node)
                else:
            # It is a new node and so add it to the list using appendsort()
                    node.cumulativecost = current_node.cumulativecost + int(split[1])
                    node.parent = current_node.name
                    node.cumulative_heuristic = node.cumulativecost + node.heuristic
                    print node.name, node.cumulativecost, node.cumulative_heuristic
                    appendsort(queue, node)
        for elem in queue:
            print elem.name, "parent is", elem.parent, " cumulativecost is ", elem.cumulativecost, "cumulative_heuristic is ", elem.cumulative_heuristic


def appendsort(queue, node):
    #Find the position of the node in queue, whose cumulativecost is just greater than the cumulativecost of node.
    #append node at that index.
    i = 0
    #Special Case 1 - If queue is empty
    if len(queue) == 0:
        print("INSERTING AT BEGINNING: ", node.name)
        queue.append(node)
        return
    if node.name == "C":
        print
        print
        print queue[i].cumulative_heuristic <= node.cumulative_heuristic
        print queue[i].cumulative_heuristic
        print node.cumulative_heuristic
        print
        print
    while(queue[i].cumulative_heuristic <= node.cumulative_heuristic) and i < len(queue):
        i = i + 1
        if i == len(queue):
            break
    if i == len(queue):
        print("INSERTING AT ENDING: ", node.name)
        queue.append(node)
        return
    print("INSERTING: ", node.name, " AT POSITION: ", i)
    queue.insert(i, node)
    return



def print_solution(current_node, START_STATE, NODE_LIST):
    stack = deque()
    while current_node.name != START_STATE:
        stack.append(current_node)
        current_node = NODE_LIST[current_node.parent]
    stack.append(NODE_LIST[START_STATE])
    #Open file output.txt and write each line to output.txt
    filewriter = open("output.txt", "w")
    while len(stack) > 0:
        node = stack.pop()
        line_of_output = node.name + " " + str(node.cumulativecost) + "\n"
        filewriter.write(line_of_output)
    filewriter.close()
