
import numpy as np
import streamlit as st

lordo = st.number_input(label='Inserisci Lordo (in Euri)')
IVA = st.number_input('Inserisci IVA (%)')
netto = lordo/(1 + IVA/100.0)

st.write()
st.write('Risultato: Netto (in euri) = ', netto)
