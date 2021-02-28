from funcoes import trata_tabela_rodadas_liga, indicadores, leitura_limpeza_html, escudos
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import display, HTML
from urllib.request import urlopen
from bs4 import BeautifulSoup


url_rodadas_liga_21_italia_inter_milao = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A'
url_rodadas_liga_21_italia_genoa = 'https://fbref.com/pt/equipes/658bf2de/2020-2021/partidas/s10730/schedule/Genoa-Resultados-e-Calendarios-Serie-A'
soup_liga_inter = leitura_limpeza_html(url_rodadas_liga_21_italia_inter_milao)
soup_liga_genoa = leitura_limpeza_html(url_rodadas_liga_21_italia_genoa)
logos = escudos(soup_liga_inter, soup_liga_genoa)

def main():
    rodadas_21_inter_milao_liga = trata_tabela_rodadas_liga(url_rodadas_liga_21_italia_inter_milao)
    rodadas_21_genoa_liga = trata_tabela_rodadas_liga(url_rodadas_liga_21_italia_genoa)

    
    numero_jogos = range(2, rodadas_21_inter_milao_liga.shape[0])
    ultimos_jogos = st.selectbox('Últimos Jogos', numero_jogos)
    col_1, col_2 = st.beta_columns(2)
    with col_1:
        st.image(logos[0])
        indicadores(rodadas_21_inter_milao_liga, ultimos_jogos=ultimos_jogos)
    with col_2:
        st.image(logos[1])
        indicadores(rodadas_21_genoa_liga, ultimos_jogos=ultimos_jogos)

if __name__ == '__main__':
    main()
