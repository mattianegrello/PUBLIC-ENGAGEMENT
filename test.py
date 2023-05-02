

import numpy as np
import streamlit as st
#import matplotlib.pyplot as plt
#from scipy.interpolate import interp1d
import scipy
import time

st.write('Hello')

# %%%%%%%%%%%%%%%%%%
# %% SOLAR SYSTEM %%
# %%%%%%%%%%%%%%%%%%

# **********************
# Info about the planets
# **********************
#
# Earth:
Period_earth = 365.2564 # days
Distance_earth = 1.0  # AU
#
# Mercury:
Period_mercury = 87.9693 # days
Distance_mercury = 0.38710  # AU
#
# Venus:
Period_venus = 224.7008 # days
Distance_venus = 0.72333  # AU
#
# Mars:
Period_mars = 686.9796 # days
Distance_mars = 1.52366  # AU
#
# Jupiter:
Period_jupiter = 4332.8201 # days
Distance_jupiter = 5.20336  # AU
#
# Saturn:
Period_saturn = 10775.599 # days
Distance_saturn = 9.53707  # AU
#
# Uranus:
Period_uranus = 30687.153 # days
Distance_uranus = 19.1913  # AU
#
# Neptune:
Period_neptune = 60190.03 # days
Distance_neptune = 30.0690  # AU


#image_sun = get_sample_data('/Users/mattianegrello/CHART_OUTREACH/ACTIVITIES/sun.png')

path_sun = 'sun.png'
path_mercury = 'mercury.png'
path_venus = 'venus_lowres.png'
path_earth = 'earth.png'
path_mars = 'mars.png'







st.header('The Solar System')

st.write(' ')



# Steps in angle along the orbit [radiants]
fac = 4
nsteps_ang = 100 * fac
ang_min = 0.0
ang_max = 2.0*np.pi * fac
ang_steps = np.linspace(ang_min,ang_max, nsteps_ang)

# ---
# SUN
# ---
x_sun = 0.0
y_sun = 0.0

# -----
# EARTH
# -----
T_earth = 1.0
R_earth = 1.0
x_earth = R_earth*np.cos(ang_steps)
y_earth = R_earth*np.sin(ang_steps)

# -------
# MERCURY
# -------
T_mercury = Period_earth/Period_mercury
D_mercury = Distance_mercury
x_mercury = D_mercury*np.cos(ang_steps*T_mercury)
y_mercury = D_mercury*np.sin(ang_steps*T_mercury)

# -----
# VENUS
# -----
T_venus = Period_earth/Period_venus
D_venus = Distance_venus
x_venus = D_venus*np.cos(ang_steps*T_venus)
y_venus = D_venus*np.sin(ang_steps*T_venus)

# ----
# MARS
# ----
T_mars = Period_earth/Period_mars
D_mars = Distance_mars
x_mars = D_mars*np.cos(ang_steps*T_mars)
y_mars = D_mars*np.sin(ang_steps*T_mars)

# -------
# JUPITER
# -------
T_jupiter = Period_earth/Period_jupiter
D_jupiter = Distance_jupiter
x_jupiter = D_jupiter*np.cos(ang_steps*T_jupiter)
y_jupiter = D_jupiter*np.sin(ang_steps*T_jupiter)

# ------
# SATURN
# ------
T_saturn = Period_earth/Period_saturn
D_saturn = Distance_saturn
x_saturn = D_saturn*np.cos(ang_steps*T_saturn)
y_saturn = D_saturn*np.sin(ang_steps*T_saturn)

# ------
# URANUS
# ------
T_uranus = Period_earth/Period_uranus
D_uranus = Distance_uranus
x_uranus = D_uranus*np.cos(ang_steps*T_uranus)
y_uranus = D_uranus*np.sin(ang_steps*T_uranus)

# -------
# NEPTUNE
# -------
T_neptune = Period_earth/Period_neptune
D_neptune = Distance_neptune
x_neptune = D_neptune*np.cos(ang_steps*T_neptune)
y_neptune = D_neptune*np.sin(ang_steps*T_neptune)


