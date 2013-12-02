"""geofences.util"""
import random
from itertools import repeat, starmap

from termcolor import colored

from geofences.point import Point


def show_user_status(user):
    """Query and print the user's status.

    Demonstrates the ability to determine which geofences the user occupies at
    any given time.

    """
    for location, is_at in user.get_status().iteritems():
        color = 'green' if is_at else 'red'
        status = 'is at' if is_at else 'is not at'
        message = '\t{0!s} {1} {2!s}.'.format(user, status, location)
        print colored(message, color)


def get_random_point(domain=(-50, 50), range_=(-50, 50)):
    return Point(random.randint(*domain), random.randint(*range_))


def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.

    Example:  repeatfunc(random.random)
    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))


def move_user(user, point):
    """Move the given `user` to the given `point`."""
    print '{0!s} begins moving from {0.position} to {1}.' \
        .format(user, point)
    user.move_to(point)
    print '{0!s} now at {0.position}.'.format(user)
