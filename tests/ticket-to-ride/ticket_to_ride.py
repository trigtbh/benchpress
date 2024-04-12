import json
from typing import List, Set, Tuple, Dict

from path_finding import PathFinder, RouteInfo


class TicketToRide:
    def __init__(self) -> None:
        self.path_finder = PathFinder()
        self._load_map_data()

    def get_minimum_path_for_ticket(self, start: int, finish: int) -> RouteInfo:
        return self.path_finder.get_minimum_path(start, finish)

    
    def _load_map_data(self):
        with open("game_city_locations.json", "r", encoding="utf-8") as file_data:
            path_data = json.loads(file_data.read())
            name_to_id = {}
            for node in path_data["cities"]:
                name_to_id[node["name"]] = node["id"]
                self.path_finder.add_node(node["id"], node["name"], node["location"])

            # TODO: Update load_map_data to load the tracks into your graph
            # Use the example for cities above, and open game_city_locations.json to see the fields for "tracks"
            for track in path_data["tracks"]:
                id1 = name_to_id[track["city_1"]]
                id2 = name_to_id[track["city_2"]]
                self.path_finder.add_edge(id1, id2, track["distance"])
                