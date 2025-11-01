import streamlit as st 
import pandas as pd
import numpy as np

# terminal run commend -> 
# 1.write the derictory (cd /Users/apple/AI_ML/19streamlit.ipynb/class1)
# 2. streamlit run file_name.py (streamlit run class1.py)

# title 

st.title("Hello from Streamlit")

## write symple text

st.write('this is a simple text')

# create a data fream 

df = pd.DataFrame({
    "1st col" : [1,2,3,4,5],
    "2nd col" : [6,7,8,9,0]
})

# display the data fream 
st.write('this is a data frame')
st.write(df)

# make a line.chat

st.line_chart(df)