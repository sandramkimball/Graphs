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
        #Check if node has been visited
        # if not:
        #   mark as visited
        #   call dft_recursive on neighbors

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        # enqueue A PATH TO the starting vertex
        # create a set to store visitied v
        # while queue is full:
        #   dequeue first PATH
        #   GRAB BERTEX FROM END OF PATH
        #   check if visited. if not:
        #       mark as visited
        #       CHECK IF ITS THE TARGET
        #       IF SO, RETURN PATH
        #   Enqueue PATH TO all neighbros
        #       MAKE A COPY OF PATH
        #       ENQUEUE THE COPY

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
