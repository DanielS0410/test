import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.title('My First App')

sel1 = st.selectbox('Selection', [1,2,3])

st.write('Deine Auswahl ist:', sel1)



#x = np.linspace(0, 50, 50)
#fig, ax = plt.subplots()

#ax.plot(x, x**sel1)

#st.pyplot(fig)

df = pd.read_csv('Bastar Craton.csv')

sel2 = st.selectbox('1. Selection', ['Mg','Si','Cr'])
sel3 = st.selectbox('2. Selection', ['Mg','Si','Cr'])

x = np.linspace(0, 50, 50)
fig, ax = plt.subplots()

ax.plot(df[sel2], df[sel3])

st.pyplot(fig)


