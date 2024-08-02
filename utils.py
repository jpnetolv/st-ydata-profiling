import pandas as pd
import streamlit as st

def process_file():
    upl = st.file_uploader('Suba seu Arquivo CSV')
    
    if upl is not None:
        df = pd.read_csv(upl)
        return df
    else:
        return None