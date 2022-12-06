import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title('My First App')

sel1 = st.selectbox('Selection', [1,2,3])

st.write('Deine Auswahl ist:', sel1)



x = np.linspace(0, 50, 50)
fig, ax = plt.subplot()

fig = ax.subplot(x, x**2)

st.pyplot(fig)
