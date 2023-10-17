from main import *

from inspect import stack
def get_line_number():
    return stack()[1].lineno

q = NQueensProblem(8)
expected = [7, 1, 3, 0, 6, 4, 2, 5]
observed = best_first_search(q).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = [0, 4, 7, 5, 2, 6, 1, 3]
observed = uniform_cost_search(q).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = [7, 1, 3, 0, 6, 4, 2, 5]
observed = a_star_search(q).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

romania_map = Graph(romania_roads, False)
romania_map.locations = romania_city_positions
g = GraphProblem('Arad', 'Bucharest', romania_map)
expected = ['Sibiu', 'Fagaras', 'Bucharest']
observed = best_first_search(g).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']
observed = uniform_cost_search(g).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest']
observed = a_star_search(g).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

e = EightPuzzle((3, 4, 1, 7, 6, 0, 2, 8, 5))
expected = ['LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'LEFT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT']
observed = best_first_search(e).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = ['DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN']
observed = a_star_search(e).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

map = Graph(best_graph_edges, True)
map.heuristics = best_graph_h
g = GraphProblem('S', 'G', map)
expected = ['B', 'G']
observed = best_first_search(g).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

map = Graph(uniform_graph_edges, True)
g = GraphProblem('S', 'G', map)
expected = ['A', 'D', 'G']
observed = uniform_cost_search(g).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

map = Graph(a_star_graph_edges, True)
map.heuristics = a_star_graph_admissible_h
g = GraphProblem('S', 'G', map)
expected = ['B', 'C', 'G']
observed = a_star_search(g).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

map.heuristics = a_star_graph_consistent_h
g = GraphProblem('S', 'G', map)
expected = ['A', 'C', 'G']
observed = a_star_search(g).solution()
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

eight_queens = NQueensProblem(8)
expected = 1
observed = eight_queens.g(0, (-1,-1,-1,-1, -1,-1,-1,-1), 7, ( 7,-1,-1,-1, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 2
observed = eight_queens.g(1, ( 7,-1,-1,-1, -1,-1,-1,-1), 1, ( 7, 1,-1,-1, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 3
observed = eight_queens.g(2, ( 7, 1,-1,-1, -1,-1,-1,-1), 3, ( 7, 1, 3,-1, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 4
observed = eight_queens.g(3, ( 7, 1, 3,-1, -1,-1,-1,-1), 0, ( 7, 1, 3, 0, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 5
observed = eight_queens.g(4, ( 7, 1, 3, 0, -1,-1,-1,-1), 6, ( 7, 1, 3, 0, 6,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 6
observed = eight_queens.g(5, ( 7, 1, 3, 0, 6,-1,-1,-1), 4, ( 7, 1, 3, 0, 6, 4,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 7
observed = eight_queens.g(6, ( 7, 1, 3, 0, 6, 4,-1,-1), 2, ( 7, 1, 3, 0, 6, 4, 2,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 8
observed = eight_queens.g(7, ( 7, 1, 3, 0, 6, 4, 2,-1), 5, ( 7, 1, 3, 0, 6, 4, 2, 5))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 56
observed = eight_queens.h((-1,-1,-1,-1, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 42
observed = eight_queens.h(( 7,-1,-1,-1, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 32
observed = eight_queens.h(( 7, 1,-1,-1, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 24
observed = eight_queens.h(( 7, 1, 3,-1, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 16
observed = eight_queens.h(( 7, 1, 3, 0, -1,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 8
observed = eight_queens.h(( 7, 1, 3, 0, 6,-1,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 4
observed = eight_queens.h(( 7, 1, 3, 0, 6, 4,-1,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 0
observed = eight_queens.h(( 7, 1, 3, 0, 6, 4, 2,-1))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 0
observed = eight_queens.h(( 7, 1, 3, 0, 6, 4, 2, 5))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

romania_map = Graph(romania_roads, False)
romania = GraphProblem('Arad', 'Bucharest', romania_map)
expected = 75
observed = romania.g(0, 'Arad', 'Zerind', 'Zerind')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 140
observed = romania.g(0, 'Arad', 'Sibiu', 'Sibiu')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 220
observed = romania.g(140, 'Sibiu', 'Rimnicu', 'Rimnicu')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 317
observed = romania.g(220, 'Rimnicu', 'Pitesti', 'Pitesti')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 418
observed = romania.g(317, 'Pitesti', 'Bucharest', 'Bucharest')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

romania_map = Graph(romania_roads, False)
romania = GraphProblem('Arad', 'Bucharest', romania_map)
expected = float('inf')
observed = romania.h('Arad')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = float('inf')
observed = romania.h('Sibiu')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = float('inf')
observed = romania.h('Fagaras')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = float('inf')
observed = romania.h('Pitesti')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = float('inf')
observed = romania.h('Rimnicu')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = float('inf')
observed = romania.h('Bucharest')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

romania_map = Graph(romania_roads, False)
romania_map.locations = romania_city_positions
romania = GraphProblem('Arad', 'Bucharest', romania_map)
expected = 350.2941620980858
observed = romania.h('Arad')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 232.69937687926884
observed = romania.h('Sibiu')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 154.62535367784935
observed = romania.h('Fagaras')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 89.89438247187641
observed = romania.h('Pitesti')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 186.48860555004427
observed = romania.h('Rimnicu')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 0.0
observed = romania.h('Bucharest')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

roads = dict(S = dict(A=1, B=2), A= dict(C=1), B = dict(C=2), C = dict(G=100))
roads_h = dict(S=90, A=100, B=88, C=100, G=0)
roads_map = Graph(roads, True)
roads_map.heuristics = roads_h
problem = GraphProblem('S', 'G', roads_map)
expected = 90
observed = problem.h('S')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 100
observed = problem.h('A')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 88
observed = problem.h('B')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 100
observed = problem.h('C')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 0
observed = problem.h('G')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,6,8,7,5,4,2,3),(0,1,2,3,4,5,6,7,8))
expected = (1, 0, 6, 8, 7, 5, 4, 2, 3)
observed = puzzle.init_state
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = (0, 1, 2, 3, 4, 5, 6, 7, 8)
observed = puzzle.goal_state
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
expected = (1, 0, 3, 4, 2, 5, 7, 8, 6)
observed = puzzle.init_state
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = (1, 2, 3, 4, 5, 6, 7, 8, 0)
observed = puzzle.goal_state
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
expected = ['DOWN', 'RIGHT']
observed = puzzle.actions((0,1,2,3,4,5,6,7,8))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = ['UP', 'LEFT', 'RIGHT']
observed = puzzle.actions((6,3,5,1,8,4,2,0,7))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = ['UP', 'DOWN', 'LEFT', 'RIGHT']
observed = puzzle.actions((4,8,1,6,0,2,3,5,7))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = ['DOWN', 'LEFT', 'RIGHT']
observed = puzzle.actions((1,0,6,8,7,5,4,2,3))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = ['UP', 'LEFT']
observed = puzzle.actions((1,2,3,4,5,6,7,8,0))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
expected = (3, 1, 2, 0, 4, 5, 6, 7, 8)
observed = puzzle.result((0,1,2,3,4,5,6,7,8), 'DOWN')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = (6, 3, 5, 1, 8, 4, 0, 2, 7)
observed = puzzle.result((6,3,5,1,8,4,2,0,7), 'LEFT')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = (3, 4, 0, 7, 6, 1, 2, 8, 5)
observed = puzzle.result((3,4,1,7,6,0,2,8,5), 'UP')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = (1, 8, 4, 7, 2, 6, 3, 5, 0)
observed = puzzle.result((1,8,4,7,2,6,3,0,5), 'RIGHT')
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,6,8,7,5,4,2,3),(0,1,2,3,4,5,6,7,8))
expected = False
observed = puzzle.goal_test((6,3,5,2,8,4,2,0,7))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = False
observed = puzzle.goal_test((1,2,3,4,5,6,7,8,0))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = True
observed = puzzle.goal_test((0,1,2,3,4,5,6,7,8))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,6,8,7,5,4,2,3))
expected = False
observed = puzzle.goal_test((6,3,5,2,8,4,2,0,7))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = False
observed = puzzle.goal_test((0,1,2,3,4,5,6,7,8))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = True
observed = puzzle.goal_test((1,2,3,4,5,6,7,8,0))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
expected = 1
observed = puzzle.g(0, (4,8,1,6,0,2,3,5,7), 'UP', (4,0,1,6,8,2,3,5,7))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 4
observed = puzzle.g(3, (8,0,1,4,6,2,3,5,7), 'DOWN', (8,6,1,4,0,2,3,5,7))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 9
observed = puzzle.g(8, (8,1,2,4,5,6,3,7,0), 'UP', (8,1,2,4,5,0,3,7,6))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 12
observed = puzzle.g(11, (1,2,8,4,5,6,3,0,7), 'RIGHT', (1,2,8,4,5,6,3,7,0))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
expected = 10
observed = puzzle.h((4,1,2,3,0,6,5,7,8))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 1
observed = puzzle.h((1,2,3,4,5,0,7,8,6))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 2
observed = puzzle.h((1,2,0,4,5,3,7,8,6))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 3
observed = puzzle.h((1,0,2,4,5,3,7,8,6))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 5
observed = puzzle.h((4,1,2,0,5,3,7,8,6))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

expected = 13
observed = puzzle.h((4,1,2,6,8,0,3,5,7))
if expected != observed:
    print('Failure at line %d: Expected %s, but got %s' % (get_line_number(), repr(expected), repr(observed)))

print('DONE')
