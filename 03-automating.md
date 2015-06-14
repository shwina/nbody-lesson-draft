---
layout: page
title: Testing Scientific Software
subtitle: Automating Tests
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> * Learn about assertions, and how they can improve our tests

So far, we've been testing our code using
`print` statements:

~~~{.python}
print 'Positions before advancing:'
print BODIES[0][0]
print BODIES[0][1]
~~~

~~~{.output}
[-5, 0.0, 0.0]
[5, 0.0, 0.0]
~~~

~~~{.python}
advance(BODIES, 1, 2)
~~~

~~~{.python}
print 'Positions after advancing:'
print BODIES[0][0]
print BODIES[0][1]
~~~

~~~{.output}
Positions after advancing:
[-4.99, 0.0, 0.0]
[4.99, 0.0, 0.0]
~~~

And we are re-setting our system for every new test:

~~~{.python}
POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)
BODIES = [POSITIONS, VELOCITIES, MASSES]
~~~

This is a great first step---
we're doing *some* testing,
which is more than a lot of programmers do.
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
and inspecting them visually.
We set up the system as before:

~~~
POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 2)
~~~

And then write our test using an assertion:

~~~
assert BODIES[2][0] == BODIES[2][1]
~~~

Let's go ahead and rewrite more of our tests using
assertions.
We'll save them in a *script*, called `test_nbody_assertions.py`:

~~~
# test_nbody_assertions.py

POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 2)

# Check that the displacements (in the x-direction)
# are equal and opposite, and that all other displacements
# are zero:
assert(BODIES[0][0][1] == 0.0)
assert(BODIES[0][0][2] == 0.0)
assert(BODIES[0][1][1] == 0.0)
assert(BODIES[0][1][2] == 0.0)
assert(BODIES[0][0][0] == -BODIES[0][1][0])

POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 2)

# Check that the velocities (in the x-direction)
# are equal and opposite, and that all other velocities
# are zero:
assert(BODIES[1][0][1] == 0.0)
assert(BODIES[1][0][2] == 0.0)
assert(BODIES[1][1][1] == 0.0)
assert(BODIES[1][1][2] == 0.0)
assert(BODIES[1][0][0] == -BODIES[1][1][0])

POSITIONS = ([-5, 0.0, 0.0],  [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 2)
~~~

Now, every time we want to run our tests,
we can do so with just a few keystrokes:

~~~{.bash}
python test_nbody_assertions.py
~~~

from the command line.
