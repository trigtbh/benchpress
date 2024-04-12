import json
import math
from typing import Dict, List, Set, Tuple

from path_finding import PathFinder, RouteInfo


class ChicagoMetro:
    def __init__(self) -> None:
        self.finder = PathFinder(directed=True)
        self._load_map_data()
           
    def _load_map_data(self):
        with open("chicago_stops.txt", "r", encoding="utf-8") as stop_file:
            stop_data = json.loads(stop_file.read())
            for stop in stop_data:
                self.finder.add_node(int(stop["stop_id"]), stop["stop_name"], (stop["x"], stop["y"]))
        
        with open("chicago_edges.txt", "r", encoding="utf-8") as edge_file:
            edges = json.loads(edge_file.read())
            for edge in edges:
                self.finder.add_edge(int(edge["Start"]), int(edge["Finish"]), int(edge["Distance"]))

    def get_minimum_path_for_ticket(self, start:int , finish:int) -> RouteInfo:
        return self.finder.get_minimum_path(start, finish)
