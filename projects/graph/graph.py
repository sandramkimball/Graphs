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
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size > 0:
            #Check if node has been visited. if not:
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                # call dft_recursive on neighbors
                for neighbor in self.get_neighbors(v):
                    dft_recursive(neighbor)


    def bfs(self, starting_vertex, destination_vertex):
        # create a queue
        q = Queue()
        # enqueue A PATH TO the starting vertex
        path = path + [starting_vertex]
        q.enqueue(path)
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
                print(v)
                visited.add(v)
                # CHECK IF ITS THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
            # Enqueue PATH to its neighbros
            for neighbor in self.get_neighbors(path):
                # MAKE A COPY OF PATH
                path.copy()
                # ENQUEUE THE COPY
                path.enqueue()

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
                path.copy()
                # ENQUEUE THE COPY
                s.push(path)

    def dfs_recursive(self, starting_vertex):
        s = Stack()
        path = path + [starting_vertex]
        s.push(path)
        visited = set()

        while s.size > 0:
            path = s.pop()
            v = path[-1]
            
            if v not in visited:
                print(v)
                visited.add(v)
                if v == destination_vertex:
                    return path

            for neighbor in self.get_neighbors(path):
                dfs_recursive(neighbor)

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
