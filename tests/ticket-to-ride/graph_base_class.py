from abc import ABC, abstractmethod
from typing import Set


class Edge:
    def __init__(self, start, finish, weight) -> None:
        self.start = start
        self.finish = finish
        self.weight = weight
        self.end = self.finish

    def __repr__(self):
        return f"Edge({self.start} -> {self.finish}, weight={self.weight})"

class GraphBaseClass(ABC):
    def __init__(self, is_directed: bool) -> None:
        self.is_directed = is_directed
        super().__init__()

    @abstractmethod
    def add_node(self, name:any) -> None:
        pass

    @abstractmethod
    def remove_node(self, name:any) -> None:
        pass

    @abstractmethod
    # return True if the node name1 is connected to the node name2 and False otherwise
    def is_connected(self, name1:any, name2:any) -> bool:
        pass

    @abstractmethod
    def add_edge(self, start:any, finish:any, weight:int) -> None:
        pass

    @abstractmethod
    # Returns a set of node names adjacent to the given node (i.e. there's an arc from the node to the neighbor)
    def get_neighbors(self, name:any) -> Set[any]:
        pass
    
    @abstractmethod
    # Gets a set of arcs leading out of the given node
    def get_edges(self, name:any) -> Set[Edge]:
        pass
    
    @abstractmethod
    # Gets a set of arcs leading out of the given node
    def get_nodes(self, name:str) -> Set[str]:
        pass