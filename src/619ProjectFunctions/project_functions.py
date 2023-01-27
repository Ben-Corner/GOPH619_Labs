#######
#Project Functions
import numpy as np
import matplotlib.pyplot as plt
###########
def ricker(t,f):
    """Ricker wavlet

    Parameters
    ----------
    t : array_like: time array
    f : scaler: frequency values

    Returns
    -------
    r : array_like: 
    """
#####Version 1
    # A = ( 1 - (0.5 * f**2 * t**2))
    # B = np.exp(-0.25 * f**2 * t**2)
    # r = A*B
#####Version 2
    A = (1 - 2*np.pi**2 * f**2 * t**2)
    B = np.exp(-1*np.pi**2 *f**2 *t**2)
    r = A*B
    return r

#############################################


if __name__ == "__main__":
    dt = 0.002
    t = np.arange(-0.07,0.07,dt)
    r = ricker(t,20)
    plt.plot(t,r)
    plt.show()

