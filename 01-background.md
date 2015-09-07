---
layout: page
title: Testing Scientific Software
subtitle: The N-Body Problem
minutes: 5
---
> ## Learning Objectives {.objectives}
>
> *   Introduce the key features of N-Body codes

The N-Body problem is a model of lots of interacting "things". It's used to model gravitational interactions in astrophysics, or atom interactions in molecular dynamics. It's a very effective and efficient modelling approach, separating out the essential features of the *bodies* (mass, charge, etc), and the interaction *force* between the bodies.

Here we will focus on the gravitational N-Body problem: each body represents a heavy object (such as a planet). The only features that matter are the body's mass, position and velocity. The only force between bodies is gravity. For any two bodies, the gravitational force pulls the bodies closer together, and the strength of the force depends on the product of the masses of the bodies divided by the distance between them. The total force on one body is the sum of all forces between that body and *all* the other bodies.

Any N-Body algorithm works by defining the *state* of the system, which is then advanced in time. The state is the collection of the positions, velocities and features (here only the masses) of all the bodies. To advance the positions to the next timestep, the code uses the velocities (which are known). To advance the velocities, the code works out the accelerations on the bodies by computing the gravitational force on each body. The masses remain fixed.

One central limitation of N-Body methods is how the cost increases with the number of bodies. To advance from one timestep to the next, the code has to compute the total force on all N bodies. To compute the force on one body, the code has to compute its interaction with all the other (N-1) bodies. The computational cost goes (at least) as N squared: if you double the number of bodies, the computational cost goes up by at least a factor of 4. For the gravitational problem, where each body is a "planet", this isn't a worry: for molecular dynamics, where bulk properties of *lots* of bodies is the point, it can be a real limitation.
