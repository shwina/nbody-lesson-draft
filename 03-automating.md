---
layout: page
title: Testing Scientific Software
subtitle: Automating Tests
minutes: 5
---

So far, we've been testing our code using
`print` statements:

~~~{.python}
print 'Positions before advancing: '
print BODIES['body-1'][0]
print BODIES['body-2'][0]
~~~

~~~{.output}
[-0.5, 0.0, 0.0]
[0.5, 0.0, 0.0]
~~~

~~~{.python}
advance(1, 1, SYSTEM, PAIRS)
~~~

~~~{.python}
print 'Positions after advancing: '
print BODIES['body-1'][0]
print BODIES['body-2'][0]
~~~

~~~{.output}
[-1.5, 0.0, 0.0]
[-0.5, 0.0, 0.0]
~~~

We're also re-setting our system for every new test:

BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}

SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)

This is a great first step---
we're doing *some* testing,
which is more than a lot of programmers.
But we can do better than using `print` statements.
`print` needs us to visually inspect and compare
output every time,
and sooner or later,
we're going to make mistakes and miss some subtle differences.

Also, writing all these print statements is a lot of work.
The more tests we write,
the more typing we'll have to do each time we want to write our tests.
And the more time testing takes us,
the less likely we are to do it often.

We need a better way to organize and run our tests,
and the first (and most important) tool that we'll use for this
is the `assert` statement.
`assert` simply checks if something is true
at a certain point in a program.
When Python sees one, it evaluates the assertion's condition.
If it's true, Python does nothing,
but if it's false,
Python halts the program immediately
and prints the error message provided.

~~~{.python}
mass_of_a = 1.0
mass_of_b = 1.0
assert mass_of_a == mass_of_b, 'Masses are not equal'
~~~

~~~{.python}
mass_of_a = 1.0
mass_of_b = 2.0
assert mass_of_a == mass_of_b, 'Masses are not equal'
~~~

~~~{.error}
AssertionError                            Traceback (most recent call last)
<ipython-input-3-6787e3e4f3ef> in <module>()
----> 1 assert mass_of_a == mass_of_b, 'Masses are not equal'

AssertionError: Masses are not equal
~~~

Using assertions, we can re-write our tests in a script,
using assertions to check for equality,
rather than printing the results,
and inspecting them visually:

~~~
# test_nbody.py

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
~~~


Now, every time we want to run our tests, we simply do:

~~~{.bash}
python test_nbody.py
~~~

from the command line.
