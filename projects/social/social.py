import random 

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes num of users and an average num of friendships as args

        Creates that num of users and randomly distributed friendships
        between them.

        Users num > avg number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(num_users):
            self.add_user(f'User {i+1}')

        # Create friendships
        # create N random friendships
        # create all possible friendships
        # shuffle list, grab the first N elements from list
        possible_friendships=[]
        for user_id in self.users: # for loop in for loop = O(n^2) 
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        # create N friendships where n = avg_friendships * num_users // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship( (friendship[0], friendship[1])
)
    def get_all_social_paths(self, user_id):
        """
        Return dict with every user in user's extended network 
        with the shortest friendship path between them:

        ( key: friend's ID, value: path )
        
        """
        qq = Queue() # a Queue creates a list - Our PATH!

        qq.enqueu([user_id])
        
        visited = {}  # DICT (not set) of all user's friends' user_ids

        while qq.size() > 0:
            path = qq.dequeue()

            v=path[-1]

            if v not in visited:
                visited[v] = path # this builds a dict of paths from start to everyone else

            for neighbor in self.friendships[v]:
                path_copy = path.copy()
                path_copy.append(neighbor)
                qq.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
