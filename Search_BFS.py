"""
@author: Anshuman Dey Kirty
Code Structure:
    Functions
    Script (main)
"""
# Libraries
import sys
import numpy as np
from queue import PriorityQueue


def convert_str_tuple_int(str_tuple):
    """
    Function to convert tuple with strings to tuple with int.
    Input:
        str_tuple: String Tuple
    Output:
        Tuple with int values.
    """
    return tuple(map(lambda x: int(x), str_tuple))


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
        return x + 1, y, z
    if step == 2:
        return x - 1, y, z
    if step == 3:
        return x, y + 1, z
    if step == 4:
        return x, y - 1, z
    if step == 5:
        return x, y, z + 1
    if step == 6:
        return x, y, z - 1
    if step == 7:
        return x + 1, y + 1, z
    if step == 8:
        return x + 1, y - 1, z
    if step == 9:
        return x - 1, y + 1, z
    if step == 10:
        return x - 1, y - 1, z
    if step == 11:
        return x + 1, y, z + 1
    if step == 12:
        return x + 1, y, z - 1
    if step == 13:
        return x - 1, y, z + 1
    if step == 14:
        return x - 1, y, z - 1
    if step == 15:
        return x, y + 1, z + 1
    if step == 16:
        return x, y + 1, z - 1
    if step == 17:
        return x, y - 1, z + 1
    if step == 18:
        return x, y - 1, z - 1


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
        path_length: Int
        nodes_num: Int
        nodes: List

    """
    visited = {}
    for key in graph.keys():
        visited[key] = 0
    tracker = [[start_point]]
    while len(tracker) > 0:
        temp = tracker[0]
        tracker = tracker[1:]
        on = temp[-1]
        if visited[on] == 0:
            visited[on] = 1
            neighbours = graph[on]
            for neighbour in neighbours:
                short_path = list(temp)
                short_path.append(neighbour)
                tracker.append(short_path)
                if neighbour == end_point:
                    return short_path
    textfile = open(output_file, "w")
    textfile.write("FAIL")
    sys.exit()


def get_distance(t1: tuple, t2: tuple):
    a = np.array(t1)
    b = np.array(t2)
    dist = np.linalg.norm(a - b)
    if dist == 1:
        return 10
    else:
        return 14


def graph_with_distance(graph: dict):
    dist_graph = {}
    for key in graph.keys():
        path = {}
        for i in range(len(graph[key])):
            path.update({graph[key][i]: get_distance(key, graph[key][i])})
        dist_graph.update({key: path})
    return dist_graph


def ucs_path_search(graph: dict, start_point: tuple, end_point: tuple):
    visited = {}
    for key in graph.keys():
        visited[key] = 0
    tracker = PriorityQueue()
    tracker.put((0, (start_point), [start_point]))
    while not tracker.empty():
        cost, on, short_path = tracker.get()
        if visited[on] == 0:
            visited[on] = 1
            neighbours = graph[on]
            for neighbour in neighbours:
                # if visited[neighbour] == 0:
                total_cost = cost + get_distance(on, neighbour)
                tracker.put((total_cost, neighbour, short_path + [neighbour]))
                if neighbour == end_point:
                    return (total_cost, short_path + [neighbour])
    textfile = open(output_file, "w")
    textfile.write("FAIL")
    sys.exit()


def write_output(path_length: int, nodes_num: int, short_path: list, search_type: str):
    if search_type == "BFS":
        textfile = open(output_file, "w")
        textfile.write(str(path_length) + "\n")
        textfile.write(str(nodes_num) + "\n")
        for i in range(len(short_path)):
            if i == 0:
                textfile.write(" ".join(map(str, short_path[i])) + " 0\n")
            elif i == len(short_path) - 1:
                textfile.write(" ".join(map(str, short_path[i])) + " 1")
            else:
                textfile.write(" ".join(map(str, short_path[i])) + " 1\n")
    elif search_type == "UCS":
        textfile = open(output_file, "w")
        textfile.write(str(path_length) + "\n")
        textfile.write(str(nodes_num) + "\n")
        for i in range(len(short_path)):
            if i == 0:
                textfile.write(" ".join(map(str, short_path[i])) + " 0\n")
                temp = short_path[i]
            elif i == len(short_path) - 1:
                textfile.write(
                    " ".join(map(str, short_path[i]))
                    + " "
                    + str(get_distance(short_path[i], temp))
                )
            else:
                textfile.write(
                    " ".join(map(str, short_path[i]))
                    + " "
                    + str(get_distance(short_path[i], temp))
                    + "\n"
                )
                temp = short_path[i]


# Main Code
# Reading Input Text File.
lines = []
input_file = "../Input6.txt"
output_file = "../Output.txt"
with open(input_file) as f:
    lines = f.readlines()
# Strip the \n read from the text file.
lines = list(map(lambda x: x.strip(), lines))

# Assigning the values to variables from the text file.
search_type = lines[0]

# Storing as tuple
grid_size = convert_str_tuple_int(tuple(lines[1].split(" ")))
start_point = convert_str_tuple_int(tuple(lines[2].split(" ")))
end_point = convert_str_tuple_int(tuple(lines[3].split(" ")))

graph = {}

# Loop to form the graph.
for i in range(int(lines[4])):
    paths = []
    for j in range(len(lines[i + 5].split()) - 3):
        next_step = fetch_next_step(
            tuple(lines[i + 5].split()[:3]), int(lines[i + 5].split()[j + 3])
        )
        paths.append(next_step)
        tuple_int = convert_str_tuple_int(tuple(lines[i + 5].split()[:3]))
    graph.update({tuple_int: paths})
    # print(graph)

# Edge Case
if end_point == start_point:
    ls = []
    ls.append(start_point)
    write_output(0, 1, ls)
    sys.exit()

if search_type == "BFS":
    short_path = bfs_path_search(graph, start_point, end_point)
    write_output(len(short_path) - 1, len(short_path), short_path, search_type)
elif search_type == "UCS":
    cost, short_path = ucs_path_search(graph, start_point, end_point)
    write_output(cost, len(short_path), short_path, search_type)
elif search_type == "A*":
    cost, short_path = astar()
