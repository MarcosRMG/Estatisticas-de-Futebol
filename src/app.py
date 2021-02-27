import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from funcoes import *

url_rodadas_liga_21_italia_inter_milao = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A'
url_rodadas_liga_21_italia_genoa = 'https://fbref.com/pt/equipes/658bf2de/2020-2021/partidas/s10730/schedule/Genoa-Resultados-e-Calendarios-Serie-A'


def main():
    rodadas_21_inter_milao_liga = trata_tabela_rodadas_liga(url_rodadas_liga_21_italia_inter_milao)
    rodadas_21_genoa_liga = trata_tabela_rodadas_liga(url_rodadas_liga_21_italia_genoa)

    #rodadas_21_inter_milao_liga = ler_dados('./dados/rodadas_inter_milao_liga.csv')
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
