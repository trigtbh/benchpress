import json
import math
from typing import Dict, List, Set, Tuple

from path_finding import PathFinder, RouteInfo


class RoadTrip:
    def __init__(self) -> None:
        self.finder = PathFinder()
        self._load_map_data()

    def _load_map_data(self):
       
        with open("car_nodes.txt", "r", encoding="utf-8") as stop_file:
            stop_data = json.loads(stop_file.read())
            nodehash = {}
            for stop in stop_data:
                nodehash[stop["id"]] = (stop["x"], stop["y"])
                self.finder.add_node(int(stop["id"]), stop["id"], (stop["x"], stop["y"]))
         
        with open("car_edges.txt", "r", encoding="utf-8") as edge_file:
            edges = json.loads(edge_file.read())
            for edge in edges:
                self.finder.add_edge(int(edge["source"]), int(edge["target"]), float(edge["length"]))
                self.finder.add_edge(int(edge["target"]), int(edge["source"]), float(edge["length"]))

    def get_minimum_path_for_ticket(self, start:int , finish:int) -> RouteInfo:
        return self.finder.get_minimum_path(start, finish)
