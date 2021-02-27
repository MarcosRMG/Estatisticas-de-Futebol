import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ler_dados(caminho: str):
    '''
    --> Faz a leitura do arquivo csv

    Keywords arguments
    :param caminho: Endereço do arquivo csv

    return DataFrame com as informações do arquivo csv 
    '''
    return pd.read_csv(caminho)

def histograma(dados: pd.DataFrame, coluna: str, titulo: str):
    '''
    --> Mostra o histograma da variável selecionada
    
    :param dados: DataFrame pandas com os dados
    :param coluna: Série pandas da variável específica
    :param titulo: Título do gráfico

    return Histograma 
    '''
    fig, ax = plt.subplots()
    ax = dados[coluna].plot(kind='hist')
    ax.set_title(titulo, loc='left', fontsize=24)
    return fig


def main():
    rodadas_21_inter_milao_liga = ler_dados('./dados/rodadas_inter_milao_liga.csv')
    figura = histograma(rodadas_21_inter_milao_liga, 'gols_marcados', 
                        'Distribuição de gols da Inter de Milão')
    equipe = list()
    
    st.title('Liga Italiana de Futebol 20-21')
    st.markdown(f'Rodadas da {equipe}')

    st.selectbox('Selecione a equipe', equipe)
    #st.dataframe(rodadas_21_inter_milao_liga)
    st.pyplot(figura)


if __name__ == '__main__':
    main()
