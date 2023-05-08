

# --------
# Packages
# --------
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
from astropy.io import ascii
import time

# -------------------------
# Set-up page configuration
# -------------------------
st.set_page_config(layout='centered')    
    
# ---------------------
# Images of the planets
# ---------------------
image_mercury = plt.imread('images/mercury.png')
image_venus = plt.imread('images/venus.png')
image_earth = plt.imread('images/earth.png')
image_mars = plt.imread('images/mars.png')
image_jupiter = plt.imread('images/jupiter.png')
image_saturn = plt.imread('images/saturn.png')
image_uranus = plt.imread('images/uranus.png')
image_neptune = plt.imread('images/neptune.png')

# ----------------------
# Info about the planets
# ----------------------
data = ascii.read('info_planets/planets.txt')
planet_name = data['NAME']              
planet_D_km = data['DISTANCE[km]']
planet_P_Edays = data['PERIOD[Earth-days]']

mercury = {'D_km':planet_D_km[0], 'P_Edays':planet_P_Edays[0], 'D_AU':planet_D_km[0]/planet_D_km[2]}
venus = {'D_km':planet_D_km[1], 'P_Edays':planet_P_Edays[1], 'D_AU':planet_D_km[1]/planet_D_km[2]}
earth = {'D_km':planet_D_km[2], 'P_Edays':planet_P_Edays[2], 'D_AU':planet_D_km[2]/planet_D_km[2]}
mars = {'D_km':planet_D_km[3], 'P_Edays':planet_P_Edays[3], 'D_AU':planet_D_km[3]/planet_D_km[2]}
jupiter = {'D_km':planet_D_km[4], 'P_Edays':planet_P_Edays[4], 'D_AU':planet_D_km[4]/planet_D_km[2]}
saturn = {'D_km':planet_D_km[5], 'P_Edays':planet_P_Edays[5], 'D_AU':planet_D_km[5]/planet_D_km[2]}
uranus = {'D_km':planet_D_km[6], 'P_Edays':planet_P_Edays[6], 'D_AU':planet_D_km[6]/planet_D_km[2]}
neptune =  {'D_km':planet_D_km[7], 'P_Edays':planet_P_Edays[7], 'D_AU':planet_D_km[7]/planet_D_km[2]}


# ========================================
# Create a sidebar where to input the data
# ========================================
#
with st.sidebar:

    col1_width = 1
    col2_width = 1.5
    
    col1, col2 = st.columns((col1_width,col2_width))
    col1.subheader('Planet')
    col2.subheader('Period (in Earth days)')
    col1.write(' ')
    col2.write(' ')
    
#   Mercury
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('MERCURY')
    col1.image(image_mercury, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    P_mercury = col2.number_input('$P_{Mercury}$', format='%0.1f', step=0.1, label_visibility='collapsed')

    st.write('')
    
#   Venus
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('VENUS')
    col1.image(image_venus, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    P_venus = col2.number_input('$P_{Venus}$', format='%0.1f', step=0.1, label_visibility='collapsed')

    st.write('')
    
#   Earth
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('EARTH')
    col1.image(image_earth, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    P_earth = col2.number_input('$P_{Earth}$', format='%0.1f', step=0.1, label_visibility='collapsed')

    st.write('')
    
#   Mars
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('MARS')
    col1.image(image_mars, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    P_mars = col2.number_input('$P_{Mars}$', format='%0.1f', step=0.1, label_visibility='collapsed')

    st.write('')
    
#   Jupiter
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('JUPITER')
    col1.image(image_jupiter, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    P_jupiter = col2.number_input('$P_{Jupiter}$', format='%0.1f', step=0.1, label_visibility='collapsed')

    st.write('')
    
#   Saturn
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('SATURN')
    col1.image(image_saturn, width=80)
    col2.write('')
    col2.write('')
    P_saturn = col2.number_input('$P_{Saturn}$', format='%0.1f', step=0.1, label_visibility='collapsed')

    st.write('')
    
#   Uranus
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('URANUS')
    col1.image(image_uranus, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    P_uranus = col2.number_input('$P_{Uranus}$', format='%0.1f', step=0.1, label_visibility='collapsed')

    st.write('')
    
#   Neptune
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('NEPTUNE')
    col1.image(image_neptune, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    P_neptune = col2.number_input('$P_{Neptune}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    


st.header('The solar system')
st.subheader('Orbital period versus Distance from the Sun')

st.write(' ')
st.write(' ')

st.write('Use the sidebar on the left to input the observed orbital period of the planets in Earth days')
st.write('The data will appear in the table and the plot below as a function of the planets distance from the Sun')

st.write(' ')
st.write(' ')

# =========================================
# Table summarizing the info on the planets
# =========================================
col1, col2, col3, col4, col5 = st.columns((1,1,1,1,1))
#
col1.write('Planet')
col2.write('Distance')
col3.write('Distance')
col4.write('Period')
col5.write('Period')
#
col1.write('')
col2.write('(in billion km)')
col3.write('(in AU)')
col4.write('(in Earth days)')
col5.write('(in Earth years)')
#
col1.write('Mercury')
col2.write(mercury['D_km']/10.0**9.0, format='%0.001f')
col3.write(mercury['D_AU'])
col4.write(P_mercury)
col5.write(P_mercury/P_earth)
#
col1.write('Venus')
col2.write(venus['D_km']/10.0**9.0, format='%0.001f')
col3.write(venus['D_AU'])
col4.write(P_venus)
col5.write(P_venus/P_earth)
#
col1.write('Earth')
col2.write(earth['D_km']/10.0**9.0, format='%0.001f')
col3.write(earth['D_AU'])
col4.write(P_earth)
col5.write(P_earth/P_earth)
#
col1.write('Mars')
col2.write(mars['D_km']/10.0**9.0, format='%0.001f')
col3.write(mars['D_AU'])
col4.write(P_mars)
col5.write(P_mars/P_earth)
#
col1.write('Jupiter')
col2.write(jupiter['D_km']/10.0**9.0, format='%0.001f')
col3.write(jupiter['D_AU'])
col4.write(P_jupiter)
col5.write(P_jupiter/P_earth)
#
col1.write('Saturn')
col2.write(saturn['D_km']/10.0**9.0, format='%0.001f')
col3.write(saturn['D_AU'])
col4.write(P_saturn)
col5.write(P_saturn/P_earth)
#
col1.write('Uranus')
col2.write(uranus['D_km']/10.0**9.0, format='%0.001f')
col3.write(uranus['D_AU'])
col4.write(P_uranus)
col5.write(P_uranus/P_earth)
#
col1.write('Neptune')
col2.write(neptune['D_km']/10.0**9.0, format='%0.001f')
col3.write(neptune['D_AU'])
col4.write(P_neptune)
col5.write(P_neptune/P_earth)


st.write(' ')
st.write(' ')


# ===============================
# GRAPH of Period versus Distance
# ===============================
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.8,0.95])
ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
ax.axes.set_xlim([0.01,10.0])
ax.axes.set_ylim([50.0,10.0**5.0])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Distance (in billion km)', size='15')
plt.ylabel('Period (in Earth days)', size='15')

plt.xticks([0.01, 0.1, 1.0, 10.0],
           [r'$0.01$', r'$0.1$', r'$1$', r'$10$'], size='14')
#plt.xticks([0.05, 0.5, 5.0],
#           [r'$0.05$', r'$0.5$', r'$5$'], size='9', minor=True)

plt.yticks([100.0, 1000.0, 10000.0, 100000.0],
           [r'$100$', r'$1000$', r'$10\,000$', r'$100\,000$'], size='14')

# Mercury
x = mercury['D_km']/10.0**9.0
y = P_mercury
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_mercury = AnnotationBbox(OffsetImage(image_mercury, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_mercury)

# Venus
x = venus['D_km']/10.0**9.0
y = P_venus
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_venus = AnnotationBbox(OffsetImage(image_venus, zoom=0.02), (x,y), frameon=False)
ax.add_artist(point_venus)

# Earth
x = earth['D_km']/10.0**9.0
y = P_earth
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_earth = AnnotationBbox(OffsetImage(image_earth, zoom=0.02), (x,y), frameon=False)
ax.add_artist(point_earth)

# Mars
x = mars['D_km']/10.0**9.0
y = P_mars
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_mars = AnnotationBbox(OffsetImage(image_mars, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_mars)

# Jupiter
x = jupiter['D_km']/10.0**9.0
y = P_jupiter
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_jupiter = AnnotationBbox(OffsetImage(image_jupiter, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_jupiter)

# Saturn
x = saturn['D_km']/10.0**9.0
y = P_saturn
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_saturn = AnnotationBbox(OffsetImage(image_saturn, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_saturn)

# Uranus
x = uranus['D_km']/10.0**9.0
y = P_uranus
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_uranus = AnnotationBbox(OffsetImage(image_uranus, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_uranus)

# Neptune
x = neptune['D_km']/10.0**9.0
y = P_neptune
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_neptune = AnnotationBbox(OffsetImage(image_neptune, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_neptune)


# -------------------------------
# BUTTON to show kepler third law
# -------------------------------
if st.button('Press button to Diplay Kepler third law'):
    M_sun = 1.989*10.0**30.0  # kg
    G_grav = 6.6743*10.0**(-11.0)  # m^3 kg^-1 s^-2
    G_grav = G_grav * 10.0**(-9.0) * (1.15741*10.0**(-5.0))**(-2.0)             # km^3 kg^-1 day^-2
    D_bkm = 10.0**np.linspace(-3.0,3.0,100)   # bilion km
    P_days = np.sqrt(4.0*np.pi**2.0/G_grav/M_sun*(D_bkm*10.0**9.0)**3.0)  # 
    plt.plot(D_bkm, P_days, '-', color='Red', lw='0.5', alpha=0.5)

# -------------------
# BUTTON to show grid
# -------------------
if st.button('Press button to show grid'):
    plt.grid(which='minor', ls=':', lw=0.5)
    plt.grid(which='major', lw=0.5)
    
st.pyplot(fig)






st.write('')




# ===============================
# GRAPH of Period versus Distance
# ===============================
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.8,0.95])
ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
ax.axes.set_xlim([0.0,10.0])
ax.axes.set_ylim([0.0,10.0**5.0])
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Distance (in billion km)', size='15')
plt.ylabel('Period (in Earth days)', size='15')

#plt.xticks([0.01, 0.1, 1.0, 10.0],
#           [r'$0.01$', r'$0.1$', r'$1$', r'$10$'], size='14')

#plt.yticks([100.0, 1000.0, 10000.0, 100000.0],
#           [r'$100$', r'$1000$', r'$10\,000$', r'$100\,000$'], size='14')

# Mercury
x = mercury['D_km']/10.0**9.0
y = P_mercury
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_mercury = AnnotationBbox(OffsetImage(image_mercury, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_mercury)

# Venus
x = venus['D_km']/10.0**9.0
y = P_venus
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_venus = AnnotationBbox(OffsetImage(image_venus, zoom=0.02), (x,y), frameon=False)
ax.add_artist(point_venus)

# Earth
x = earth['D_km']/10.0**9.0
y = P_earth
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_earth = AnnotationBbox(OffsetImage(image_earth, zoom=0.02), (x,y), frameon=False)
ax.add_artist(point_earth)

# Mars
x = mars['D_km']/10.0**9.0
y = P_mars
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_mars = AnnotationBbox(OffsetImage(image_mars, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_mars)

# Jupiter
x = jupiter['D_km']/10.0**9.0
y = P_jupiter
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_jupiter = AnnotationBbox(OffsetImage(image_jupiter, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_jupiter)

# Saturn
x = saturn['D_km']/10.0**9.0
y = P_saturn
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_saturn = AnnotationBbox(OffsetImage(image_saturn, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_saturn)

# Uranus
x = uranus['D_km']/10.0**9.0
y = P_uranus
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_uranus = AnnotationBbox(OffsetImage(image_uranus, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_uranus)

# Neptune
x = neptune['D_km']/10.0**9.0
y = P_neptune
plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=0.5)
plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=0.5)
point_neptune = AnnotationBbox(OffsetImage(image_neptune, zoom=0.025), (x,y), frameon=False)
ax.add_artist(point_neptune)
    
st.pyplot(fig)




exit()





