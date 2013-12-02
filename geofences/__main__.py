"""Example of tracking arrivals/departures from locations using geofences."""
import random
import sys
import time

import colorama
from blinker import signal
from termcolor import colored

from geofences import util
from geofences.geofence import Geofence
from geofences.user import User

# number of seconds to delay between moves and after events
DELAY = 1 if len(sys.argv) < 2 else float(sys.argv[1])

# define signals
arrival = signal('arrival')
departure = signal('departure')


@arrival.connect
def user_arrived_at(user, location):
    message = '==> {0!s} arrived at {1!s}.'.format(user, location)
    print colored(message, 'yellow')
    util.show_user_status(user)
    time.sleep(DELAY)


@departure.connect
def user_departed_from(user, location):
    message = '==> {0!s} departed from {1!s}.'.format(user, location)
    print colored(message, 'blue')
    util.show_user_status(user)
    time.sleep(DELAY)

# define locations of interest
home = Geofence('Home', radius=5)
work = Geofence('Work', radius=7.6, center=(-20.7, 13.4))
school = Geofence('School', radius=10, center=(30, 9.8))
park = Geofence('Park', radius=3, center=(23, 9.8))

# define users
sera = User('Sera', locations=[home, work])
daisy = User('Daisy', locations=[home, school, park])

colorama.init()

# simulate travel to random destinations...
for point in util.repeatfunc(util.get_random_point):
    user = random.choice((sera, daisy))
    util.move_user(user, point)
    time.sleep(DELAY)

    # ...with occassional stops at locations of interest
    if random.randint(1, 10) < 3:
        user = random.choice((sera, daisy))
        location = random.choice(list(user.locations))
        util.move_user(user, location.boundary.center)
        time.sleep(DELAY)
