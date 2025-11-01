import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# cd /Users/apple/AI_ML/19streamlit.ipynb/class1
# streamlit run prc.py

st.title('I am Subho')

df = sns.load_dataset('titanic')
st.write('this is a data set')
st.write(df)
plt.figure(figsize=(5,4))
fig = sns.pairplot(df)
st.write('This is a PairPlot of this Data Frame')
st.pyplot(fig)
st.write('end')