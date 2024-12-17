# Importação das bibliotecas necessárias
import pandas as pd  # Biblioteca para manipulação e análise de dados
from ydata_profiling import ProfileReport  # Biblioteca para gerar relatórios detalhados de análise de dados
import streamlit as st  # Biblioteca para criar aplicativos interativos de dados na web
from streamlit_pandas_profiling import st_profile_report  # Integração entre Streamlit e ydata-profiling para exibir relatórios
from utils import process_file  # Função personalizada para carregar arquivos CSV

# Configuração do layout do Streamlit para exibição em larga escala
st.set_page_config(layout='wide')

def main():
    """
    Função principal que define a estrutura do aplicativo Streamlit para análise de dados com Pandas Profiling.

    Esta função exibe um título, permite o upload de um arquivo CSV, e, se um arquivo for carregado,
    exibe estatísticas básicas sobre o DataFrame, como o número de linhas e colunas, os tipos de dados das colunas,
    e as primeiras linhas do DataFrame. Além disso, gera e exibe um relatório detalhado utilizando o ydata-profiling.
    O usuário também pode baixar o relatório gerado como um arquivo HTML.

    Caso nenhum arquivo seja carregado, exibe uma mensagem de alerta para que o usuário faça o upload de um arquivo CSV.
    """
    # Define o título do aplicativo
    st.title('Análise de Dados com Pandas Profiling')

    # Chama a função process_file do utils.py para permitir o upload do arquivo
    df = process_file()

    if df is not None:
        # Se o DataFrame for carregado com sucesso, exibe informações básicas
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

        # Gera o relatório de Pandas Profiling
        st.title('Relatório Ydata Profiling')
        profile = ProfileReport(df, minimal=True)
        st_profile_report(profile)
        
        # Opção para baixar o relatório como um arquivo HTML
        st.subheader('Baixar Relatório')
        html = profile.to_html()
        st.download_button(label="Baixar Relatório como HTML", data=html, file_name="relatorio_analise.html", mime="text/html")
        
    else:
        # Exibe uma mensagem de alerta se nenhum arquivo for carregado
        st.warning("Nenhum arquivo carregado. Por favor, faça o upload de um arquivo CSV.")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
