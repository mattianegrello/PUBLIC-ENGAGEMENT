

#import astropy
#import matplotlib
#import scipy

#print(astropy.__version__)
#print(matplotlib.__version__)
#print(scipy.__version__)



# --------
# Packages
# --------
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
from matplotlib.ticker import AutoMinorLocator
import matplotlib.ticker as ticker
from astropy.io import ascii
import time



#def ChangeWidgetFontSize(wgt_txt, wch_font_size = '12px'):
#    htmlstr = """<script>var elements = window.parent.document.querySelectorAll('*'), i;
#                    for (i = 0; i < elements.length; ++i) { if (elements[i].innerText == |wgt_txt|) 
#                        { elements[i].style.fontSize='""" + wch_font_size + """';} } </script>  """
#
#    htmlstr = htmlstr.replace('|wgt_txt|', "'" + wgt_txt + "'")
#    components.html(f"{htmlstr}", height=0, width=0)

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
if 'TABLE' not in st.session_state:
    st.session_state.TABLE = False
if 'GRAPH_innerplanets' not in st.session_state:
    st.session_state.GRAPH_innerplanets = False
if 'GRAPH_outerplanets' not in st.session_state:
    st.session_state.GRAPH_outerplanets = False
if 'QUESTIONS' not in st.session_state:
    st.session_state.QUESTIONS = False
if 'solQ2' not in st.session_state:
    st.session_state.solQ2 = False
if 'answer_1' not in st.session_state:
    st.session_state.answer_1 = False
if 'answer_2' not in st.session_state:
    st.session_state.answer_2 = False

# -------------------------
# Set-up page configuration
# -------------------------
#st.set_page_config(layout='centered') 
st.set_page_config(layout='wide')   

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
image_ceres = plt.imread('images/ceres_lowres.png')

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


# ----------------------------
# Info about the dwarf planets
# ----------------------------
ceres = {'P_Edays':1680.0, 'D_km':0.0*10.0**6.0}


# ------------------
# Kepler's third law 
# ------------------
M_sun = 1.989*10.0**30.0  # kg
G_grav = 6.6743*10.0**(-11.0)  # m^3 kg^-1 s^-2
G_grav = G_grav * 10.0**(-9.0) * (1.15741*10.0**(-5.0))**(-2.0)             # km^3 kg^-1 day^-2
D_bkm = 10.0**np.linspace(-3.0,3.0,100)   # bilion km
P_Edays = np.sqrt(4.0*np.pi**2.0/G_grav/M_sun*(D_bkm*10.0**9.0)**3.0)  #
kepler = {'D_km': D_bkm*10.0**9.0, 'P_Edays': P_Edays}
x_kepler = kepler['D_km']
y_kepler = kepler['P_Edays']
# Initialise so it does not show in the plots
kepler['D_km'] = - kepler['D_km']
kepler['P_Edays'] = - kepler['P_Edays']









# ========================================
# Create a sidebar where to input the data
# ========================================
#
with st.sidebar:

    #st.markdown('**INSTRUCTIONS**: insert in the boxes below the measured value of the orbital period of the planets in units of Earth days.')
    #st.write('')
    
    col1_width = 1
    col2_width = 1.5
    
    col1, col2 = st.columns((col1_width,col2_width))
    col1.subheader('Planet')
    col2.subheader('Orbital period (in Earth days)')
    col1.write(' ')
    col2.write(' ')
    
#   Mercury
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('MERCURY')
    col1.image(image_mercury, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #P_mercury = col2.number_input('$P_{Mercury}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    mercury['P_Edays'] = col2.number_input('$P_{Mercury}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=mercury['P_Edays'])

    st.write('')
    
#   Venus
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('VENUS')
    col1.image(image_venus, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #P_venus = col2.number_input('$P_{Venus}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    venus['P_Edays'] = col2.number_input('$P_{Venus}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=venus['P_Edays'])

    st.write('')
    
#   Earth
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('EARTH')
    col1.image(image_earth, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #P_earth = col2.number_input('$P_{Earth}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=earth['P_Edays'])
    earth['P_Edays'] = col2.number_input('$P_{Earth}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=earth['P_Edays'])

    st.write('')
    
#   Mars
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('MARS')
    col1.image(image_mars, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #P_mars = col2.number_input('$P_{Mars}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    mars['P_Edays'] = col2.number_input('$P_{Mars}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=mars['P_Edays'])

    st.write('')
    
#   Jupiter
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('JUPITER')
    col1.image(image_jupiter, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #P_jupiter = col2.number_input('$P_{Jupiter}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    jupiter['P_Edays'] = col2.number_input('$P_{Jupiter}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=jupiter['P_Edays'])
    
    st.write('')
    
#   Saturn
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('SATURN')
    col1.image(image_saturn, width=80)
    col2.write('')
    col2.write('')
    #P_saturn = col2.number_input('$P_{Saturn}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    saturn['P_Edays'] = col2.number_input('$P_{Saturn}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=saturn['P_Edays'])

    st.write('')
    
#   Uranus
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('URANUS')
    col1.image(image_uranus, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #P_uranus = col2.number_input('$P_{Uranus}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    uranus['P_Edays'] = col2.number_input('$P_{Uranus}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=uranus['P_Edays'])

    st.write('')
    
#   Neptune
    col1, col2 = st.columns((col1_width,col2_width))
    col1.write('NEPTUNE')
    col1.image(image_neptune, width=60)
    col2.write('')
    col2.write('')
    col2.write('')
    #P_neptune = col2.number_input('$P_{Neptune}$', format='%0.1f', step=0.1, label_visibility='collapsed')
    neptune['P_Edays'] = col2.number_input('$P_{Neptune}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=neptune['P_Edays'])

    st.divider()

#   Kepler third law
    st.subheader('Show Kepler third law?')

    opt = st.radio('tick:', ['NO', 'YES'], label_visibility='collapsed')
    if (opt == 'YES'):
        kepler['D_km'] = x_kepler
        kepler['P_Edays'] = y_kepler
    elif (opt == 'NO'):
        kepler['D_km'] = -x_kepler
        kepler['P_Edays'] = -y_kepler


    #if 'Kepler_YES' not in st.session_state:
    #    st.session_state.kepler_YES = False
    #if 'Kepler_NO' not in st.session_state:
    #    st.session_state.kepler_NO = False
    # 
    #if st.checkbox('YES') or st.session_state.kepler_YES:
    #    kepler['D_km'] = x_kepler
    #    kepler['P_Edays'] = y_kepler
    #    st.session_state.kepler_NO = False
    #if st.checkbox('NO') or st.session_state.kepler_NO:
    #    kepler['D_km'] = -x_kepler
    #    kepler['P_Edays'] = -y_kepler
    #    st.session_state.kepler_YES = False
        
        
    
#   Ceres
#    col1, col2 = st.columns((col1_width,col2_width))
#    col1.write('CERES')
#    col1.image(image_ceres, width=60)
#    col2.write('')
#    col2.write('')
#    col2.write('')
#    #P_mercury = col2.number_input('$P_{Mercury}$', format='%0.1f', step=0.1, label_visibility='collapsed')
#    ceres['P_Edays'] = col2.number_input('$P_{ceres}$', format='%0.1f', step=0.1, label_visibility='collapsed', value=ceres['P_Edays'])
    
    

    #with st.container():
    #   Ceres
    #    col1, col2 = st.columns((col1_width,col2_width))
    #    col1.write('CERES')
    #    col1.image(image_ceres, width=60)
    #    col2.write('')
    #    col2.write('')
    #    col2.write('')
        
    
mercury.update({'P_Eyears':mercury['P_Edays']/earth['P_Edays']})
venus.update({'P_Eyears':venus['P_Edays']/earth['P_Edays']})
earth.update({'P_Eyears':earth['P_Edays']/earth['P_Edays']})
mars.update({'P_Eyears':mars['P_Edays']/earth['P_Edays']})
jupiter.update({'P_Eyears':jupiter['P_Edays']/earth['P_Edays']})
saturn.update({'P_Eyears':saturn['P_Edays']/earth['P_Edays']})
uranus.update({'P_Eyears':uranus['P_Edays']/earth['P_Edays']})
neptune.update({'P_Eyears':neptune['P_Edays']/earth['P_Edays']})
kepler.update({'P_Eyears':kepler['P_Edays']/earth['P_Edays']})
    
# %%%%%%%%%%%%%%%%%%%%%%%%
# %% STARTING MAIN PAGE %%
# %%%%%%%%%%%%%%%%%%%%%%%%
st.header('The solar system: orbital period versus distance from the Sun')

st.write(' ')
st.write(' ')

st.markdown('**INSTRUCTIONS**: use the sidebar on the left to input the observed orbital period of the planets. The data will appear in the table and the graphs below as a function of the planets distance from the Sun. Once you have carefully looked at the graphs, answer the questions.')

st.write(' ')
st.write(' ')



#   =========================================
#   Table summarizing the info on the planets
#   =========================================
    
expander_label = 'TABLE: info about the planets'
with st.expander(expander_label) or st.session_state.TABLE:

#   Update session_state:
    st.session_state.TABLE = True
    
    col1, col2, col3, col4, col5, col6 = st.columns((0.5,0.8,0.8,0.8,0.6,0.6))
#
    col1.write('**Planet**')
    col2.write('**Distance from Sun** <p style="font-size:15px;">(in billion km)</p>', unsafe_allow_html=True)
#   col2.write('Distance <p style="font-size:15px; padding: -10px;">(in billion km)</p>', unsafe_allow_html=True)
    col3.write('**Distance from Sun** <p style="font-size:15px;">(in million km)</p>', unsafe_allow_html=True)
    col4.write('**Distance from Sun** <p style="font-size:15px;">(in AU)</p>', unsafe_allow_html=True)
    col5.write('**Orbital period** <p style="font-size:15px;">(in Earth days)</p>', unsafe_allow_html=True)
    col6.write('**Orbital period** <p style="font-size:15px;">(in Earth years)</p>', unsafe_allow_html=True)
#
    col1, col2, col3, col4, col5, col6 = st.columns((0.5,0.8,0.8,0.8,0.6,0.6))
#
    col1.write('**Mercury**')
    col2.write(np.round(mercury['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(mercury['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(mercury['D_AU'],3))
    col5.write(np.round(mercury['P_Edays'],1))
    col6.write(np.round(mercury['P_Eyears'],3))
#
    col1.write('**Venus**')
    col2.write(np.round(venus['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(venus['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(venus['D_AU'],3))
    col5.write(np.round(venus['P_Edays'],1))
    col6.write(np.round(venus['P_Eyears'],3))
#
    col1.write('**Earth**')
    col2.write(np.round(earth['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(earth['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(earth['D_AU'],3))
    col5.write(np.round(earth['P_Edays'],1))
    col6.write(np.round(earth['P_Eyears'],3))
#
    col1.write('**Mars**')
    col2.write(np.round(mars['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(mars['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(mars['D_AU'],3))
    col5.write(np.round(mars['P_Edays'],1))
    col6.write(np.round(mars['P_Eyears'],3))
#
    col1.write('**Jupiter**')
    col2.write(np.round(jupiter['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(jupiter['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(jupiter['D_AU'],3))
    col5.write(np.round(jupiter['P_Edays'],1))
    col6.write(np.round(jupiter['P_Eyears'],3))
#
    col1.write('**Saturn**')
    col2.write(np.round(saturn['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(saturn['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(saturn['D_AU'],3))
    col5.write(np.round(saturn['P_Edays'],1))
    col6.write(np.round(saturn['P_Eyears'],3))
#
    col1.write('**Uranus**')
    col2.write(np.round(uranus['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(uranus['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(uranus['D_AU'],3))
    col5.write(np.round(uranus['P_Edays'],1))
    col6.write(np.round(uranus['P_Eyears'],3))
#
    col1.write('**Neptune**')
    col2.write(np.round(neptune['D_km']/10.0**9.0,3), format='%0.001f')
    col3.write(np.round(neptune['D_km']/10.0**6.0,1), format='%0.001f')
    col4.write(np.round(neptune['D_AU'],3))
    col5.write(np.round(neptune['P_Edays'],1))
    col6.write(np.round(neptune['P_Eyears'],3))


ChangeWidgetFontSize(expander_label, wch_font_size='25px')





# =====================================================
# GRAPH of Period versus Distance for the inner planets
# =====================================================

expander_label = 'GRAPH: Mercury, Venus, Earth, Mars'
with st.expander(expander_label) or st.session_state.GRAPH_innerplanets:

#   Update session_state
    st.session_state.GRAPH_innerplanets = True
    
    fig = plt.figure()
    ax = fig.add_axes([0.15,0.15,0.8,0.95])
    ax.set_title('Mercury, Venus, Earth, Mars', fontsize=15)
    ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
    ax.axes.set_xlim([0.0,250.0])
    ax.axes.set_ylim([0.0,750.0])
    #plt.xscale('log')
    #plt.yscale('log')
    plt.xlabel('Distance from the Sun (in million km)', size='15')
    plt.ylabel('Orbital period (in Earth days)', size='15')
    
    plt.grid(which='minor', ls=':', lw=0.5)
    plt.grid(which='major', lw=0.5)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(25))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
    
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))
    
    #plt.xticks([0.01, 0.1, 1.0, 10.0],
    #           [r'$0.01$', r'$0.1$', r'$1$', r'$10$'], size='14')
    
    #plt.yticks([100.0, 1000.0, 10000.0, 100000.0],
    #           [r'$100$', r'$1000$', r'$10\,000$', r'$100\,000$'], size='14')
    
    # Mercury
    x = mercury['D_km']/10.0**6.0
    y = mercury['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_mercury = AnnotationBbox(OffsetImage(image_mercury, zoom=0.025), (x,y), frameon=False)
    ax.add_artist(point_mercury)
    
    # Venus
    x = venus['D_km']/10.0**6.0
    y = venus['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_venus = AnnotationBbox(OffsetImage(image_venus, zoom=0.02), (x,y), frameon=False)
    ax.add_artist(point_venus)
    
    # Earth
    x = earth['D_km']/10.0**6.0
    y = earth['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_earth = AnnotationBbox(OffsetImage(image_earth, zoom=0.02), (x,y), frameon=False)
    ax.add_artist(point_earth)

    # Mars
    x = mars['D_km']/10.0**6.0
    y = mars['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_mars = AnnotationBbox(OffsetImage(image_mars, zoom=0.025), (x,y), frameon=False)
    ax.add_artist(point_mars)

#   ----------------------
#   Add kepler's third law
#   ----------------------
    plt.plot(kepler['D_km']/10.0**6.0, kepler['P_Edays'], '-', color='Red', lw='0.5', alpha=0.5)
    
    st.pyplot(fig)

ChangeWidgetFontSize(expander_label, wch_font_size='25px')





# =====================================================
# GRAPH of Period versus Distance for the outer planets
# =====================================================

label_expander = 'GRAPH: Jupiter, Saturn, Uranus, Neptune'
with st.expander(label_expander) or st.session_state.GRAPH_outerplanets:

#   Update session_state    
    st.session_state.GRAPH_outerplanets = True
    
    st.markdown('Notice that the distance is now shown in units of **billion km** and the orbital period in shown as multiples of **Earth year**. This is to avoid the use of excessively large numbers in the axes.')
    st.write('')
    
    fig = plt.figure()
    ax = fig.add_axes([0.15,0.15,0.8,0.95])
    ax.set_title('Jupiter, Saturn, Uranus, Neptune', fontsize=15)
    ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
    ax.axes.set_xlim([0.5, 5.0])
    ax.axes.set_ylim([5.0,200.0])
    #plt.xscale('log')
    #plt.yscale('log')
    plt.xlabel('Distance from the Sun (in billion km)', size='15')
    plt.ylabel('Orbital period (in Earth years)', size='15')
    
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(25))
    
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
    
    plt.grid(which='minor', ls=':', lw=0.5)
    plt.grid(which='major', lw=0.5)
    
    #plt.xticks([0.01, 0.1, 1.0, 10.0],
    #           [r'$0.01$', r'$0.1$', r'$1$', r'$10$'], size='14')
    
    #plt.yticks([100.0, 1000.0, 10000.0, 100000.0],
    #           [r'$100$', r'$1000$', r'$10\,000$', r'$100\,000$'], size='14')
    
    # Jupiter
    x = jupiter['D_km']/10.0**9.0
    y = jupiter['P_Eyears']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_jupiter = AnnotationBbox(OffsetImage(image_jupiter, zoom=0.020), (x,y), frameon=False)
    ax.add_artist(point_jupiter)
    
    # Saturn
    x = saturn['D_km']/10.0**9.0
    y = saturn['P_Eyears']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_saturn = AnnotationBbox(OffsetImage(image_saturn, zoom=0.04), (x,y), frameon=False)
    ax.add_artist(point_saturn)
    
    # Uranus
    x = uranus['D_km']/10.0**9.0
    y = uranus['P_Eyears']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_uranus = AnnotationBbox(OffsetImage(image_uranus, zoom=0.03), (x,y), frameon=False)
    ax.add_artist(point_uranus)
    
    # Neptune
    x = neptune['D_km']/10.0**9.0
    y = neptune['P_Eyears']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_neptune = AnnotationBbox(OffsetImage(image_neptune, zoom=0.018), (x,y), frameon=False)
    ax.add_artist(point_neptune)

#   ----------------------
#   Add kepler's third law
#   ----------------------
    plt.plot(kepler['D_km']/10.0**9.0, kepler['P_Eyears'], '-', color='Red', lw='0.5', alpha=0.5)
    
    st.pyplot(fig)
    
ChangeWidgetFontSize(label_expander, wch_font_size='25px')





# =========
# QUESTIONS
# =========
label_expander = 'QUESTIONS'
with st.expander(label_expander) or st.session_state.QUESTIONS:

#   Update session_state    
    st.session_state.QUESTIONS = True



# ==========
# QUESTION 1
# ==========
label_expander = 'QUESTION 1'
with st.expander(label_expander):
    
    st.markdown('By looking at the two graphs, what can you say about how the orbital period of a planet changes with the planet distance from the Sun? Choose one of the options below:')

    answer_1 = 'There is no evident relation between the orbital period of a planet and its distance from the Sun'
    answer_2 = 'The orbital period of the planets steadly increases with the distance from the Sun'

    if st.checkbox(answer_1):
        st.markdown('**INCORRECT**')
        
    if st.checkbox(answer_2):
        st.markdown('**CORRECT**')
    
    #if st.checkbox(answer_1) or st.session_state.answer_1:
    #    st.markdown('INCORRECT')
    #    st.session_state.answer_2 = True
        
    #if st.checkbox(answer_2) or st.session_state.answer_2:
    #    st.markdown('CORRECT')
    #    st.session_state.answer_1 = True
         
       
    #opt = st.radio('tick:', [answer_1, answer_2], label_visibility='collapsed', index=0)
    #if (opt == answer_1):
    #    st.markdown('INCORRECT')
    #elif (opt == answer_2):
    #    st.markdown('CORRECT')
    

ChangeWidgetFontSize(label_expander, wch_font_size='25px')


# ==========
# QUESTION 2
# ==========
label_expander = 'QUESTION 2'
with st.expander(label_expander):
    
    st.markdown('In between Mars and Jupiter there is a dwarf planet called **Ceres**. The orbital period of Ceres is **1680 Earth days**. Looking at the graph below, which shows the Earth, Mars and Jupiter, can you guess the distance of Ceres from the Sun? Input your value below to visualise Ceres in the graph')

    ceres['D_km'] = st.number_input('Input Ceres distance from the Sun in million km:', format='%0.1f', step=0.1)
    ceres['D_km'] = ceres['D_km']*10.0**6.0

    fig = plt.figure()
    ax = fig.add_axes([0.15,0.15,0.8,0.95])
    ax.set_title('Earth, Mars, Jupiter', fontsize=15)
    ax.tick_params(axis='both', which='both', direction='in', top='on', right='on')
    ax.axes.set_xlim([00.0,1000.0])
    ax.axes.set_ylim([000.0,5000.0])
    #plt.xscale('log')
    #plt.yscale('log')
    plt.xlabel('Distance from the Sun (in million km)', size='15')
    plt.ylabel('Orbital period (in Earth days)', size='15')
    
    ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(500))
    
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(25))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(100))
    
    plt.grid(which='minor', ls=':', lw=0.5)
    plt.grid(which='major', lw=0.5)
    
    #plt.xticks([0.01, 0.1, 1.0, 10.0],
    #           [r'$0.01$', r'$0.1$', r'$1$', r'$10$'], size='14')
    
    #plt.yticks([100.0, 1000.0, 10000.0, 100000.0],
    #           [r'$100$', r'$1000$', r'$10\,000$', r'$100\,000$'], size='14')
    
    # Earth
    x = earth['D_km']/10.0**6.0
    y = earth['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_earth = AnnotationBbox(OffsetImage(image_earth, zoom=0.02), (x,y), frameon=False)
    ax.add_artist(point_earth)
    
    # Mars
    x = mars['D_km']/10.0**6.0
    y = mars['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_mars = AnnotationBbox(OffsetImage(image_mars, zoom=0.025), (x,y), frameon=False)
    ax.add_artist(point_mars)
    
    # Jupiter
    x = jupiter['D_km']/10.0**6.0
    y = jupiter['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_jupiter = AnnotationBbox(OffsetImage(image_jupiter, zoom=0.025), (x,y), frameon=False)
    ax.add_artist(point_jupiter)

    # Ceres
    x = ceres['D_km']/10.0**6.0
    y = ceres['P_Edays']
    plt.plot(x, y, 'o', color='Black', lw='0.5', alpha=0.5)
    plt.plot([x,x], [0.0001,y], '--', color='Black', lw='0.5', alpha=1.0)
    plt.plot([0.00001,x], [y,y], '--', color='Black', lw='0.5', alpha=1.0)
    point_ceres = AnnotationBbox(OffsetImage(image_ceres, zoom=0.02), (x,y), frameon=False)
    ax.add_artist(point_ceres)
    plt.text(x+25,y+50,'Ceres')

#   ----------------------
#   Add kepler's third law
#   ----------------------
    plt.plot(kepler['D_km']/10.0**6.0, kepler['P_Edays'], '-', color='Red', lw='0.5', alpha=0.5)

    st.pyplot(fig)

    st.write('')
        
    

#   --------------
#   Solution to Q2
#   --------------
    if st.button('Press here to discover the true distance of Ceres from the Sun') or st.session_state.solQ2:
        st.session_state.solQ2 = True
        
        st.markdown('The true distance of Ceres from the Sun is **414.0 million km**')
        D_ceres = 414.0
        aux = np.abs(ceres['D_km']/10.0**6.0 - D_ceres)/D_ceres
        if (aux <= 0.1):
            st.markdown(':clap: WELL DONE! your value is very close to the true value!')
        if (np.logical_and(aux <= 0.3, aux > 0.1)):
            st.markdown(':+1: NOT TOO BAD! your value is not too far from the true value!')
        if (aux > 0.3):
            st.markdown(':sweat: SORRY! your value is quite far from the true value!')

        st.write('')

        st.markdown(':point_right: :red[The relation between the orbital period of a planet and its distance from the Sun is known as **Kepler third law**]. You can visualise the kepler law in the graphs above by using the options at the bottom of the sidebar.')

ChangeWidgetFontSize(label_expander, wch_font_size='25px')


# ==========
# QUESTION 3
# ==========
label_expander = 'QUESTION 3'
with st.expander(label_expander):
    
    st.markdown('Immagine that a distant star has two planets orbiting around it, as illustrated in the picture below. **Planet 1** is located very close to the star while **Planet 2** is far away from the star. Which of the two planets is more likely to transit in front of the star while you are observing that system and why? Select the correct answer below.')

    st.image('IMAGES/Planet_1_and_Planet_2.png')
    st.write('')

    answer_1 = 'Planet 1 is more likely to be seen transiting in front of the star'
    answer_2 = 'Planet 2 is more likely to be seen transiting in front of the star'

    if st.checkbox(answer_1):
        st.markdown('**CORRECT!** In fact, Planet 1 is closer to its star and, based on Kepler third law, it has a shorter orbital period compared to Planet 2. Therefore, it transits more frequently in front of its star.')
        
    if st.checkbox(answer_2):
        st.markdown('**INCORRECT** Planet 2 is further away from the star and, based on Kepler third law, it has a longer orbital period than Planet 1. Therefore, it transits less frequently in front of its star.')

ChangeWidgetFontSize(label_expander, wch_font_size='25px')

    
    
















