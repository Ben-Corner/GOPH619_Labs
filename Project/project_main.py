########
#Numerical solutions to 1D and 2D Acoustic Wave Equation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter





############
def gaussian(x,sigma,mu):
    return 1/(np.sqrt(2*np.pi*sigma)) * np.exp(-((x-mu)**2)/2)
x = np.linspace(-10,10,1000)
sigma = 1
mu = 0

#############
#Stability condition
#c*(dt/dx)<1
c0 = 343. #m/s
dx = 0.5 #m
dt = 0.001 #s
stab = c0 *(dt/dx)
if stab < 1:
    print("Stability condition passes:", stab)
else:
    print("Stability condition too large:", stab)

##############
#Initialization
Nx = 1000
Nt = 1001

isrc = 500 #Source location
ir = 730 #Reveiver location
f0 = 40
t0 = 4. / f0
src = np.zeros(Nt+1)
time = np.linspace(0,Nt*dt,Nt)
src = src  = -2. * (time - t0) * (f0 ** 2) * (np.exp(-1.0 * (f0 ** 2) * (time - t0) ** 2))

p = np.zeros(Nx)
p_old = np.zeros(Nx)
p_new = np.zeros(Nx)
d2px = np.zeros(Nx)

c = np.zeros(Nx)
c = c + c0

x = np.arange(Nx)
x = x * dx

seis = np.zeros(Nt)


for i in range(Nt//2):
    for j in range(1,Nx-2):
        d2px[j] = (p[j+1] - 2* p[j] + p[j-1])/ dx**2

    p_new = 2 * p - p_old + c**2 * dt**2 *d2px

    p_new[isrc] = p_new[isrc] +src[i] / (dx) * dt **2
    
    p_old, p = p, p_new

    # seis[i] = p[ir]
    

if __name__ == "__main__":
