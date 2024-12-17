import pandas as pd
import streamlit as st

def process_file():
    """
    Função para processar o arquivo CSV carregado pelo usuário.

    Exibe um botão de upload de arquivo no Streamlit. Quando o usuário faz o upload de um arquivo CSV, 
    o arquivo é lido utilizando o pandas e o DataFrame resultante é retornado. Se nenhum arquivo for 
    carregado, a função retorna None.

    Returns:
        pd.DataFrame or None: Retorna o DataFrame carregado a partir do arquivo CSV, ou None se nenhum arquivo 
                               for carregado.
    """
    # Exibe o botão para upload do arquivo CSV
    upl = st.file_uploader('Suba seu Arquivo CSV')
    
    if upl is not None:
        # Se um arquivo for carregado, lê o CSV e retorna o DataFrame
        df = pd.read_csv(upl)
        return df
    else:
        # Se nenhum arquivo for carregado, retorna None
        return None
