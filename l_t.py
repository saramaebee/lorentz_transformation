import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

c = 299792458

# on a plot, an arrow represents velocity, with the end
# falling on the point where an event occurs
# the arrow is the representation of the time
# and space that must be travelled in order for
# an object at the start of the arrow to reach
# the event

# accepts x : location on x axis, representing space
# accepts t : location on y axis, representing time


def lorentz_transformation(x, t, v):
    # gamma, lorentz factor
    g_1 = 1 - (v**2/c**2)
    g = 1 / sqrt(g_1)
    print('g: %10.2f' % g)

    # time transformation
    t_1 = (v * x) / (c ** 2)
    t_2 = t - t_1
    tp = g * t_2

    # space transformation
    x_1 = x - (v * t)
    xp = g * x_1

    return xp, tp


def main():
    x = 3
    t = 5
    v = 2
    xp, tp = lorentz_transformation(x, t, v)
    print(x, t, v)
    print(xp, tp)

    fig, (ax1, ax2) = plt.subplots(2)

    ax1.plot([0, x], [0, t], 'o--')
    ax1.plot([0, 0], [0, 10], 'o--')
    ax1.axis([-10, 10, 0, 10])

    ax2.plot([0, 0], [0, 10], 'o--')
    ax2.plot([0, xp], [0, tp], 'o--')
    ax2.axis([-10, 10, 0, 10])

    plt.show()


if __name__ == '__main__':
    main()

