"""Example of tracking arrivals/departures from locations using geofences."""

import random
import time
from itertools import repeat, starmap

import colorama
from blinker import signal
from termcolor import colored

from geofences.geofence import Geofence
from geofences.point import Point
from geofences.user import User

colorama.init()

arrival = signal('arrival')
departure = signal('departure')


@arrival.connect
def user_arrived_at(user, location):
    message = '==> {0!s} arrived at {1!s}.'.format(user, location)
    print colored(message, 'green')


@departure.connect
def user_departed_from(user, location):
    message = '==> {0!s} departed from {1!s}.'.format(user, location)
    print colored(message, 'blue')

home = Geofence('Home', radius=5)
work = Geofence('Work', radius=7.6, center=(-20.7, 13.4))
school = Geofence('School', radius=10, center=(30, 9.8))
park = Geofence('Park', radius=3, center=(23, 9.8))


def get_random_point(domain=(-50, 50), range_=(-50, 50)):
    return Point(random.randint(*domain), random.randint(*range_))


def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.

    Example:  repeatfunc(random.random)
    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))

if __name__ == '__main__':
    sera = User('Sera', locations=[home, work])
    daisy = User('Daisy', locations=[home, school, park])

    # simulate random travels...
    for point in repeatfunc(get_random_point):
        user = random.choice((sera, daisy))
        user.move_to(point)
        time.sleep(1)

        # ...with occassional stops at favorite locations
        if random.randint(1, 10) < 3:
            user = random.choice((sera, daisy))
            user.move_to(random.choice(list(user.locations)).boundary.center)
            time.sleep(1)
