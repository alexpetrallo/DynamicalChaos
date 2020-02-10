
import numpy as np
from scipy import *
import matplotlib.pyplot as plt

from random import randrange



N = 250;
def stdmap(list):
    pn = mod(list[1] + K*cos(list[0]), 2*pi)
    xn = mod(list[0] + pn, 2*pi)
    return (xn, pn)


x0 = np.linspace(0, 2*pi, 32)
p0 = np.linspace(0, 2*pi, 32)
mesh = []
for i in range(len(x0)):
    for j in range(len(p0)):
        mesh.append((x0[i], p0[j]))

Kvals = np.linspace(0, 2.1, 15)
i = 0
for val in Kvals:
    K = val
    # fig = plt.figure(figsize=(5, 5))
    for item in mesh:
        traj = [item]
        for ii in range(N):
            traj.append(stdmap(traj[ii]))
        traj = np.array(traj)
        # plt.scatter(traj.T[0], traj.T[1])
        plt.plot(traj.T[0], traj.T[1], '.', linewidth=20)


    plt.xlim([0, 2*pi])
    plt.ylim([0, 2*pi])
    plt.xlabel('Position (rad)')
    plt.ylabel('Momentum')
    plt.title("K = " + str(K))
    # plt.show()
    plt.savefig('stdmap'+ str(i)+'.png')
    i = i + 1

