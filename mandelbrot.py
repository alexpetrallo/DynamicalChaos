#renderes different zoom points of a mandelbrot set, saved figures to make a gif
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure


# xvalues = np.linspace(-0.22, -0.21, 1000)
# yvalues = np.linspace(-0.70, -0.69, 1000)

# x1 = -0.2175
# x2 = -0.2125
#
# y1 = -0.6975
# y2 = -0.6925

x1 = -0.21625
x2 = -0.21375

y1 = -0.69625
y2 = -0.69375




for i in range(12):

    # x1 = -0.21615
    # x2 = 1
    # x2 = -0.21385
    # y1 = -.69615
    # y2 = -.69385

    # y1 = -0.70
    # y2 = -0.69

    xvalues = np.linspace(x1, x2, 1000)
    yvalues = np.linspace(y1, y2, 1000)

    # size of these lists of x and y values
    xlen = len(xvalues)
    ylen = len(yvalues)


    def mandel(c, maxiter):
        # starting value of complex z is 0+0i before iterations update it
        z = complex(0, 0)

        # start iterating and stop when it's done maxiter times
        for iteration in range(maxiter):

            # the main function which generates the output value of z from the input values using the formula (z^2) + c
            z = (z * z) + c

            # check if the (pythagorean) magnitude of the output complex number z is bigger than 4, and if so stop iterating as we've diverged already
            if abs(z) > 4:
                break
                pass
            pass

        # return the number of iterations we actually did, not the final value of z, as this tells us how quickly the values diverged past the magnitude threshold of 4
        return iteration


    atlas = np.zeros((xlen, ylen))



    # go through each point in this atlas array and test to see how many iterations are needed to diverge (or reach the maximum iterations when not diverging)
    for ix in range(xlen):
        for iy in range(ylen):
            # at this point in the array, work out what the actual real and imaginary parts of x are by looking it up in the xvalue and yvalue lists
            cx = xvalues[ix]
            cy = yvalues[iy]
            c = complex(cx, cy)

            # now we know what c is for this place in the atlas, apply the mandel() function to return the number of iterations it took to diverge
            # we use 40 maximum iterations to stop and accept the function didn't diverge
            atlas[ix, iy] = mandel(c, 120)

            pass
        pass
    # figure.figsize(18,18)

    # plot the array atlas as an image, with its values represented as colours, peculiarity of python that we have to transpose the array
    plt.imshow(atlas.T, interpolation="nearest", cmap="jet")
    # plt.xlabel()
    # plt.ylabel()
    plt.title("Mandelbrot set")
    plt.savefig("figure" + str(i) + ".png")
    xDiff = ((x1 - x2) * .90) / 2
    x1 = x1 + xDiff
    x2 = x2 - xDiff

    yDiff = ((x1 - x2) * .90) / 2
    y1 = y1 + yDiff
    y2 = y2 - yDiff

    print("x1:", str(x1))
    print("x2:", str(x2))

    print("y1:", str(y1))
    print("y2:", str(y2))


