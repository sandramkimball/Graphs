from util import Stack, Queue
# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. .
# Return None if there is no such transformation sequence.
# All lowercase.
# Assume no duplicates in the word list.
# Assume begin_word and end_word are non-empty and not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# 1. Translate problem into graph terms
# 2. Build graph
# 3. Traverse graph (which algorithm we gonna use?) Bfs - shortest path
f = open('words.txt', 'r')
word_set = set( f.read().lower().split("\n") )
f.close()


def words_are_neighbors(w1, w2):
    # go through each letter of word, switch with each letter in alphabet, check if equals given word
    list_word = list(w1)
    for i in range(len(list_word)):
        for letter in ['a', 'b', 'c']:
            temp_word = list_word.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word == in word_set and joined_word != word:
                results.append(temp_word)
            
    return results
    # for loop in for loop = O(26n) = O(n)

def get_neighbors(word):
    return neighbors[word]

def word_ladder(self, begin_word, end_word):
    q = Queue()
    q.enqeue([begin_word])
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        w = path[-1]
        if w == end_word:
            return path
        if w not in visited:
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)

# BIG O(n^2)?
neighbors = {}

for word in words: 
    words[word] = set()
    for potential_neighbor in words:
        if words_are_neighbors(word, potential_neighbor):
            words[word].add(potential_neighbor)

