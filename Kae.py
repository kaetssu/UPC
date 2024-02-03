import streamlit as st 

import pandas as pd 

import numpy as np 

st.title('Titulo') 

PETER MONTALVO GARCIA7:43 PM
main.py

PETER MONTALVO GARCIA7:47 PM
n = st.slider("n", 5,100, step=1)

chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])

st.line_chart(chart_data)

PETER MONTALVO GARCIA7:49 PM
import streamlit as st 

import pandas as pd 

import numpy as np



st.title('UPC Data Science 2024')

st.header('Simulador Ventas')

n = st.slider("cant. ventas", 5,100, step=1)

chart_data = pd.DataFrame(np.random.randn(n),columns=['ventas'])

st.line_chart(chart_data)
