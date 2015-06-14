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

POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)

BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 2)
~~~

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
POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
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
[-4.99  0.    0.  ]
[ 5.01  0.    0.  ]
~~~

That doesn't look good---it looks like body 1 has moved by 1 unit to the right,
and body 2 has moved by 1 unit... also to the right.
What about the velocities?
We expect these to behave the same; i.e.,
gravity should cause the bodies to acquire
equal *and opposite*  velocities.

~~~
POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
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
advance(BODIES, 1, 2)
~~~

~~~{.python}
print 'Velocities after advancing:'
print BODIES[1][0]
print BODIES[1][1]
~~~

~~~{.output}
[0.02, 0.0, 0.0]
[0.02  , 0.0, 0.0]
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
POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
VELOCITIES = ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0])
MASSES = (1.0, 1.0)
BODIES = [POSITIONS, VELOCITIES, MASSES]

advance(BODIES, 1, 2)
print BODIES[1][0]
print BODIES[1][1]

# now do the same, but
# shift positions by 1, 2 and 3 units in
# each co-ordinate direction respectively.

POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
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

Our tests have checked that the code satisfies various, simple conditions.
Tests like these are useful because when they fail,
it's relatively easy to figure out where the problem is.
In our case, there is a problem with the signs of the positions
and velocities.

~~~
dvdt[i][k] += mag * m[j] * dr[k]
dvdt[j][k] += mag * m[i] * dr[k]
~~~

`dvdt[i][k]` is the acceleration in the `k` direction,
experienced by the `i` body due to the `j` body,
and `dvdt[j][k]` is the acceleration in the `k` direction,
experienced by the `j` body due to the `i` body.
We know that the two must have *opposite* signs,
but looking at the right hand sides,
we can see that they will have the same sign.
So we go ahead and change this:

~~~
dvdt[i][k] += mag * m[j] * dr[k]
dvdt[j][k] -= mag * m[i] * dr[k]
~~~

Now, we perform the same test as above:

~~~
POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
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
[-5, 0.0, 0.0]
[5, 0.0, 0.0]
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
advance(BODIES, 1, 2)
~~~

~~~{.python}
print 'Positions after advancing:'
print BODIES[0][0]
print BODIES[0][1]
~~~

~~~{.output}
[-5.01  0.   0. ]
[5.01  0.   0. ]
~~~

~~~{.python}
print 'Velocities after advancing:'
print BODIES[1][0]
print BODIES[1][1]
~~~

~~~{.output}
[-0.02.  0.  0.]
[0.02.  0.  0.]
~~~

Now our positions and velocities are both equal and opposite,
but you'll notice that the bodies are moving in the wrong directions.
Gravity should pull them *together*,
but our code is pushing them *apart*.
As you can guess, the fix is to switch the following signs:

~~~
dvdt[i][k] += mag * m[j] * dr[k]
dvdt[j][k] -= mag * m[i] * dr[k]
~~~

~~~
dvdt[i][k] -= mag * m[j] * dr[k]
dvdt[j][k] += mag * m[i] * dr[k]
~~~

Let's run our tests one more time:


~~~
POSITIONS = ([-5, 0.0, 0.0], [5, 0.0, 0.0])
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
[-5, 0.0, 0.0]
[5, 0.0, 0.0]
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
advance(BODIES, 1, 2)
~~~

~~~{.python}
print 'Positions after advancing:'
print BODIES[0][0]
print BODIES[0][1]
~~~

~~~{.output}
[-4.99  0.    0.  ]
[ 4.99  0.    0.  ]
~~~

~~~{.python}
print 'Velocities after advancing:'
print BODIES[1][0]
print BODIES[1][1]
~~~

~~~{.output}
[ 0.02  0.    0.  ]
[-0.02  0.    0.  ]
~~~

Now our code is performing like we expect it to.
Let's make the changes in `nbody.py`,
and run `plot_trajectories.py`:

![Output from visualization script](fig/planets_fixed.gif)
