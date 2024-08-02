import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from utils import process_file

st.set_page_config(layout='wide')

def main():
    st.title('Análise de Dados com Pandas Profiling')

    df = process_file()

    if df is not None:
        #exibir estatísticas básicas e pré-visualização dos dados lado a lado
        st.subheader('Visão Geral dos Dados')

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('**Número de linhas e colunas:**', df.shape)

        with col2:
            st.write('**Tipos de dados das colunas:**')
            st.write(df.dtypes)

        with col3:
            st.write('**Primeiras linhas do DataFrame:**')
            st.write(df.head())

        st.title('Relatório Ydata Profiling')
        profile = ProfileReport(df, minimal=True)
        st_profile_report(profile)
        
        #opção para baixar o relatório como HTML
        st.subheader('Baixar Relatório')
        html = profile.to_html()
        st.download_button(label="Baixar Relatório como HTML", data=html, file_name="relatorio_analise.html", mime="text/html")
        
    else:
        st.warning("Nenhum arquivo carregado. Por favor, faça o upload de um arquivo CSV.")

if __name__ == "__main__":
    main()
