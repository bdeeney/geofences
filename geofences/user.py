"""geofences.user"""
from copy import deepcopy

from blinker import signal

from geofences.point import Point


class User(object):
    """A user moving in 2-D Euclidean space."""
    def __init__(self, name, position=(0, 0), locations=None):
        self.name = name

        if isinstance(position, tuple):
            self.position = Point(*position)
        else:
            self.position = deepcopy(position)

        if locations is None:
            locations = []
        self._is_at = {location: self in location for location in locations}

    @property
    def locations(self):
        """Return a dictionary view of the user's configured locations."""
        return self._is_at.viewkeys()

    def get_status(self):
        """
        Whether the user is at each of their locations.

        Returns a dict of (location, status) pairs where the boolean status
        value indicates whether the user is at the corresponding location.

        """
        return self._is_at.copy()

    def move(self, delta_x, delta_y):
        """Move the user in 2-D space.

        The user's position is updated by a distance of `delta_x` horizontally
        and `delta_y` vertically.

        """
        self.position.move(delta_x, delta_y)
        self._update_status()

    def move_to(self, point, steps=100):
        """Move the user in a straight line to the given `point`.

        Use the given number of incremental `steps` along the line to the
        destination.

        """
        delta_x = (point.x - self.position.x) / steps
        delta_y = (point.y - self.position.y) / steps
        for i in xrange(steps):
            self.move(delta_x, delta_y)

    def _update_status(self):
        """Update the user's status relative to configured locations."""
        for location, was_at in self._is_at.iteritems():
            self._is_at[location] = self in location
            if self._is_at[location] != was_at:
                self._signal_arrival_departure(location)

    def _signal_arrival_departure(self, location):
        """Signal that the user arrived at or departed from `location`."""
        event = 'arrival' if self._is_at[location] else 'departure'
        signal(event).send(self, location=location)

    def __str__(self):
        return self.name
