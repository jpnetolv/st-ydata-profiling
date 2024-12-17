Aqui está o **README.md** para o seu projeto:

```markdown
# Análise de Dados com Pandas Profiling

Este projeto utiliza o Streamlit para criar uma interface web interativa para análise de dados. Ele permite que o usuário faça o upload de um arquivo CSV, visualize informações básicas sobre o DataFrame e gere um relatório detalhado utilizando a biblioteca `ydata-profiling`. O relatório gerado pode ser baixado em formato HTML.

## Funcionalidades

- **Upload de Arquivo CSV**: O usuário pode carregar seu próprio arquivo CSV para análise.
- **Visão Geral dos Dados**: Exibe o número de linhas e colunas, tipos de dados das colunas e as primeiras linhas do DataFrame.
- **Relatório Ydata Profiling**: Gera um relatório detalhado de análise exploratória dos dados com a biblioteca `ydata-profiling`.
- **Download do Relatório**: Permite ao usuário baixar o relatório em formato HTML.

## Instalação

Para executar o projeto, você precisa ter o Python instalado em seu sistema. Além disso, é necessário instalar as dependências do projeto. Siga os passos abaixo:

1. Clone este repositório:

   ```bash
   git clone https://github.com/jpnetolv/st-ydata-profiling
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. Execute o script `st-tdt-profiling.py` com o Streamlit:

   ```bash
   streamlit run st-tdt-profiling.py
   ```

2. Na interface web do Streamlit:
   - Faça o upload de um arquivo CSV.
   - Visualize as estatísticas básicas do DataFrame.
   - Veja o relatório gerado pelo `ydata-profiling`.
   - Baixe o relatório em formato HTML.

## Dependências

- `streamlit`: Para a interface web interativa.
- `pandas`: Para manipulação e análise dos dados.
- `ydata-profiling`: Para gerar o relatório detalhado de análise exploratória.
- `streamlit_pandas_profiling`: Para integrar o `ydata-profiling` ao Streamlit.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
