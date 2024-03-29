#######################################################
# Author:   Quinn Trate
# Date:     October 17, 2023
# Class:    CMPSC 441 Artificial Intelligence
# Language: Python
# Purpose:  Constructor for Main
#######################################################


class Problem:

    
    def __init__ (self, init_state, goal_state=None):
        """ Initialization """
        self.init_state = init_state
        self.goal_state = goal_state

        
    def actions(self, state):
        """ Returns the List of Actions that can be Executed in the Current State """
        pass

    
    def result(self, state, action):
        """ Returns the State that Results from Executing the Current Action in the Current State """
        pass
    

    def goal_test(self, state):
        """ Returns True if the Current State is a Current State and False Otherwise """
        pass
    

    def g(self, cost, from_state, action, to_state):
        """
        Returns the Path Cost from the Root to to_state via from_state.
        The Current Cost is the Path Cost from the Root to from_state 
        and the Current Action will Lead from from_state to to_state.  
        """
        pass
    

    def h(self, state):
        """ Returns the Heuristic Value at this State """
        pass
    
    



class Node:
    """
    Represents a Node in a Search Tree. It Contains the Current State,
    the Pointer to the Parent Node, and the Action that Leads to the
    Current Node from the Parent Node.
    """

    def __init__ (self, state, parent=None, action=None, path_cost=0, heuristic=0):
        """ Creates a Search Tree Node that Results from Executing the Current Action from the Parent Node """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

            
    def expand(self, problem):
        """ Returns the List of Child Nodes, i.e., the List of Nodes Reachable from this Node in one Step """
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]
    

    def child_node(self, problem, action):
        """ Returns the Node that Results from Executing the Current Action in this Node """
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
                         problem.g(self.path_cost, self.state,
                                   action, next_state),
                         problem.h(next_state))
        return next_node

    
    def solution(self):
        """ Returns the Sequence of Actions that Leads to this Node from the Root Node """
        if self.state == None:
            return None
        return [node.action for node in self.path()[1:]]
    

    def path(self):
        """ Returns a List of Nodes from the Root to this Node """
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


    def __repr__(self):
        return "<Node {}(g={}, h={})>".format(self.state, self.path_cost, self.heuristic)


    def __eq__(self, other):
        """
        Used for 'in' operator. It Treats the Nodes
        with the Same State as Equal (Since Breadth
        First Graph Search and A* Search Should Have
        no Duplicated States). This Might not be
        What you Want in Other Contexts
        """
        return isinstance(other, Node) and self.state == other.state




class Graph:
    """
    A Graph Connects Vertices by Edges. Each Edge can Have a Length
    Associated with it. The Edges are Represented as a Dictionary
    of the Following Form:
       edges = { 'A' : {'B':1, 'C':2}, 'B' : {'C':2, 'D':2} }

    Creating an Instance of Graph as 
         g = Graph(edges)
    Instantiates a Directed Graph with 4 Vertices A, B, C, and D with
    the Edge of Length 1 from A to B, Length 2 from A to C, Length 2
    from B to C, and Length 2 from B to D.

    Creating an Instance of Graph as
         g = Graph(edges, False)
    Instantiates an Undirected Graph by Adding the Inverse Edges, so
    that the Edges Become:
        { 'A' : {'B':1, 'C':2},
          'B' : {'A':1, 'C':2, 'D':2},
          'C' : {'A':2, 'B':2},
          'D' : {'B':2} }
    """

    def __init__(self, edges=None, directed=True):
        """ Initialization """
        self.edges = edges or {}
        self.directed = directed
        if not directed:
            for x in list(self.edges.keys()):
                for (y, dist) in self.edges[x].items():
                    self.edges.setdefault(y,{})[x] = dist

                    
    def get(self, x, y=None):
        """ Returns the Distance from x to y, or the Distances to Cities Reachable from x """
        edges = self.edges.setdefault(x,{})
        if y is None:
            return edges
        else:
            return edges.get(y)
        

    def vertices(self):
        """ Returns the List of Vertices in the Graph """
        s = set([x for x in self.edges.keys()])
        t = set([y for v in self.edges.values() for (y,d) in v.items()])
        v = s.union(t)
        return list(v)

    
    def __repr__(self):
        return "<Graph {}>".format(self.edges)





# Example Graph - Romania Map
romania_roads = dict(
    Arad      = dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest = dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova   = dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta   = dict(Mehadia=75),
    Eforie    = dict(Hirsova=86),
    Fagaras   = dict(Sibiu=99),
    Hirsova   = dict(Urziceni=98),
    Iasi      = dict(Vaslui=92, Neamt=87),
    Lugoj     = dict(Timisoara=111, Mehadia=70),
    Oradea    = dict(Zerind=71, Sibiu=151),
    Pitesti   = dict(Rimnicu=97),
    Rimnicu   = dict(Sibiu=80),
    Urziceni  = dict(Vaslui=142)
    )

romania_city_positions = dict(
    Arad    = ( 91, 492),  Bucharest = (400, 327),  Craiova  = (253, 288),
    Drobeta = (165, 299),  Eforie    = (562, 293),  Fagaras  = (305, 449),
    Giurgiu = (375, 270),  Hirsova   = (534, 350),  Iasi     = (473, 506),
    Lugoj   = (165, 379),  Mehadia   = (168, 339),  Neamt    = (406, 537),
    Oradea  = (131, 571),  Pitesti   = (320, 368),  Rimnicu  = (233, 410),
    Sibiu   = (207, 457),  Timisoara = ( 94, 410),  Urziceni = (456, 350),
    Vaslui  = (509, 444),  Zerind    = (108, 531)
    )





# Example Graphs with Heuristicss
best_graph_edges = dict(
    S = dict(A=2, B=5),
    A = dict(C=2, D=4),
    B = dict(D=1, G=5),
    D = dict(C=3, G=2)
    )
best_graph_h = dict(S=10, A=2, B=3, C=1, D=4, G=0)


uniform_graph_edges = dict(
    S = dict(A=2, B=5),
    A = dict(C=2, D=4),
    B = dict(D=1, G=5),
    D = dict(C=3, G=2)
    )


a_star_graph_edges = dict(
    S = dict(A=1, B=2),
    A = dict(C=1),
    B = dict(C=2),
    C = dict(G=100)
    )
a_star_graph_admissible_h = dict( S=90, A=100, B=1, C=90, G=0 )
a_star_graph_consistent_h = dict( S=90, A=100, B=88, C=100, G=0 )
