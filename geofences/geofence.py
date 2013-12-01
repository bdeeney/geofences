"""geofences.geofence"""
from copy import deepcopy

from geofences.circle import Circle


class Geofence(object):
    """A circular geofence in 2-D Euclidean space."""
    def __init__(self, name, **kwargs):
        self.name = name
        if 'boundary' in kwargs:
            self.boundary = deepcopy(kwargs['boundary'])
        else:
            self.boundary = Circle(**kwargs)

    def __contains__(self, locatable):
        """Whether the boundary of the geofence encloses a `locatable` object.

        The `locatable` object must have a `position` attribute that returns a
        :class:`Point` indicating the position of the object.

        """
        return locatable.position in self.boundary

    def __str__(self):
        return self.name
