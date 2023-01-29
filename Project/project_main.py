########
#Numerical solutions to 1D and 2D Acoustic Wave Equation
import numpy as np
import matplotlib.pyplot as plt
###Test for matlab from wikiseg
# Initialization
Nx = 101      
dx = 1         
x= np.arange(0,Nx-1,dx)
mpx = (Nx+1)/2; 
                                
T = 1001      
f = 10        
dt = 0.001  
t= np.arange(0,T-1,dt)
v = 500
c = v*(dt/dx)
U = np.zeros([T,Nx]) 
s1 = int(np.floor(T/f))

####
U[0,:] = np.sin(2*np.pi*f*t[0:s1+1])
# U((1:s1),1) = sin(2*pi*f.*t(1:s1));
# U((1:s1),2) = sin(2*pi*f.*t(1:s1));
for j in range(T):
    for i in range(1,Nx-1):
            U1 = 2*U[j,i] - U[j-1,i]
            U2 = U[j,i-1] - 2* U[j,i] + U[j,i+1]
            U[j,i] = U1 + c*U2
# for j = 3:T
#     for i = 2:Nx-1
#         U1 = 2*U(j-1,i)-U(j-2,i);
#         U2 = U(j-1,i-1)-2*U(j-1,i)+U(j-1,i+1);
#         U(j,i) = U1 + c*c.*U2;    
#     end                   
# end
###########
if __name__ == "__main__":
    plt.plot(x,U[0,:]-1)
    plt.show()
    print(U[0,:].shape)
