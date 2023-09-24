import env
import dataAPI
from dataAPI import data_fetch
import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")
dectree=pickle.load(open('model.pkl','rb'))

def pred(features):
    input_data = input_data = np.column_stack(features)
    result = dectree.predict(input_data)
    if 1 in result:
        return True
    else:
        return False
    
st.title("Fake Account Checker")
html_temp = """
<div style="background-color:#025246 ;padding:10px">
<h2 style="color:white;text-align:center;">Check for Fake Twitter Accounts </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

username = st.text_input("Twitter Username","Type Here")
safe_html="""  
    <div style="background-color:#F4D03F;padding:10px >
    <h2 style="color:white;text-align:center;"> This Account is Real</h2>
    </div>
"""
danger_html="""  
    <div style="background-color:#F08080;padding:10px >
    <h2 style="color:black ;text-align:center;"> This Account is Fake</h2>
    </div>
"""

if st.button("Predict"):
    data = data_fetch(username)
    output=pred(data)
    if output:
        st.markdown(safe_html,unsafe_allow_html=True)
    else:
        st.markdown(danger_html,unsafe_allow_html=True)

# print(pred(dataAPI.data_fetch("al3649")))