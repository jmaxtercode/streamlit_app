import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World!")
with st.sidebar:
    st.header("About App")
    st.write("This is my application.")

st.header('This is a header with a divider', divider='rainbow')
st.markdown("This is created with st.markdown")



st.subheader("st.column")
col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose an x value", 1, 10, )

with col2:
    st.write("The double value of :blue[***x***]**2 is", x**2)

st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
