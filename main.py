import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Product": ["A", "B", "C"],
    "Sales": [100, 150, 80]
})

st.title("Business Dashboard")
st.bar_chart(df.set_index("Product"))
