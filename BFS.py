import sys
from collections import deque

from utilities import *

class SokobanProblem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        player_pos = get_player_position(state)
        player_pos = [int(player_pos[0]), int(player_pos[1])]
        for act, pos in POS_PLAYER_MOVE.items():
            if not can_move(state, (player_pos[0] + pos[0], player_pos[1] + pos[1]), act):
                possible_actions.remove(act)
        return possible_actions

    def result(self, state, action):
        player_pos = get_player_position(state)
        player_pos = [int(player_pos[0]), int(player_pos[1])]
        new_state = list(map(list,state))
        next_player_pos = (player_pos[0] + POS_PLAYER_MOVE[action][0], player_pos[1] + POS_PLAYER_MOVE[action][1])
        if new_state[next_player_pos[0]][next_player_pos[1]] == '*':
            next_box_pos = (next_player_pos[0] + POS_PLAYER_MOVE[action][0], next_player_pos[1] + POS_PLAYER_MOVE[action][1])
            new_state[next_player_pos[0]][next_player_pos[1]], new_state[next_box_pos[0]][next_box_pos[1]] = new_state[next_box_pos[0]][next_box_pos[1]], new_state[next_player_pos[0]][next_player_pos[1]]
        new_state[next_player_pos[0]][next_player_pos[1]], new_state[player_pos[0]][player_pos[1]] = new_state[player_pos[0]][player_pos[1]], new_state[next_player_pos[0]][next_player_pos[1]]
        if new_state[player_pos[0]][player_pos[1]] == 'g':
            new_state[player_pos[0]][player_pos[1]] = '0'
        return tuple(map(tuple,new_state))

    def goal_test(self, state):
        count = 0
        index = 0
        list_position = get_box_position(state)
        for i in list_position:
            if i[0] == self.goal[index][0] and i[1] == self.goal[index][1]:
                count +=1
            index += 1
        if count == len(self.goal):
            return True
        return False

    def path_cost(self, c, state1, action, state2):
        return c + 1     

    def find_blank_square(self, state):
        return state.index(0)
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
        return tuple([self.child_node(problem, action)
                for action in problem.actions(self.state)])

    def child_node(self, problem, action):
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        return [node.action for node in self.path()[1:]]

    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


def BFS(problem):
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
      



    