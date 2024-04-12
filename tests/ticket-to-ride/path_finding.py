from math import sqrt
import sys
from typing import Dict, List, Set, Tuple
from priority_queue import PriorityQueue
from adjacency_list import AdjacencyListGraph

# You do not need to change this class.  It is used as the return type for get_minimum_path
class RouteInfo:
    def __init__(self, 
                 route: List[Tuple[str, str]], # list of tuples of friendly names for the start and destination cities
                 route_ids: List[Tuple[int, int]], # list of tuples of ids for the start and destination cities
                 cost: int) -> None: # the total cost of the route from start to destination
        self.route = route
        self.route_ids = route_ids
        self.cost = cost

class Edge:
    def __init__(self, start, finish, weight) -> None:
        self.start = start
        self.finish = finish
        self.weight = weight
        self.end = self.finish

    def __repr__(self):
        return f"Edge({self.start} -> {self.finish}, weight={self.weight})"


class BusStop:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

# TODO: Implement the methods on the PathFinder class using an underlying graph representation
# of your choice. Feel free to use your graph classes from the practice exercises; copy the appropriate
# files into your project and import the classes at the top of this file.
class PathFinder:
    def __init__(self, directed=False) -> None:
        
        self.graph = AdjacencyListGraph(directed)
        self.ids = {}

    # TODO: adds an edge to the graph, using a the id of the start node and id of the finish node
    def add_edge(self, start_id: int, finish_id:int , cost: float) -> None:
        self.graph.add_edge(start_id, finish_id, cost)

    # TODO: adds a node to the graph, passing in the id, friendly name, and location of the node.
    # location is a tuple with the x and y coordinates of the location
    def add_node(self, id: int, name: str, location: Tuple[float, float]) -> None:
        stop = BusStop(id, name, location)
        self.ids[id] = stop

        self.graph.add_node(id)

    def heuristic(self, id1, id2):
        stop1 = self.ids[id1]
        stop2 = self.ids[id2]
        
        #return abs(stop1.location[0] - stop2.location[0]) + abs(stop1.location[1] - stop2.location[1])
        #return 0
        return ((stop1.location[0] - stop2.location[0])**2 + (stop1.location[1] - stop2.location[1])**2)**(1/2)
        # manhattan distance
        #return abs(stop1.location[0] - stop2.location[0]) + abs(stop1.location[1] - stop2.location[1])

    # TODO: calculates the minimum path using the id of the start city and id of the destination city, using A*
    # Returns a RouteInfo object that contains the edges for the route.  See RouteInfo above for attributes
    # Note: This implementation should use A*.  Tests that should pass 
    def get_minimum_path(self, start_city_id: int, destination_id:int ) -> RouteInfo:
        pqueue: PriorityQueue = PriorityQueue()
        lengths = {}
        for node in self.graph.get_nodes():
            lengths[node] = None
            pqueue.enqueue(float("inf"), node)
        
        lengths[start_city_id] = (0, None)
        pqueue.change_priority(start_city_id, self.heuristic(start_city_id, destination_id))
        
        
        visited = set() # it took me 5 hours of debugging to realize you can't check to see if you've visited a node before
        # because you have to always see if there's a lower value from the path that you're currently on
        
        while pqueue.size() > 0:
            
            startpoint = pqueue.dequeue()
            if startpoint == destination_id: break
            before = lengths[startpoint][0]
            
            
            for edge in sorted(self.graph.get_edges(startpoint), key=lambda x: x.weight):
                target = edge.finish
                added_distance = before + edge.weight
                if lengths[target] is None or added_distance < lengths[target][0]:
                    lengths[target] = (added_distance, startpoint)
                    pqueue.enqueue(added_distance + self.heuristic(target, destination_id), target)
    
                
        ids = []

        current = destination_id
        while current is not None:
            ids.insert(0, current)
            current = lengths[current][1]

        id_groups = [(ids[i], ids[i+1]) for i in range(len(ids)-1)]
        names = [(self.ids[id1].name, self.ids[id2].name) for id1, id2 in id_groups]

        return RouteInfo(names, id_groups, lengths[destination_id][0])
