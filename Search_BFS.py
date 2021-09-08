"""
Created on Tue Sep  7 15:50:04 2021

@author: anshuman_k
"""

# Reading Input Text File.
lines = []
with open('Input8.txt') as f:
    lines = f.readlines()
# Strip the \n read from the text file.
lines = list(map(lambda x:x.strip(),lines))

# Assigning the values to variables from the text file.
search_type = lines[0]

def convert_str_tuple_int(str_tuple):
    return tuple(map(lambda x: int(x), str_tuple))

# Storing as tuple
grid_size = convert_str_tuple_int(tuple(lines[1].split(" ")))
start_point = convert_str_tuple_int(tuple(lines[2].split(" ")))
end_point = convert_str_tuple_int(tuple(lines[3].split(" ")))

def fetch_next_step(coordinate: tuple, step: int):
    """
    Function to get the next node/action/step possible in the graph.
    Inputs:
        coordinate: Tuple of x,y,z cordinate of current node.
    Output:
        x: The X co-ordinate of the next node.
        y: The Y co-ordinate of the next node.
        z: The Z co-ordinate of the next node.
    """
    x = int(coordinate[0])
    y = int(coordinate[1])
    z = int(coordinate[2])
    if step == 1:
        return x+1, y, z
    if step == 2:
        return x-1, y, z
    if step == 3:
        return x, y+1, z
    if step == 4:
        return x, y-1, z
    if step == 5:
        return x, y, z+1
    if step == 6:
        return x, y, z-1
    if step == 7:
        return x+1, y+1, z
    if step == 8:
        return x+1, y-1, z
    if step == 9:
        return x-1, y+1, z
    if step == 10:
        return x-1, y-1, z
    if step == 11:
        return x+1, y, z+1
    if step == 12:
        return x+1, y, z-1
    if step == 13:
        return x-1, y, z+1
    if step == 14:
        return x-1, y, z-1
    if step == 15:
        return x, y+1, z+1
    if step == 16:
        return x, y+1, z-1
    if step == 17:
        return x, y-1, z+1
    if step == 18:
        return x, y-1, z-1

graph = {}

# Loop to form the graph.
for i in range(int(lines[4])):
    paths = []
    for j in range(len(lines[i+5].split())-3):
        next_step = fetch_next_step(tuple(lines[i+5].split()[:3]), 
                                    int(lines[i+5].split()[j+3]))
        paths.append(next_step)
        tuple_int = tuple(map(lambda s: int(s), 
                              tuple(lines[i+5].split()[:3])))
    graph.update({tuple_int: paths})
#print(graph)

def bfs_path_search(graph: dict, start_point: tuple, end_point: tuple):
    """
    Function to get the shortest path if available between two nodes else
    return "FAIL".
    Inputs:
        graph: Dictionary of graph with tuples inside representing 
        points/nodes.
        start_point: Tuple with the start point.
        end_point: Tuple with the end point.
    Output:
        
    """

    
    