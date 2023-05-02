
import numpy as np
import streamlit as st

lordo = st.number_input(label='** Lordo (in Euri) = ** ', layout = 'wide')
IVA = st.number_input('IVA (%) = ')
netto = lordo/(1 + IVA/100.0)

st.write('Netto (in euri) = ', netto)
