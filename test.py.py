#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
st.title('Fist App')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

