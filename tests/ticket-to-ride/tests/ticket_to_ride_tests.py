from unittest import TestCase

from ticket_to_ride import TicketToRide


class TicketToRideTests(TestCase):
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
        

    def test_one_route(self):
        ticket = TicketToRide()
        route_info = ticket.get_minimum_path_for_ticket(11,21)
        self.assertEqual(1, route_info.cost)
        self._assert_path(route_info, 11, 21)

    def test_long_route(self):
        ticket = TicketToRide()
        route_info = ticket.get_minimum_path_for_ticket(33, 15)
        self.assertEqual(23, route_info.cost)
        self._assert_path(route_info, 33, 15)

    def test_half_route(self):
        ticket = TicketToRide()
        route_info = ticket.get_minimum_path_for_ticket(6, 16)
        self.assertEqual(14, route_info.cost)
        self._assert_path(route_info, 6, 16)

    def test_interesting_route(self):
        ticket = TicketToRide()
        route_info = ticket.get_minimum_path_for_ticket(8, 13)
        self.assertEqual(6, route_info.cost)
        self._assert_path(route_info, 8, 13)