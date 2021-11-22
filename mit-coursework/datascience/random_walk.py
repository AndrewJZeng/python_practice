import random
import copy
from statistics import mean
import pylab

class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltx, delty):
        self.x += deltx
        self.y += delty

    def calc_dist(self, otherLoc):
        return ((self.x - otherLoc.x) ** 2 + (self.y - otherLoc.y) ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Drunk(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def take_step(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        step = random.choice(stepChoices)
        self.location.move(step[0], step[1])

class MasochistDrunk(Drunk):
    def take_step(self):
        stepChoices = [(0, 1), (0, -0.7), (1, 0), (-1, 0)]
        step = random.choice(stepChoices)
        self.location.move(step[0], step[1])

def drunkTest(walkLengths, numTrials, dClass):
    dist = []
    loc = []
    for i in range(numTrials):
        origin = Location(0, 0)
        drunk = dClass(str(i), copy.deepcopy(origin))

        for _ in range(walkLengths):
            drunk.take_step()

        d = origin.calc_dist(drunk.location)
        dist.append(d)
        loc.append((drunk.location.x, drunk.location.y))
    return dist, loc

def plot_results(numTrial, numSteps):
    print('Usual Drunk')
    d_list, loc_list_u = drunkTest(numSteps, numTrial, Drunk)
    print('Mean: {}, Max: {}, Min: {}'.format(mean(d_list), max(d_list), min(d_list)))
    pylab.plot(d_list, 'r+', label='Usual')

    print('\nMasochistDrunk')
    d_list, loc_list_m = drunkTest(numSteps, numTrial, MasochistDrunk)
    print('Mean: {}, Max: {}, Min: {}'.format(mean(d_list), max(d_list), min(d_list)))
    pylab.plot(d_list, 'g^', label='Masochist')
    pylab.legend()
    pylab.title('Drunk Distance')
    pylab.xlabel('trial #')
    pylab.ylabel('distance')
    pylab.show()

    x = [x for (x, y) in loc_list_u]
    y = [y for (x, y) in loc_list_u]
    xm = [x for (x, y) in loc_list_m]
    ym = [y for (x, y) in loc_list_m]
    pylab.plot(x, y, 'r+', label='Usual')
    pylab.plot(xm, ym, 'g^', label='Masochist')
    pylab.legend()
    pylab.title('Drunk 2D Locations')
    pylab.xlabel('x axis')
    pylab.ylabel('y axis')
    pylab.show()


plot_results(numTrial = 1000, numSteps = 500)
