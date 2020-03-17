from util import Stack, Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
       self.vertices[vertex_id] = new Set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('Error, cannot add edge.')

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('Error, vertex does not exist.')
            raise ValueException

#   PART 2
#   Sets = no duplicates, 0(1)
#   though arrays are better for memory
#   Graphs vs Trees: graphs are cycles

    def bft(self, starting_vertex):
        # create a queue
        q = Queue()
        # enqueue starting vertex
        q.enqueue(starting_vertex)
        #create a set to store visited vertices
        visited = set()
        #while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # check if its been vistited. if not...
            if v not in visited:
                #mark as visited
                print(v)
                visited.add(v)
                #enqueue its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        #just change bft's queue to stack
        # create a stack
        s = Stack()
        # push the starting vertex
        s.push(starting_vertex)
        # create a set to store visited
        visited = set()
        # while stack is full:
        while s.size() > 0:
            # pop first vertex
            v = s.pop()
            # check if visited. if not:
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                # push its neigbor onto stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        if visited is None:
            visited = set()
        #Check if node has been visited. if not:
        if starting_vertex not in visited:
            # mark as visited
            visited.add(starting_vertex)
            # call dft_recursive on neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                dft_recursive(neighbor)


    def bfs(self, starting_vertex, destination_vertex):
        # create a queue
        q = Queue()
        # enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # create a set to store visitied v
        visited = set()
        # while queue is full:
        while q.size > 0:
            # dequeue first PATH
            path = path.dequeue()
            # GRAB VERTEX FROM END OF PATH
            v = path[-1]
            # check if visited. if not:
            if v not in visited:
                # mark as visited
                visited.add(v)
                # CHECK IF ITS THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
            # Enqueue PATH to its neighbros
            for neighbor in self.get_neighbors(v):
                # MAKE A COPY OF PATH
                path_copy = path.copy()
                # ENQUEUE THE COPY
                path_copy.enqueue()

    def dfs(self, starting_vertex, destination_vertex):
        # create a stack
        s = Stack()
        # push A PATH TO the starting vertex
        path = path + [starting_vertex]
        s.push(path)
        # create a set to store visitied v
        visited = set()
        # while stack is full:
        while s.size > 0:
            # pop first PATH
            path = s.pop()
            # GRAB VERTEX FROM END OF PATH
            v = path[-1]
            # check if visited. if not:
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                # CHECK IF ITS THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
            # Enqueue PATH to its neighbros
            for neighbor in self.get_neighbors(path):
                # MAKE A COPY OF PATH
                path_copy = path.copy()
                # PUSH THE COPY
                s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None:
            visitied = set()

        if path is None:
            path = []

        visited.add(starting_vertex)
        path_copy = path.copy()
        path_copy.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path_copy

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()

        else neighbor in self.get_neighbors(starting_vertex):
            new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
            if new_path is not None:
                return new_path
            else:
                return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
