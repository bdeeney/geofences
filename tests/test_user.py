import unittest

from blinker import signal
from mock import MagicMock

from geofences.geofence import Geofence
from geofences.point import Point
from geofences.user import User


class DescribeUser(unittest.TestCase):

    def setUp(self):
        self.user = User('Daisy')

    def should_have_name(self):
        self.assertEqual(self.user.name, 'Daisy')

    def should_have_position(self):
        self.assertEqual(self.user.position, Point(0, 0))

    def should_have_list_of_locations(self):
        self.assertItemsEqual(self.user.locations, [])


class WhenCreatingUser(unittest.TestCase):

    def setUp(self):
        self.locations = [
            Geofence('Home', radius=5),
            Geofence('Work', center=(10, 10), radius=6)
        ]
        self.user = User('Bob', position=Point(3, 4), locations=self.locations)

    def should_set_position(self):
        self.assertEqual(self.user.position, Point(3, 4))

    def should_set_locations(self):
        self.assertItemsEqual(self.user.locations, self.locations)

    def should_set_is_at(self):
        self.assertIsInstance(self.user._is_at, dict)


class WhenMovingUser(unittest.TestCase):

    def should_update_position(self):
        user = User('Daisy', position=(1, 2))
        user.move(0.5, 0.6)
        self.assertEqual(user.position, Point(1.5, 2.6))


class WhenArrivingAtLocation(unittest.TestCase):

    def setUp(self):
        self.home = Geofence('Home', radius=5)
        self.user = User('Daisy', position=(0, 6), locations=[self.home])
        self.callback = MagicMock()

        with signal('arrival').connected_to(self.callback):
            self.user.move(0, -1)

    def should_update_is_at(self):
        self.assertTrue(self.user._is_at[self.home])

    def should_emit_arrival_signal(self):
        self.callback.assert_called_with(self.user, location=self.home)


class WhenDepartingFromLocation(unittest.TestCase):

    def setUp(self):
        self.home = Geofence('Home', radius=5)
        self.user = User('Daisy', position=(0, 5), locations=[self.home])
        self.callback = MagicMock()

        with signal('departure').connected_to(self.callback):
            self.user.move(0.1, 0.1)

    def should_update_is_at(self):
        self.assertFalse(self.user._is_at[self.home])

    def should_emit_departure_signal(self):
        self.callback.assert_called_with(self.user, location=self.home)
