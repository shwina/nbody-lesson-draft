from nbody_fixed import *

# Initialize the system:

POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

# Advance the system by a single time step:
advance(BODIES, 1, 1)

# Check that the masses remain unchanged
assert BODIES[2][0] == BODIES[2][1]

# Initialize the system:
POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

# Advance the system by a single time step:
advance(BODIES, 1, 2)

# Check that the displacements (in the x-direction)
# are equal and opposite, and that all other displacements
# are zero:
assert(BODIES[0][0][1] == 0.0)
assert(BODIES[0][0][2] == 0.0)
assert(BODIES[0][1][1] == 0.0)
assert(BODIES[0][1][2] == 0.0)
assert(BODIES[0][0][0] == -BODIES[0][1][0])

# Initialize the system:
POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

# Advance the system by a single time step:
advance(BODIES, 1, 2)

# Check that the velocities (in the x-direction)
# are equal and opposite, and that all other velocities
# are zero:
assert(BODIES[1][0][1] == 0.0)
assert(BODIES[1][0][2] == 0.0)
assert(BODIES[1][1][1] == 0.0)
assert(BODIES[1][1][2] == 0.0)
assert(BODIES[1][0][0] == -BODIES[1][1][0])

# Initialize the system:
POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

# Advance the system by a single time step:
advance(BODIES, 1, 2)

# Check that body 1 has a positive velocity (in the x-direction)
# and that body 2 has a negative velocity (in the x-direction):

assert(BODIES[1][0][0] > 0)
assert(BODIES[1][1][0] < 0)
