from nbody import *

import copy
import numpy
from numpy import testing

# Initial data for later use
BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}
SYSTEM = list(BODIES.values())

# Helper codes

def differences(bodies1, bodies2):
    """
    Compare two configurations.
    """
    assert len(bodies1) == len(bodies2), "Configurations must have same number of bodies! {}, {}".format(len(bodies1), len(bodies2))
    N = len(bodies1)
    d_positions = numpy.zeros((N, 3))
    d_velocities = numpy.zeros((N, 3))
    norm_difference = 0.0
    for n in range(N):
        d_positions[n, :] = numpy.array(bodies1[n][0]) - numpy.array(bodies2[n][0])
        d_velocities[n, :] = numpy.array(bodies1[n][1]) - numpy.array(bodies2[n][1])
        norm_difference += numpy.sum(numpy.abs(d_positions[n, :])) + numpy.sum(numpy.abs(d_velocities[n, :]))
    return norm_difference, d_positions, d_velocities

def flip_time(bodies):
    """
    Flip the time by flipping the velocity.
    """

    for i in range(len(bodies)):
        for j in range(3):
            bodies[i][1][j] *= -1.0

def flip_coordinate(bodies, coord):
    """
    Flip a single coordinate direction
    """

    for i in range(len(bodies)):
        bodies[i][0][coord] *= -1.0
        bodies[i][1][coord] *= -1.0

def translate_coordinate(bodies, shift):
    """
    Translate the coordinates of all bodies
    """

    for i in range(len(bodies)):
        for n in range(3):
            bodies[i][0][n] += shift[n]

def rotate_bodies(bodies, angles, invert=False):
    """
    Rotate the coordinates of all bodies.
    """

    Rx = numpy.array([[1.0, 0.0, 0.0],
                      [0.0, numpy.cos(angles[0]), -numpy.sin(angles[0])],
                      [0.0, numpy.sin(angles[0]), numpy.cos(angles[0])]])
    Ry = numpy.array([[numpy.cos(angles[1]), 0.0, numpy.sin(angles[1])],
                      [0.0, 1.0, 0.0],
                      [-numpy.sin(angles[1]), 0.0, numpy.cos(angles[1])]])
    Rz = numpy.array([[numpy.cos(angles[2]), -numpy.sin(angles[2]), 0.0],
                      [numpy.sin(angles[2]), numpy.cos(angles[2]), 0.0],
                      [0.0, 0.0, 1.0]])
    if invert:
        R = numpy.dot(numpy.dot(Rx, Ry), Rz)
    else:
        R = numpy.dot(Rz, numpy.dot(Ry, Rx))
    for i in range(len(bodies)):
        x = numpy.array(bodies[i][0])
        v = numpy.array(bodies[i][1])
        xp = numpy.dot(R, x)
        vp = numpy.dot(R, v)
        for n in range(3):
            bodies[i][0][n] = xp[n]
            bodies[i][1][n] = vp[n]

def scale_bodies(bodies, scale):
    """
    Scale coordinates and masses.
    """

    bodies_scale = []
    for (x, v, m) in bodies:
        new_x = copy.deepcopy(x)
        new_v = copy.deepcopy(v)
        new_m = m * scale
        for i in range(3):
            new_x[i] *= scale
        bodies_scale.append((new_x, new_v, new_m))

    return bodies_scale

# Actual tests

def test_flip_time():
    bodies_flip_time_1 = copy.deepcopy(SYSTEM)
    bodies_flip_time_2 = copy.deepcopy(SYSTEM)
    advance(dt=0.01, n=1, bodies=bodies_flip_time_1, pairs = combinations(bodies_flip_time_1))
    flip_time(bodies_flip_time_2)
    advance(dt=-0.01, n=1, bodies=bodies_flip_time_2, pairs = combinations(bodies_flip_time_2))
    flip_time(bodies_flip_time_2)
    norm_flip_time, dx, dv = differences(bodies_flip_time_1, bodies_flip_time_2)
    testing.assert_allclose(norm_flip_time, 0.0)
    testing.assert_allclose(dx, numpy.zeros_like(dx))
    testing.assert_allclose(dv, numpy.zeros_like(dv))

def test_flip_coordinates():
    bodies_flip_coord_base = copy.deepcopy(SYSTEM)
    advance(dt=0.01, n=1, bodies=bodies_flip_coord_base, pairs = combinations(bodies_flip_coord_base))
    for coord in range(3):
        bodies_flip_coord = copy.deepcopy(SYSTEM)
        flip_coordinate(bodies_flip_coord, coord)
        advance(dt=0.01, n=1, bodies=bodies_flip_coord, pairs = combinations(bodies_flip_coord))
        flip_coordinate(bodies_flip_coord, coord)
        norm_flip_coord, dx, dv = differences(bodies_flip_coord_base, bodies_flip_coord)
        testing.assert_allclose(norm_flip_coord, 0.0)
        testing.assert_allclose(dx, numpy.zeros_like(dx))
        testing.assert_allclose(dv, numpy.zeros_like(dv))

def test_rotate_coordinates():
    bodies_rotate_coord_base = copy.deepcopy(SYSTEM)
    advance(dt=0.01, n=1, bodies=bodies_rotate_coord_base, pairs = combinations(bodies_rotate_coord_base))
    angles = numpy.pi/4.0*numpy.random.rand(3) # Random Euler angles in [0, pi/4]
    bodies_rotate_coord = copy.deepcopy(SYSTEM)
    rotate_bodies(bodies_rotate_coord, angles)
    advance(dt=0.01, n=1, bodies=bodies_rotate_coord, pairs=combinations(bodies_rotate_coord))
    rotate_bodies(bodies_rotate_coord, -angles, invert=True)
    norm_rotate_coord, dx, dv = differences(bodies_rotate_coord_base, bodies_rotate_coord)
    max_error = 3*9*5*numpy.sum(numpy.abs(numpy.spacing(angles)))
    testing.assert_allclose(norm_rotate_coord, 0.0, atol = max_error)
    testing.assert_allclose(dx, numpy.zeros_like(dx), atol = max_error)
    testing.assert_allclose(dv, numpy.zeros_like(dv), atol = max_error)
