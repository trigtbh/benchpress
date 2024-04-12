from unittest import TestCase
from chicago_metro import ChicagoMetro
from king_county_bus import KingCountyBus
from road_trip import RoadTrip

class TransportationTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def _assert_path(self, route_info, start_city, end_city):
        start_set = set()
        end_set = set()
        for start, finish in route_info.route_ids:
            self.assertNotIn(start, start_set)
            self.assertNotIn(finish, end_set)
            start_set.add(start)
            end_set.add(finish)

        dif = start_set.difference(end_set)
        self.assertEqual(1, len(dif))
        self.assertIn(start_city, dif)

        dif = end_set.difference(start_set)
        self.assertEqual(1, len(dif))
        self.assertIn(end_city,  dif)
        
    def test_one_route_kc_bus(self):
        ticket = KingCountyBus()
        route_info = ticket.get_minimum_path_for_ticket(57211, 57212)
        self.assertEqual(371, route_info.cost)
        self._assert_path(route_info, 57211, 57212)


    def test_long_route_kc_bus(self):
        ticket = KingCountyBus()
        route_info = ticket.get_minimum_path_for_ticket(67330,  99431)
        self.assertEqual(36407, route_info.cost)
        self._assert_path(route_info, 67330, 99431)

    def test_long_route_chicago(self):
        ticket = ChicagoMetro()
        route_info = ticket.get_minimum_path_for_ticket(8759,  3804)
        self.assertEqual(27557, route_info.cost)
        self._assert_path(route_info, 8759, 3804)

    def test_long_route_road_trip(self):
        ticket = RoadTrip()
        # East lake high school to Mt Rainer
        route_info = ticket.get_minimum_path_for_ticket(110817474,  512051128)
        self.assertAlmostEqual(176767.8818243295, route_info.cost)
        self._assert_path(route_info, 110817474, 512051128)
        
testobj = TransportationTests()
