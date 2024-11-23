import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

st.title('Streamlit App')
st.header('st.write')

st.write('This is a simple Streamlit app that demonstrates the use of `st.write`.')

st.write('Here is a random number:', np.random.randint(0, 100))

df = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.write(df)

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.markdown('-*-')
st.subheader('st.write with Markdown')
st.caption('st.write can also render Markdown')
st.text('This is a simple Streamlit app that demonstrates the use of `st.write`.')
st.latex('f(x) = x^2')
st.code('print("Hello, World!")', language='python')