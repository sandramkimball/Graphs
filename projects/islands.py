# Write a function that takes a 2D binary array and returns the number of 1 islands (connected components). 
# An island consists of 1s that are connected to the n, s, e, w.

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4 

# translate problem into graph terminology: undirected, cyclic, nodes, edges?
# build the graph
# traverse the graph

def island_counter(matrix):
    # create entirely diff visited matrix (a 2d array)
    visited = [] 
    for i in range(len(matrix)): # this gets the height/rows
        visited.append( [False] * len(matrix[0]) )
    island_count = 0
    # for all nodes:
    for col in range(len(matrix[0])):
        for row in range(len(matrix[0])):
            # if node is not visited:
            if not visited[row][col]:
            # if we hit a 1 not visited, 
                if matrix[row][col] == 1:
                    # mark visited and increment count
                    # traverse all connected nodes, mark as visited
                    visited = dft(row, col, matrix, visited)
                    island_count += 1
    return island_count


def dft(row, col, matrix, visited):
    # do a df traversal
    # return updated visited matrix with all conn comp marked visited
    s = Stack()
    s.push((start_row, start_col))
    while s.size() > 0:
        v = s.pop()
        row = v[0]
        col = [1]

        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in self.get_neighbors(row, col, matrix):
                s.push(neighbor)
    return visited


def get_neighbors(row, col, matrix):
    neighbors = []
    # check north
    if row > 0 and matrix[row-1][col]:
        neighbors.append( (row-1, col) )
    # check south
    if row < len(matrix) -1 and matrix[row+1][col]:
        neighors.append( (row+1, col) )
    # check east
    if col < len(matrix[0]) - 1 and matrix[row][col-1] == 1:
        neighbors.append( (col, row-1) )
    # check west
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append( (col, row+1) )
