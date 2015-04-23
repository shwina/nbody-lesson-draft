---
layout: page
title: Testing Scientific Software
subtitle: Growing Tests
minutes: 5
---

Before we can test that our code produces the right answer,
we need to know *what* the right answer is.

Let's consider a much simpler system:
two bodies of unit mass,
separated by unit distance,
and initially at rest (zero velocity):

~~~{.python}
from nbody import *

BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}

SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)
~~~

~~~{.python}
advance(1, 1, SYSTEM, PAIRS)
~~~

One of the first things we need to make sure of is
that the masses of the bodies haven't changed:

~~~{.python}
print BODIES['body-1'][2]
print BODIES['body-2'][2]
~~~

~~~{.output}
1
1
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
BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}

SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)
~~~

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

That doesn't look good---
it looks like `body-1` has moved by 1 unit to the left,
and `body-2` has moved by 1 unit... also to the left.

What about the velocities?
We expect these to behave the same; i.e.,
gravity should cause the bodies to acquire
equal *and opposite*  velocities.

~~~
BODIES = {
    'body-1': ([-0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1),
    'body-2': ([0.5, 0.0, 0.0], [0.0, 0.0, 0.0], 1)
}

SYSTEM = list(BODIES.values())
PAIRS = combinations(SYSTEM)
~~~

~~~{.python}
print 'Velocities before advancing: '
print BODIES['body-1'][1]
print BODIES['body-2'][1]
~~~

~~~{.output}
[0.0, 0.0, 0.0]
[0.0, 0.0, 0.0]
~~~

~~~{.python}
advance(1, 1, SYSTEM, PAIRS)
~~~

~~~{.python}
print 'Velocities after advancing: '
print BODIES['body-1'][1]
print BODIES['body-2'][1]
~~~

~~~{.output}
[-1.0, 0.0, 0.0]
[-1.0, 0.0, 0.0]
~~~

Again, the velocities *are* equal,
but they have the same sign (both negative),
which suggests that the bodies move
in the same direction.

Let's write some more tests to find out more about our code.
