import numpy as np
import math as m


def r(a, e, i, raan, w, f):
    r1 = np.array([[m.cos(raan), -m.sin(raan), 0], [m.sin(raan), m.cos(raan), 0], [0, 0, 1]])
    r2 = np.array([[1, 0, 0], [0, m.cos(i), -m.sin(i)], [0, m.sin(i), m.cos(i)]])
    r3 = np.array([[m.cos(w), -m.sin(w), 0], [m.sin(w), m.cos(w), 0], [0, 0, 1]])
    realign = np.matmul(r1, np.matmul(r2, r3))
    rrr = np.array([(a*(1-e**2)*m.cos(f))/(1 + e*m.cos(f)), (a*(1-e**2)*m.sin(f))/(1 + e*m.cos(f)), 0])
    return np.matmul(realign, rrr)


def v(a, e, i, raan, w, f, mu):
    r1 = np.array([[m.cos(raan), -m.sin(raan), 0], [m.sin(raan), m.cos(raan), 0], [0, 0, 1]])
    r2 = np.array([[1, 0, 0], [0, m.cos(i), -m.sin(i)], [0, m.sin(i), m.cos(i)]])
    r3 = np.array([[m.cos(w), -m.sin(w), 0], [m.sin(w), m.cos(w), 0], [0, 0, 1]])
    realign = np.matmul(r1, np.matmul(r2, r3))
    vvv = np.array([m.sqrt(mu/(a*(1 - e**2)))*e*m.sin(f), m.sqrt(mu / (a*(1 - e**2)))*(1 + e*m.cos(f)), 0])
    return np.matmul(realign, vvv)


def true_anomaly(e, mmm):
    eee = e_anomaly(e, mmm)
    return m.acos((m.cos(eee)-e)/(1-e*m.cos(eee)))


def e_anomaly(e, mmm):
    eee = m.pi
    for t in range(1, 100):
        if abs(mmm - eee + e * m.sin(eee)) < .001:
            return eee
        elif mmm - eee + e*m.sin(eee) > .001:
            eee = eee + m.pi * (.5**t)
        else:
            eee = eee - m.pi * (.5**t)
    print("Error: failure to achieve .001 precision below m.pi/2**100 precision")
