from util import Stack


def get_parents(ancestors, starting_node):
    # for i in ancestors:
    #     if i == starting_node:
    #         return i + 1


    if starting_node in ancestors:
        return ancestors[starting_node]
    else:
        print('Error: does not exist')
        raise ValueException

# dft O(n)?
def earliest_ancestor(ancestors, starting_node):
    # create a stack
    s = Stack()
    # push start to stack
    s.push(starting_node)
    # create a set for visited
    visited = set()
    # while stack is full:
    while s.size() > 0:
    #     pop first vertex in stack
        v = s.pop()
    #     check if visited. if not:
        if v not in visited:
    #         mark as visited
            visited.add(v)
    #         push parent onto stack
            for parent in get_parents(ancestors, v):
                s.push(parent)

    if len(ancestors) == 2:
        return ancestors.sort()[0]