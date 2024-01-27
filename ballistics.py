import numpy as np
import math as mt


re = 6.3781*10**6  # meters,   radius of the earth


def gps3c2pos(altitude, latitude, longitutde):
    return np.arrray([(altitude+re)*mt.cos(latitude)*mt.cos(longitude), (altitude+re)*mt.cos(latitude)*mt.sin(longitude), (altitude+re)*mt.sin(latitude)])
    x = 
    y = 
    z = (altitude+re)*mt.sin(latitude)
    

class BallisticProjectile:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = np.array([0, 0, 0])

    def time_evolve_uniform_low_altitude(dt):
        self.acceleration = np.array([0, 0, -9.81])
        self.position = self.position + dt*self.velocity
        self.velocity = self.velocity + self.acceleration*dt
        t = t + dt

    def time_advance(nt, dt):
        for i in range(0, nt):
            self.time_evolve_low_altitude(dt)
        
