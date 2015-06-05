from matplotlib.pyplot import *
import matplotlib.animation as animation
from nbody import *

PI = 3.14159265358979323
SOLAR_MASS = 4 * PI * PI
DAYS_PER_YEAR = 365.24

POSITIONS = ([0.0, 0.0, 0.0],
            [4.84143144246472090e+00,
             -1.16032004402742839e+00,
             -1.03622044471123109e-01],
            [8.34336671824457987e+00,
            4.12479856412430479e+00,
            -4.03523417114321381e-01],
            [1.28943695621391310e+01,
            -1.51111514016986312e+01,
            -2.23307578892655734e-01],
            [1.53796971148509165e+01,
             -2.59193146099879641e+01,
             1.79258772950371181e-01])

VELOCITIES = ([0.0, 0.0, 0.0],
               [1.66007664274403694e-03 * DAYS_PER_YEAR,
                 7.69901118419740425e-03 * DAYS_PER_YEAR,
                 -6.90460016972063023e-05 * DAYS_PER_YEAR],
               [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                4.99852801234917238e-03 * DAYS_PER_YEAR,
                2.30417297573763929e-05 * DAYS_PER_YEAR],
               [2.96460137564761618e-03 * DAYS_PER_YEAR,
                2.37847173959480950e-03 * DAYS_PER_YEAR,
                -2.96589568540237556e-05 * DAYS_PER_YEAR],
               [2.68067772490389322e-03 * DAYS_PER_YEAR,
                 1.62824170038242295e-03 * DAYS_PER_YEAR,
                 -9.51592254519715870e-05 * DAYS_PER_YEAR])

MASSES = (SOLAR_MASS,
        9.54791938424326609e-04 * SOLAR_MASS,
        2.85885980666130812e-04 * SOLAR_MASS,
        4.36624404335156298e-05 * SOLAR_MASS,
        5.15138902046611451e-05 * SOLAR_MASS
        )

BODIES = [POSITIONS, VELOCITIES, MASSES]

ims = []

fig, ax = subplots(edgecolor='w')

def step(i):
    cla()
    advance(BODIES, 0.01, 10)

    x_list = []
    y_list = []

    for [x, y, z] in BODIES[0]:
        x_list.append(x)
        y_list.append(y)

    line = plot(x_list, y_list, '.')
    axis([-40, 40, -40, 40])
    axis('off')
    return line,

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, bitrate=1800)

im_ani = animation.FuncAnimation(fig, step, range(500))
im_ani.save('planets.mp4', writer=writer)
