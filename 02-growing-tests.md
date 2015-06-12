---
layout: page
title: Testing Scientific Software
subtitle: Growing Tests
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> * Learn different strategies to test code
> * Identify bugs in our code by writing tests for it

Let's consider a much simpler system:
two bodies of unit mass,
separated by unit distance,
and initially at rest (zero velocity):

~~~{.python}
from nbody import *

POSITIONS = ([-0.5, 0.0, 0.0], [0.5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 1)
}

One of the first things we need to make sure of is
that the masses of the bodies haven't changed:

~~~{.python}
print BODIES[2][0]
print BODIES[2][1]
~~~

~~~{.output}
1.0
1.0
~~~

Gravity is an *attractive* force, i.e,
it pulls bodies closer together.
So  the second thing that we can check is that
the two bodies have moved *toward* each other,
by equal amounts.
Since the bodies are of equal mass,
and are both initially at rest,
we don't expect that one body should
move more than the other.
Let's look at the positions of the
bodies before and after advancing the system:

~~~
POSITIONS = ([-0.5, 0.0, 0.0], [0.5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)
BODIES = [POSITIONS, VELOCITIES, MASSES]
~~~

~~~{.python}
print 'Positions before advancing:'
print BODIES[0][0]
print BODIES[0][1]
~~~

~~~{.output}
Positions before advancing:
[-0.5, 0.0, 0.0]
[0.5, 0.0, 0.0]
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
[0.5, 0.0, 0.0]
[1.5, 0.0, 0.0]
~~~

That doesn't look good---it looks like body 1 has moved by 1 unit to the right,
and body 2 has moved by 1 unit... also to the right.

What about the velocities?
We expect these to behave the same; i.e.,
gravity should cause the bodies to acquire
equal *and opposite*  velocities.

~~~
POSITIONS = ([-0.5, 0.0, 0.0], [0.5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)
BODIES = [POSITIONS, VELOCITIES, MASSES]

~~~

~~~{.python}
print 'Velocities before advancing:'
print BODIES[1][0]
print BODIES[1][1]
~~~

~~~{.output}
Velocities before advancing:
[0.0, 0.0, 0.0]
[0.0, 0.0, 0.0]
~~~

~~~{.python}
advance(BODIES, 1, 1)
~~~

~~~{.python}
print 'Velocities before advancing:'
print BODIES[1][0]
print BODIES[1][1]
~~~

~~~{.output}
[2.0, 0.0, 0.0]
[2.0, 0.0, 0.0]
~~~

Again, the velocities *are* equal,
but they have the same sign (both positive),
which suggests that the bodies move
in the same direction (the right).

Let's write some more tests to find out more about our code.

Note that only the separation between bodies is meant to matter.
So if we arbitrarily translate all coordinates by some amount,
and advance the system by the same amount,
the velocities acquired should be the same.

~~~{.python}
POSITIONS = ([-0.5, 0.0, 0.0], [0.5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)
BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 2)
print BODIES[1][0]
print BODIES[1][1]

# now do the same, but
# shift positions by 1, 2 and 3 units in
# each co-ordinate direction respectively.

POSITIONS = ([-0.5, 0.0, 0.0], [0.5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)
BODIES = [POSITIONS, VELOCITIES, MASSES]

N = len(BODIES[2])
shift = np.array([1, 2, 3])
for i in range(N):
    for n in range(3):
        BODIES[0][i][n] += shift[n]

advance(BODIES, 1, 2)

print 'Velocities after shifting: '
print BODIES[1][0]
print BODIES[1][1]
~~~

~~~{.output}
[2.0, 0.0, 0.0]
[2.0, 0.0, 0.0]

[2.0, 0.0, 0.0]
[2.0, 0.0, 0.0]
~~~

Although our velocities are wrong,
shifting, or *translating* our system
doesn't change its behavior, which is a good sign.
