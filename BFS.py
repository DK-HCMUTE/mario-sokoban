# [SHARED WITH AI CLASSES] week05 exercise
'''
The code below is INCOMPLETE. You need to implement the following functions:
1. depth_limited_search()  
2. iterative_deepening_search() 

HINT: Function breadth_first_graph_search() is for your reference (Its usage is demonstrated in the __main__ part (line 154)). Read it to understand the given code.
'''


import sys
from collections import deque

from sympy import true
from utilities import *


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


def BFS(problem):
    """Bread first search (GRAPH SEARCH version)
    See [Figure 3.11] for the algorithm"""

    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None
      


  
  

class SokobanProblem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        
        return possible_actions

    def result(self, state, action):
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        count = 0
        list_position = get_position(state)
        for i in list_position:
            if i in self.goal:
                count +=1
        if count == len(self.goal):
            return True
        return False

    def path_cost(self, c, state1, action, state2):
        return c + 1     

    def find_blank_square(self, state):
        return state.index(0)


    