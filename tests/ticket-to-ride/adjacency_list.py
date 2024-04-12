from typing import Set, List, Dict
from graph_base_class import Edge, GraphBaseClass


# Implement Graph using an adjacency list as the underlying representation
class AdjacencyListGraph(GraphBaseClass):

    # if is_directed is true, this should be a directed graph.  If false, it's an undirected graph
    # Make sure your implementation accounts for node order on an edge for directed and is neutral for undirected
    # super sets a property self.is_directed to the parameter value
    def __init__(self, is_directed:bool) -> None:
        self.nodes: Dict[Set] = {}
        super().__init__(is_directed)
    
    # Adds a node named "name" to the graph.
    def add_node(self, name:any) -> None:
        self.nodes.setdefault(name, set())
        

    # Removes the node named "name" and all arcs connected to it
    def remove_node(self, name:any) -> None:
        del self.nodes[name]
        for node in self.nodes:
            self.nodes[node] = set(edge for edge in self.nodes[node] if edge.finish != name)
        
    
    # Gets a set of the names of all nodes in the graph
    def get_nodes(self) -> Set[any]:
        return set(self.nodes.keys())

    

    # Returns True if the node name1 is connected to the node name2 and False otherwise
    def is_connected(self, name1:any, name2:any) -> None:
        for edge in self.nodes[name1]:
            if edge.finish == name2:
                return edge
        return False

    # Adds an edge from node start to node finish with the weight specified
    def add_edge(self, start:any, finish:any, weight:int) -> None:
        self.nodes[start].add(Edge(start, finish, weight))
        if not self.is_directed:
            self.nodes[finish].add(Edge(finish, start, weight))


    # Returns a set of the names of nodes adjacent to the given node (i.e. there's an arc from the node to the neighbor)
    def get_neighbors(self, name:str) -> Set[any]:
        return set(edge.finish for edge in self.nodes[name])
    
    # Gets a set of edges leading out of the given node
    def get_edges(self, name:str) -> Set[Edge]:
        return self.nodes[name]
    
