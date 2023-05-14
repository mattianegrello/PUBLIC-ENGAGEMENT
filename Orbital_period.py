

# --------
# Packages
# --------
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
from astropy.io import ascii
import time

def ChangeWidgetFontSize(wgt_txt, wch_font_size = '12px'):
    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('p'), i;
                for (i = 0; i < elements.length; ++i) 
                    { if (elements[i].textContent.includes(|wgt_txt|)) 
                        { elements[i].style.fontSize ='""" + wch_font_size + """'; } }</script>  """

    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
    components.html(f"{htmlstr}", height=0, width=0)



# ------------------------------------------------------------
# Initialise session_state for the different parts of the code
# ------------------------------------------------------------
if 'GRAPH_1' not in st.session_state:
    st.session_state.GRAPH_1 = False
if 'GRAPH_2' not in st.session_state:
    st.session_state.GRAPH_2 = False
if 'PLOT_1' not in st.session_state:
    st.session_state.PLOT_1 = False
if 'PLOT_2' not in st.session_state:
    st.session_state.PLOT_2 = False
if 'sol_Q1' not in st.session_state:
    st.session_state.sol_Q1 = False
if 'sol_Q2' not in st.session_state:
    st.session_state.sol_Q2 = False
if 'sol_Q3' not in st.session_state:
    st.session_state.sol_Q3 = False
if 'sol_Q4' not in st.session_state:
    st.session_state.sol_Q4 = False
    
    
# -------------------------
# Set up page configuration
# -------------------------
st.set_page_config(layout='wide')
    
    
st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

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
image_sun = plt.imread('images/sun.png')

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





# =============================================
# Create a sidebar with some info about planets
# =============================================
#
with st.sidebar:

    col1_width = 1
    col2_width = 1.5
    
    col1, col2 = st.columns((col1_width,col2_width))
    col1.subheader('Planet')
    col2.subheader('Distance from Sun (in million km)')
    col1.write(' ')
    col2.write(' ')

#   Mercury
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('MERCURY')
    col1.image(image_mercury, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #col2.write(str(np.round(mercury['D_km']/10.0**6.0,1)), fontsize=40)
    col2.markdown('<p class="big-font">'+str(np.round(mercury['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 

    st.write('')
    
#   Venus
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('VENUS')
    col1.image(image_venus, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #col2.write(np.round(venus['D_km']/10.0**6.0,1))
    col2.markdown('<p class="big-font">'+str(np.round(venus['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 

    st.write('')
    
#   Earth
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('EARTH')
    col1.image(image_earth, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #col2.write(np.round(earth['D_km']/10.0**6.0,1))
    col2.markdown('<p class="big-font">'+str(np.round(earth['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 

    st.write('')
    
#   Mars
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('MARS')
    col1.image(image_mars, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #col2.write(np.round(mars['D_km']/10.0**6.0,1))
    col2.markdown('<p class="big-font">'+str(np.round(mars['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 

    st.write('')
    
#   Jupiter
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('JUPITER')
    col1.image(image_jupiter, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #col2.write(np.round(jupiter['D_km']/10.0**6.0,1))
    col2.markdown('<p class="big-font">'+str(np.round(jupiter['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 

    st.write('')
    
#   Saturn
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('SATURN')
    col1.image(image_saturn, width=80)
    col2.write('')
    col2.write('')
    #col2.write(np.round(saturn['D_km']/10.0**6.0,1))
    col2.markdown('<p class="big-font">'+str(np.round(saturn['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 

    st.write('')
    
#   Uranus
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('URANUS')
    col1.image(image_uranus, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #col2.write(np.round(uranus['D_km']/10.0**6.0,1))
    col2.markdown('<p class="big-font">'+str(np.round(uranus['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 

    st.write('')
    
#   Neptune
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('NEPTUNE')
    col1.image(image_neptune, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #col2.write(np.round(neptune['D_km']/10.0**6.0,1))
    col2.markdown('<p class="big-font">'+str(np.round(neptune['D_km']/10.0**6.0,1))+'</p>', unsafe_allow_html=True) 



    
    
st.header('The solar system: orbital period of the planets')

st.write(' ')
st.write(' ')

st.markdown('**DEFINITIONS**:')
st.markdown('- The **ORBIT** of a planet around the Sun is the repeating path in space taken by the planet around the Sun. It can be approximated with a **circle**; therefore, the radius of the orbit of a planet correspond to the distance of the planet from the Sun. The distance of the Earth from the Sun is referred to as an **Astronomical Unit (AU)** and measures about **150 million km**. The sidebar on the left shows the distance of each planet from the Sun in units of million km. Can you work out the distance of the planets in AU?')

image_orbit = plt.imread('images/Orbit.png')
st.image(image_orbit)

st.write('')
st.markdown('- The **ORBITAL PERIOD** of a planet is the time it takes the planet to complete an orbit around the Sun. For the Earth this corresponds to 365.3 days (or 1 year). Hereafter, we will refer to the orbital period of the Earth as 1 **Earth year**. In fact, as you will see, the concept of year (as well as the concept of day) is planet-dependent, because different planets have different orbital periods.')

st.write('')

st.markdown('**INSTRUCTIONS**: The animations below show the planets moving along their orbits around the Sun. Time is shown in terms of Earth days. Play with the animations to find out the number of Earth days it takes each planet to complete a single orbit around the Sun. Write down your findings. The sidebar on the left shows the distance of each planet from the Sun, measured in million of km. Once you are done with the animations, answer the questions.')

st.write(' ')
st.write(' ')




# ---
# SUN
# ---
x_sun = 0.0
y_sun = 0.0






# %%%%%%%%%%%%%%%%%%%
# %% INNER PLANETS %%
# %%%%%%%%%%%%%%%%%%%

# Steps in angle along the orbit [radiants]
n_Eorbits = 3  
nsteps_ang = 50 * n_Eorbits
ang_min = 0.0
ang_max = 2.0*np.pi * n_Eorbits
ang_steps = np.linspace(ang_min, ang_max, nsteps_ang)
index_ang = np.arange(nsteps_ang)
Edays_steps = ang_steps / ((2.0*np.pi)/earth['P_Edays'])

# -------
# MERCURY
# -------
fac = earth['P_Edays']/mercury['P_Edays']
x_mercury = mercury['D_AU']*np.cos(ang_steps*fac)
y_mercury = mercury['D_AU']*np.sin(ang_steps*fac)

# -----
# VENUS
# -----
fac = earth['P_Edays']/venus['P_Edays']
x_venus = venus['D_AU']*np.cos(ang_steps*fac)
y_venus = venus['D_AU']*np.sin(ang_steps*fac)

# -----
# EARTH
# -----
fac = earth['P_Edays']/earth['P_Edays']
x_earth = earth['D_AU']*np.cos(ang_steps*fac)
y_earth = earth['D_AU']*np.sin(ang_steps*fac)

# -----
# MARS
# -----
fac = earth['P_Edays']/mars['P_Edays']
x_mars = mars['D_AU']*np.cos(ang_steps*fac)
y_mars = mars['D_AU']*np.sin(ang_steps*fac)





expander_label = 'ANIMATION: Mercury, Venus, Earth, Mars'
with st.expander(expander_label) or st.session_state.GRAPH_1:

#   Update session_state:
    st.session_state.GRAPH_1 = True

    #width = st.slider("plot width", 1, 25, 3)
    #height = st.slider("plot height", 1, 25, 1)

    fig = plt.figure()
    #fig = plt.figure(figsize=(10,10))
    ax = fig.add_axes([0.15,0.05,0.8,0.95])
    ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
    plt.axis('off')
    xy_max = 1.6
    ax.axes.set_xlim([-xy_max,xy_max])
    ax.axes.set_ylim([-xy_max,xy_max])
    #plt.plot([0,0], [-xy_max,xy_max], '--', color='Black', lw='0.5', alpha=0.5)
    #plt.plot([-xy_max,xy_max], [0,0], '--', color='Black', lw='0.5', alpha=0.5)
    #plt.plot([-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], [-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], '--', color='Black', lw='0.5', alpha=0.5)
    #plt.plot([-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], [xy_max/np.sqrt(2.0),-xy_max/np.sqrt(2.0)], '--', color='Black', lw='0.5', alpha=0.5)
    plt.plot([0.0,xy_max], [0.0,0.0], '--', color='Black', lw='0.5', alpha=0.5)

    ab = AnnotationBbox(OffsetImage(image_sun, zoom=0.04), (x_sun, y_sun), frameon=False)
    ax.add_artist(ab)
    
    x = np.cos(ang_steps)
    y = np.sin(ang_steps)
    plt.plot(mercury['D_AU']*x, mercury['D_AU']*y, '-', color='Grey', lw=0.5, alpha=0.3)
    plt.plot(venus['D_AU']*x, venus['D_AU']*y, '-', color='Cyan', lw=0.5, alpha=0.3)
    plt.plot(earth['D_AU']*x, earth['D_AU']*y, '-', color='Blue', lw=0.5, alpha=0.3)
    plt.plot(mars['D_AU']*x, mars['D_AU']*y, '-', color='Red', lw=0.5, alpha=0.3)
    
    point_mercury, = plt.plot([], [], 'o', color='Grey')
    point_venus, = plt.plot([], [], 'o', color='Cyan')
    point_earth, = plt.plot([], [], 'o', color='Blue')
    point_mars, = plt.plot([], [], 'o', color='Red')
    label = ax.text(-0.15, 0.90, 'initialise', transform=ax.transAxes, fontsize='13',
                        bbox=dict(facecolor='none', edgecolor='black', pad=10.0))

    label_mercury = ax.annotate('Mercury', xy=(0,0), xytext=(1.0,0.0), color='Grey', fontsize='8')
    label_venus = ax.annotate('Venus', xy=(0,0), xytext=(1.0,0.0), color='Cyan', fontsize='8')
    label_earth = ax.annotate('Earth', xy=(0,0), xytext=(1.0,0.0), color='Blue', fontsize='8')
    label_mars = ax.annotate('Mars', xy=(0,0), xytext=(1.0,0.0), color='Red', fontsize='8')
    
    def animate_inner_planets(i_ang):
        point_mercury.set_data(x_mercury[i_ang], y_mercury[i_ang])
        point_venus.set_data(x_venus[i_ang], y_venus[i_ang])
        point_earth.set_data(x_earth[i_ang], y_earth[i_ang])
        point_mars.set_data(x_mars[i_ang], y_mars[i_ang])
        label.set_text('Earth days: '+str(round(Edays_steps[i_ang],1)))
        label_mercury.set_position((x_mercury[i_ang]+0.04, y_mercury[i_ang]+0.04))
        label_venus.set_position((x_venus[i_ang]+0.04, y_venus[i_ang]+0.04))
        label_earth.set_position((x_earth[i_ang]+0.04, y_earth[i_ang]+0.04))
        label_mars.set_position((x_mars[i_ang]+0.04, y_mars[i_ang]+0.04))
        return point_earth, label, label_earth,
    
    #orbits_animation = animation.FuncAnimation(fig, animate_planets, interval=100, blit=True)
    orbits_animation = animation.FuncAnimation(fig, animate_inner_planets, index_ang, interval=100, blit=True)
    components.html(orbits_animation.to_jshtml(), height=600)

ChangeWidgetFontSize(expander_label, wch_font_size='25px')




# %%%%%%%%%%%%%%%%%%%
# %% OUTER PLANETS %%
# %%%%%%%%%%%%%%%%%%%

# Steps in angle along the orbit [radiants]
n_Norbits = 1  
nsteps_ang = 100 * n_Norbits
ang_min = 0.0
ang_max = 2.0*np.pi * n_Norbits
ang_steps = np.linspace(ang_min, ang_max, nsteps_ang)
index_ang = np.arange(nsteps_ang)
Edays_steps = ang_steps / ((2.0*np.pi)/neptune['P_Edays']) 

# -------
# JUPITER
# -------
fac = neptune['P_Edays']/jupiter['P_Edays']
x_jupiter = jupiter['D_AU']*np.cos(ang_steps*fac)
y_jupiter = jupiter['D_AU']*np.sin(ang_steps*fac)
        
# ------
# SATURN
# ------
fac = neptune['P_Edays']/saturn['P_Edays']
x_saturn = saturn['D_AU']*np.cos(ang_steps*fac)
y_saturn = saturn['D_AU']*np.sin(ang_steps*fac)
        
# ------
# URANUS
# ------
fac = neptune['P_Edays']/uranus['P_Edays']
x_uranus = uranus['D_AU']*np.cos(ang_steps*fac)
y_uranus = uranus['D_AU']*np.sin(ang_steps*fac)
        
# -------
# NEPTUNE
# -------
fac = neptune['P_Edays']/neptune['P_Edays']
x_neptune = neptune['D_AU']*np.cos(ang_steps*fac)
y_neptune = neptune['D_AU']*np.sin(ang_steps*fac)


expander_label = 'ANIMATION: Jupiter, Saturn, Uranus, Neptune'
with st.expander(expander_label) or st.session_state.GRAPH_2:

#   Update session_state:
    st.session_state.GRAPH_2 = True
    
    fig = plt.figure()
    #fig = plt.figure(figsize=(10,10))
    ax = fig.add_axes([0.15,0.05,0.8,0.95])
    ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
    plt.axis('off')
    xy_max = 32.0
    ax.axes.set_xlim([-xy_max,xy_max])
    ax.axes.set_ylim([-xy_max,xy_max])
    #plt.plot([0,0], [-xy_max,xy_max], '--', color='Black', lw='0.5', alpha=0.5)
    #plt.plot([-xy_max,xy_max], [0,0], '--', color='Black', lw='0.5', alpha=0.5)
    #plt.plot([-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], [-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], '--', color='Black', lw='0.5', alpha=0.5)
    #plt.plot([-xy_max/np.sqrt(2.0),xy_max/np.sqrt(2.0)], [xy_max/np.sqrt(2.0),-xy_max/np.sqrt(2.0)], '--', color='Black', lw='0.5', alpha=0.5)
    plt.plot([0.0,xy_max], [0.0,0.0], '--', color='Black', lw='0.5', alpha=0.5)
        
    ab = AnnotationBbox(OffsetImage(image_sun, zoom=0.04), (x_sun, y_sun), frameon=False)
    ax.add_artist(ab)
        
    x = np.cos(ang_steps)
    y = np.sin(ang_steps)
    plt.plot(jupiter['D_AU']*x, jupiter['D_AU']*y, '-', color='Orange', lw=0.5, alpha=0.3)
    plt.plot(saturn['D_AU']*x, saturn['D_AU']*y, '-', color='Gold', lw=0.5, alpha=0.3)
    plt.plot(uranus['D_AU']*x, uranus['D_AU']*y, '-', color='Cyan', lw=0.5, alpha=0.3)
    plt.plot(neptune['D_AU']*x, neptune['D_AU']*y, '-', color='Blue', lw=0.5, alpha=0.3)
        
    point_jupiter, = plt.plot([], [], 'o', color='Orange')
    point_saturn, = plt.plot([], [], 'o', color='Gold')
    point_uranus, = plt.plot([], [], 'o', color='Cyan')
    point_neptune, = plt.plot([], [], 'o', color='Blue')
    label = ax.text(-0.15, 0.90, 'initialise', transform=ax.transAxes, fontsize='13',
                        bbox=dict(facecolor='none', edgecolor='black', pad=10.0))

    label_jupiter = ax.annotate('Jupiter', xy=(0,0), xytext=(1.0,0.0), color='Orange', fontsize='8')
    label_saturn = ax.annotate('Saturn', xy=(0,0), xytext=(1.0,0.0), color='Gold', fontsize='8')
    label_uranus = ax.annotate('Uranus', xy=(0,0), xytext=(1.0,0.0), color='Cyan', fontsize='8')
    label_neptune = ax.annotate('Neptune', xy=(0,0), xytext=(1.0,0.0), color='Blue', fontsize='8')
        
    def animate_inner_planets(i_ang):
        point_jupiter.set_data(x_jupiter[i_ang], y_jupiter[i_ang])
        point_saturn.set_data(x_saturn[i_ang], y_saturn[i_ang])
        point_uranus.set_data(x_uranus[i_ang], y_uranus[i_ang])
        point_neptune.set_data(x_neptune[i_ang], y_neptune[i_ang])
        label.set_text('Earth days: '+str(round(Edays_steps[i_ang],1)))
        label_jupiter.set_position((x_jupiter[i_ang]+0.15, y_jupiter[i_ang]+1.0))
        label_saturn.set_position((x_saturn[i_ang]+0.15, y_saturn[i_ang]+1.0))
        label_uranus.set_position((x_uranus[i_ang]+0.15, y_uranus[i_ang]+1.0))
        label_neptune.set_position((x_neptune[i_ang]+0.15, y_neptune[i_ang]+1.0))
        return point_earth, label, label_earth,
    
    #orbits_animation = animation.FuncAnimation(fig, animate_planets, interval=100, blit=True)
    orbits_animation = animation.FuncAnimation(fig, animate_inner_planets, index_ang, interval=100, blit=True)
    components.html(orbits_animation.to_jshtml(), height=600)

ChangeWidgetFontSize(expander_label, wch_font_size='25px')


# =========
# QUESTIONS
# =========
label_expander = 'QUESTIONS'
with st.expander(label_expander):

    st.write('')
    st.markdown('**Q1**: Knowing the distance of the Earth from the Sun, what is the distance travelled by the Earth in one year?')

    if st.button('Solution to **Q1**') or st.session_state.sol_Q1:
        st.session_state.sol_Q1 = True
        st.markdown('Because the orbit of the Earth is well approximated by a circle, the distance travelled by the Earth in one year is given by the formula of the circonference of a circle, where the radius is equal to 149.6 million km:')
        st.latex(r'2 \times \pi \times 149.6 {\rm \,million\,km}\,\,\simeq\,\,940 {\rm \,million\,km}')
    
    st.write('')
    st.markdown('**Q2**: What is the distance travelled by the Earth since you were born?')
    if st.button('Solution to **Q2**') or st.session_state.sol_Q2:
        st.session_state.sol_Q2 = True
        st.markdown('This is given by the product between the length of the orbit of the Earth and your age:')
        st.latex(r'940 {\rm \,million\,km} \times 11\,{\rm years} \,\,\simeq \,\,10.3 {\rm \,billion\,km}')

    st.write('')
    st.markdown('**Q3**: How long (in Earth years) is one year on Saturn?')
    if st.button('Solution to **Q3**') or st.session_state.sol_Q3:
        st.session_state.sol_Q3 = True
        st.markdown('The orbital period of Saturn is about 10775 Earth days. If we devide this number by the number of days corresponding to 1 Earth year, i.e. 365.3 days, than we get the answer to the question:')
        st.latex(r'\frac{10775}{365.3} \simeq 29.5 {\rm \,Earth\,years}')

    st.write('')
    st.markdown('**Q4**: What would be your age on Saturn?')
    if st.button('Solution to **Q4**') or st.session_state.sol_Q4:
        st.session_state.sol_Q4 = True
        st.markdown('You would be less than 1 year old! :laughing: In fact, your age would be equal to 11/29.5=0.37 Saturn years')
    
    #st.markdown('**Q5**: How many orbits has the Earth completed during one Saturn year?')

       
ChangeWidgetFontSize(label_expander, wch_font_size='25px')

    
    



