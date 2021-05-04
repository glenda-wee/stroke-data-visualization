import streamlit as st
import pandas as pd 

header = st.beta_container()
dataset = st.beta_container() 
features = st.beta_container() 
others = st.beta_container() 

with header: 
    st.title("Stroke Visualization")
    st.text("Found this dataset on Kaggle, wanted to give Streamlit a try with this!")

with dataset: 
    st.title("The Dataset")
    st.text("This is how the dataset looks like:")

    stroke_data = pd.read_csv("healthcare-dataset-stroke-data.csv")
    st.write(stroke_data.head())


