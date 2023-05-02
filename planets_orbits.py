import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
#import mpld3
#import streamlit.components.v1 as components
import time
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data



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


image_sun = plt.imread(path_sun)
image_mercury = plt.imread(path_mercury)
image_venus = plt.imread(path_venus)
image_earth = plt.imread(path_earth)
image_mars = plt.imread(path_mars)








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



# -------------------
# Make a plot
# -------------------
#fig = plt.figure()
#plt.plot(x_earth, y_earth, 'o', color='Red') 
#st.pyplot(fig)



#fig, ax = plt.subplots()

#max_x = 5
#max_rand = 10

#x = np.arange(0, max_x)
#ax.set_ylim(0, max_rand)
#line, = ax.plot(x, np.random.randint(0, max_rand, max_x))
#the_plot = st.pyplot(plt)

#def init():  # give a clean slate to start
#    line.set_ydata([np.nan] * len(x))

#def animate(i):  # update the y values (every 1000ms)
#    line.set_ydata(np.random.randint(0, max_rand, max_x))
#    the_plot.pyplot(plt)

#init()
#for i in range(100):
#    animate(i)
#    time.sleep(0.1)

#exit()



fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.8,0.95])
ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
plt.axis('off')
xy_max = 2.0
ax.axes.set_xlim([-xy_max,xy_max])
ax.axes.set_ylim([-xy_max,xy_max])
plt.plot([0,0], [-xy_max,xy_max], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([-xy_max,xy_max], [0,0], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], [-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], [xy_max/np.sqrt(2.0),-xy_max/np.sqrt(2.0)], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot(x_sun, y_sun, 'o', color='Gold', markersize=10)
plt.plot(x_mercury, y_mercury, '-', color='Grey', lw=0.5, alpha=0.3)
plt.plot(x_venus, y_venus, '-', color='Cyan', lw=0.5, alpha=0.3)
plt.plot(x_earth, y_earth, '-', color='Blue', lw=0.5, alpha=0.3)
plt.plot(x_mars, y_mars, '-', color='Red', lw=0.5, alpha=0.3)

ab = AnnotationBbox(OffsetImage(image_sun, zoom=0.06), (x_sun, y_sun), frameon=False)
ax.add_artist(ab)

#the_plot = st.pyplot(plt)

def animate_earth(i_ang):  
    point_earth, = plt.plot(x_earth[i_ang], y_earth[i_ang], 'o', color='Blue')
    #point_earth = AnnotationBbox(OffsetImage(image_earth, zoom=0.024), (x_earth[i_ang], y_earth[i_ang]), frameon=False)
    #ax.add_artist(point_earth)
    return point_earth

def animate_mercury(i_ang):  
    point_mercury, = plt.plot(x_mercury[i_ang], y_mercury[i_ang], 'o', color='Grey')
    #point_mercury = AnnotationBbox(OffsetImage(image_mercury, zoom=0.02), (x_mercury[i_ang], y_mercury[i_ang]), frameon=False)
    #ax.add_artist(point_mercury)
    return point_mercury

def animate_venus(i_ang):  
    point_venus, = plt.plot(x_venus[i_ang], y_venus[i_ang], 'o', color='Cyan')
    #point_venus = AnnotationBbox(OffsetImage(image_venus, zoom=0.021), (x_venus[i_ang], y_venus[i_ang]), frameon=False)
    #ax.add_artist(point_venus)
    return point_venus

def animate_mars(i_ang):  
    point_mars, = plt.plot(x_mars[i_ang], y_mars[i_ang], 'o', color='Red')
    #point_mars = AnnotationBbox(OffsetImage(image_mars, zoom=0.03), (x_mars[i_ang], y_mars[i_ang]), frameon=False)
    #ax.add_artist(point_mars)
    return point_mars

def animate_jupiter(i_ang):  
    point_jupiter, = plt.plot(x_jupiter[i_ang], y_jupiter[i_ang], 'o', color='Orange')
    #point_jupiter = AnnotationBbox(OffsetImage(image_jupiter, zoom=0.02), (x_jupiter[i_ang], y_jupiter[i_ang]), frameon=False)
    #ax.add_artist(point_jupiter)
    return point_jupiter

def animate_saturn(i_ang):  
    point_saturn, = plt.plot(x_saturn[i_ang], y_saturn[i_ang], 'o', color='Yellow')
    #point_saturn = AnnotationBbox(OffsetImage(image_saturn, zoom=0.02), (x_saturn[i_ang], y_saturn[i_ang]), frameon=False)
    #ax.add_artist(point_saturn)
    return point_saturn

def animate_uranus(i_ang):  
    point_uranus, = plt.plot(x_uranus[i_ang], y_uranus[i_ang], 'o', color='Yellow')
    #point_uranus = AnnotationBbox(OffsetImage(image_uranus, zoom=0.02), (x_uranus[i_ang], y_uranus[i_ang]), frameon=False)
    #ax.add_artist(point_uranus)
    return point_uranus

def animate_neptune(i_ang):  
    point_neptune, = plt.plot(x_neptune[i_ang], y_neptune[i_ang], 'o', color='Yellow')
    #point_neptune = AnnotationBbox(OffsetImage(image_neptune, zoom=0.02), (x_neptune[i_ang], y_neptune[i_ang]), frameon=False)
    #ax.add_artist(point_neptune)
    return point_neptune

for i_ang in np.arange(nsteps_ang):
    point_earth = animate_earth(i_ang)
    point_mercury = animate_mercury(i_ang)
    point_venus = animate_venus(i_ang)
    point_mars = animate_mars(i_ang)
    point_jupiter = animate_jupiter(i_ang)
    point_saturn = animate_saturn(i_ang)
    point_uranus = animate_uranus(i_ang)
    point_neptune = animate_neptune(i_ang)
    the_plot.pyplot(plt)
    time.sleep(0.0)
    #point_earth.remove()
    #point_mercury.remove()
    #point_venus.remove()
    #point_mars.remove()
    #point_jupiter.remove()
    #point_saturn.remove()
    #point_uranus.remove()
    #point_neptune.remove()    
    
st.pyplot(fig)

    
