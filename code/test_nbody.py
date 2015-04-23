from nbody import *

# Initialize the system:
BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}

SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)

# Advance the system by a single time step:
advance(1, 1, SYSTEM, PAIRS)

# Check that the masses remain unchanged
assert BODIES['body-1'][1] == BODIES['body-2'][1], 'Masses are not equal'

# Initialize the system:
BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}

SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)

# Advance the system by a single time step:
advance(1, 1, SYSTEM, PAIRS)

# Check that the displacements (in the x-direction)
# are equal and opposite, and that all other displacements
# are zero:
assert(BODIES['body-1'][0][1] == 0.0)
assert(BODIES['body-1'][0][2] == 0.0)
assert(BODIES['body-2'][0][1] == 0.0)
assert(BODIES['body-2'][0][2] == 0.0)
assert(BODIES['body-1'][0][0] == -BODIES['body-2'][0][0])

# Initialize the system:
BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}

SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)

# Advance the system by a single time step:
advance(1, 1, SYSTEM, PAIRS)

# Check that the velocities (in the x-direction)
# are equal and opposite, and that all other velocities
# are zero:
assert(BODIES['body-1'][1][1] == 0.0)
assert(BODIES['body-1'][1][2] == 0.0)
assert(BODIES['body-2'][1][1] == 0.0)
assert(BODIES['body-2'][1][2] == 0.0)
assert(BODIES['body-1'][1][0] == -BODIES['body-2'][1][0])
