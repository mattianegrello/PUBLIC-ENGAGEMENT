

import numpy as np
import streamlit as st
#import matplotlib.pyplot as plt
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

path_sun = '/Users/mattianegrello/CHART_OUTREACH/ACTIVITIES/sun.png'
path_mercury = '/Users/mattianegrello/CHART_OUTREACH/ACTIVITIES/mercury.png'
path_venus = '/Users/mattianegrello/CHART_OUTREACH/ACTIVITIES/venus_lowres.png'
path_earth = '/Users/mattianegrello/CHART_OUTREACH/ACTIVITIES/earth.png'
path_mars = '/Users/mattianegrello/CHART_OUTREACH/ACTIVITIES/mars.png'


image_sun = plt.imread(path_sun)
image_mercury = plt.imread(path_mercury)
image_venus = plt.imread(path_venus)
image_earth = plt.imread(path_earth)
image_mars = plt.imread(path_mars)








st.header('The Solar System')

st.write(' ')
