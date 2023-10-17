#######################################################
# Author:   Quinn Trate
# Date:     October 17, 2023
# Class:    CMPSC 441 Artificial Intelligence
# Language: Python
# Purpose:  Implements the Five Main Search
#           Algorithms for the N-Queens, Farmers,
#           and Eight-Puzzle Problems.
#######################################################


# Imports
from constructor import *
from collections import deque
import math


# Search Algorithm Functions
def helper(frontier, function):
    temp = deque()
    lst = []
    for i in range(len(frontier)):
        lst.append(frontier.popleft())
    lst.sort(key = function)
    for node in lst:
        if node not in temp:
            temp.append(node)
    return temp


def breadth_first_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])
    explored = [problem.init_state]
    while len(frontier) > 0:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        for i in node.expand(problem):
            if i.state not in explored:
                explored.append(i.state)
                frontier.append(i)
    return Node(None)


def depth_first_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])
    explored = [problem.init_state]
    while len(frontier) > 0:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        for i in node.expand(problem):
            if i.state not in explored:
                explored.append(i.state)
                frontier.append(i)
    return Node(None)


def best_first_search(problem):
    node = Node(problem.init_state, heuristic = problem.h(problem.init_state))
    frontier = deque([node])
    explored = [problem.init_state]
    while len(frontier) > 0:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        for i in node.expand(problem):
            if i.state not in explored:
                explored.append(i.state)
                frontier.append(i)
        frontier = helper(frontier, (lambda node : node.heuristic))
    return Node(None)


def uniform_cost_search(problem):
    node = Node(problem.init_state)
    frontier = deque([node])
    explored = []
    while len(frontier) > 0:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        if node.state in explored:
            continue
        explored.append(node.state)
        for i in problem.actions(node.state):
            if problem.result(node.state, i) not in explored:
                if node.child_node(problem, i) not in frontier:
                    frontier.append(node.child_node(problem, i))
                else:
                    for j in frontier:
                        if j == node.child_node(problem, i) and node.child_node(problem, i).path_cost < j.path_cost:
                            frontier.remove(j)
                            frontier.append(node.child_node(problem, i))
                            break
        frontier = helper(frontier, (lambda node : node.path_cost))
    return Node(None)


def a_star_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])
    explored = []
    while len(frontier) > 0:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        if node.state in explored:
            continue
        explored.append(node.state)
        for i in problem.actions(node.state):
            if problem.result(node.state, i) not in explored:
                if node.child_node(problem, i) not in frontier:
                    frontier.append(node.child_node(problem, i))
                else:
                    for j in frontier:
                        if j == node.child_node(problem, i) and node.child_node(problem, i).path_cost < j.path_cost:
                            frontier.remove(j)
                            frontier.append(node.child_node(problem, i))
                            break
        frontier = helper(frontier, (lambda node : node.path_cost + node.heuristic))
    return Node(None)





# N-Queens Problem
class NQueensProblem(Problem):


    def __init__(self, n):
        """ Initialization """
        super().__init__(tuple([-1] * n))
        self.n = n


    def actions(self, state):
        """ Returns Valid Actions """
        if -1 not in state:
            return []
        empty = state.index(-1)
        arr = [i for i in range(0, len(state))]
        for column in range(0, empty):
            for hit in [state[column], state [column] - (empty - column), state[column] + (empty - column)]:
               if hit in arr:
                   arr.remove(hit)
        return arr


    def result(self, state, action):
        """ Returns Result of a Move """
        arr = []
        for elem in state:
            if elem == -1:
                break
            arr.append(elem)
        arr.append(action)
        for i in range(0, state.count(-1) - 1):
            arr.append(-1)
        return tuple(arr)


    def goal_test(self, state):
        """ Tests if the Current State is the Goal State """
        if -1 in state:
            return False
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                    return False
        return True


    def g(self, cost, from_state, action, to_state):
        """ Returns the Cost of a Move. Since N-Queens Takes Place on a Game Board, Each Move Costs 1 Value """
        return cost + 1


    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the total number of conflicts in the given
        state as a heuristic value for the state.
        """
        temp = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j]:
                    temp += 1
                if abs(state[i] - state[j]) == abs(i - j):
                    temp += 1
        return temp * 2





# Farmer's Problem
class FarmerProblem(Problem):


    def __init__(self, init_state, goal_state = (False, False, False, False)):
        """ Initialization """
        super().__init__(init_state, goal_state)


    def actions(self, state):
        """ Returns Valid Actions """
        arr = []
        for i in range(0, len(state)):
            if state[0] != state[i]:
                continue
            lst = list(state)
            lst[0] = not lst[0]
            if i > 0:
                lst[i] = not lst[i]
            valid = True
            for j in range(1, len(state) - 1):
                if lst[0] != lst[j] and lst[j] == lst[j + 1]:
                    valid = False
            if valid:
                if i == 0:
                    arr.append('F')
                elif i == 1:
                    arr.append('FG')
                elif i == 2:
                    arr.append('FC')
                elif i == 3:
                    arr.append('FX')
                else:
                    raise Exception("Not Proper Move")
        return arr

    
    def result(self, state, action):
        """ Returns Result of a Move """
        arr = list(state)
        arr[0] = not arr[0]
        if action == 'F':
            index = 0
        elif action == 'FG':
            index = 1
        elif action == 'FC':
            index = 2
        elif action == 'FX':
            index = 3
        else:
            raise Exception("Not Proper Move")
        if index != 0:
            arr[index] = not arr[index]
        return tuple(arr)

    
    def goal_test(self, state):
        """ Tests if the Current State is the Goal State """
        return state == self.goal_state





# Graph Problem
class GraphProblem(Problem):

    
    def __init__(self, init_state, goal_state, graph):
        """ Initialization """
        super().__init__(init_state, goal_state)
        self.graph = graph

   
    def actions(self, state):
        """ Returns the List of Adjacent States from the Current State """
        return list(self.graph.get(state).keys())

    
    def result(self, state, action):
        """ Returns the Resulting State by Taking the Given Action """
        return action

    
    def goal_test(self, state):
        """ Tests if the Current State is the Goal State """
        return state == self.goal_state

    
    def g(self, cost, from_state, action, to_state):
        """ Returns the Cost of a Move From the Current State to to_State """
        return cost + self.graph.get(from_state, to_state)
    

    def h(self, state):
        """
        Returns the Heuristic Value for the Current State and is Calculated as Follows:
        1. If an Attribute Called 'heuristics' Exists:
            - Heuristics Must be a Dictionary of States as Keys and Corresponding Heuristic Values as Values
            - Returns the Heuristic Value for the Current State
        2. If an Attribute Called 'locations' Exists:
            - Locations Must be a Dictionary of States as Keys and Corresponding GPS Coordinates (x, y) as Values
            - Returns the Euclidean Norm from the Current State to the Goal State
        3. Else:
            - Cannot Calculate Heuristic Value for the Current State
            - Return Infinity
        """
        if hasattr(self.graph, 'heuristics'):
            return self.graph.heuristics[state]
        elif hasattr(self.graph, 'locations'):
            curr = self.graph.locations[state]
            goal = self.graph.locations[self.goal_state]
            return math.sqrt((goal[0] - curr[0]) ** 2 + (goal[1] - curr[1]) ** 2)
        else:
            return math.inf





# Eight Puzzle
class EightPuzzle(Problem):


    def __init__(self, init_state, goal_state=(1,2,3,4,5,6,7,8,0)):
        """ Initialization """
        super().__init__(init_state, goal_state)

    
    def actions(self, state):
        """ Returns Valid Actions """
        dct = {
            0: ['DOWN', 'RIGHT'],
            1: ['DOWN', 'LEFT', 'RIGHT'],
            2: ['DOWN', 'LEFT'],
            3: ['UP', 'DOWN', 'RIGHT'],
            4: ['UP', 'DOWN', 'LEFT', 'RIGHT'],
            5: ['UP', 'DOWN', 'LEFT'],
            6: ['UP', 'RIGHT'],
            7: ['UP', 'LEFT', 'RIGHT'],
            8: ['UP', 'LEFT']
        }
        if state.count(0) != 1:
            raise Exception("No Blank Space in Eight Puzzle")
        return dct[state.index(0)]
    
    
    def result(self, state, action):
        """ Returns Result of a Move by Swapping the Blank Space with the Adjacent Space """
        lst = list(state)
        for i in range(9):
            if lst[i] == 0:
                if action == 'UP':
                    if 0 <= i - 3 < len(lst):
                        temp = lst[i]
                        lst[i] = lst[i - 3]
                        lst[i - 3] = temp
                        break
                    else:
                        continue
                elif action == 'DOWN':
                    if 0 <= i + 3 < len(lst):
                        temp = lst[i]
                        lst[i] = lst[i + 3]
                        lst[i + 3] = temp
                        break
                    else:
                        continue
                elif action == 'LEFT':
                    if 0 <= i - 1 < len(lst):
                        temp = lst[i]
                        lst[i] = lst[i - 1]
                        lst[i - 1] = temp
                        break
                    else:
                        continue
                elif action == 'RIGHT':
                    if 0 <= i + 1 < len(lst):
                        temp = lst[i]
                        lst[i] = lst[i + 1]
                        lst[i + 1] = temp
                        break
                    else:
                        continue
                else:
                    raise Exception("Not Legal Move")
        else:
            raise Exception("No Blank Space in Eight Puzzle or Not Legal Move")
        state = tuple(lst)
        return state

    
    def goal_test(self, state):
        """ Tests if the Current State is the Goal State """
        return state == self.goal_state
    

    def g(self, cost, from_state, action, to_state):
        """ Returns the Cost of a Move. Since 8-Puzzle Takes Place on a Game Board, Each Move Costs 1 Value """
        return cost + 1
    

    def h(self, state):
        """ Returns the Sum of the Manhattan Distances of Misplaced Tiles to Their Final Positions as the Heuristic Value for the Current State """
        temp = 0
        for i in range(9):
            if state[i] != 0:
                temp += abs((i // 3) - (self.goal_state.index(state[i]) // 3)) + abs((i % 3) - (self.goal_state.index(state[i]) % 3))
        return temp
