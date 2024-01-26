import numpy as np 
import math as mt


theta = np.array([0, 0, 0])
dtheta_dt = np.array([0, 0, 0])
d2theta_dt2 = np.array([0, 0, 0])
nt = 10
dt = 0.001
for i in range(0, nt):
    theta = theta + dt*dtheta_dt
    dtheta_dt = dtheta_dt + dt*d2theta_dt2
    t = t + dt
  

















