import streamlit as st
from data import EDA
from data import data
page=st.sidebar.selectbox('which page',('EDA','data'))
if page=='EDA':
    EDA()
if page=='data':
    data()