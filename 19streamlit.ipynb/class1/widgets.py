
# derictory -> (cd /Users/apple/AI_ML/19streamlit.ipynb/class1)

import streamlit as st

# input a name 

name = st.text_input("enter your name")
if name:
    st.write(f"hello ,{name}")
    
# making a slider
age = st.slider("enter your age",0,100,18)
st.write(f"your age is {age}")

# making a select box
option  = ['python','java','c++']
lan = st.selectbox("chose your language",option)

if lan == 'python':
    st.write("you are cool")

elif lan == "java":
    st.write('you are sexy')

else:
    st.write('you are hot')
