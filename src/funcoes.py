import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from urllib.request import urlopen
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML


colunas_2 = {
    'Data': 'data', 
    'Horário': 'horario', 
    'Rodada': 'rodada', 
    'Dia': 'dia', 
    'Local': 'local', 
    'Resultado': 'resultado', 
    'GP': 'gols_marcados', 
    'GC': 'gols_sofridos',
    'Oponente': 'oponente', 
    'xG': 'xg', 
    'xGA': 'xga', 
    'Posse': 'posse', 
    'Público': 'publico', 
    'Capitão': 'capitao', 
    'Formação': 'formacao',
    'Árbitro': 'arbitro', 
    'Relatório da Partida': 'relatorio_partida', 
    'Notas': 'notas'
}


colunas = {
    'Cl': 'posicao',
    'Equipe': 'equipe',
    'MP': 'jogos',	
    'V': 'vitorias',	
    'E': 'empates',	
    'D': 'derrotas',	
    'GP': 'gols_marcados',	
    'GC': 'gols_sofridos',	
    'GD': 'saldo_gols',	
    'Pt': 'pontos',	
    'Últimos 5': 'ultimos_5'
}


def trata_tabela_rodadas_liga(html: str, dicionario_colunas=colunas_2, indice='rodada',
                      colunas_desconsideradas=['notas', 'publico', 
                                               'relatorio_partida', 'arbitro',
                                               'capitao', 'formacao', 'xga', 'xg',
                                               'horario', 'dia', 'data']):
  '''
  --> Trata a tabela da liga para análise

  :param html: Variável que guarda o endereço html
  :param dicionario_colunas: Dicionário com a descrição da coluna padronizada
  :param indice: Indice da tabela
  :param colunas_desconsideradas: Lista de colunas que não serão analidas

  return: Nota tabela com as informações para análise
  '''
  rodadas = pd.read_html(html)[0]
  rodadas.rename(dicionario_colunas, axis=1, inplace=True)
  rodadas[indice] = rodadas[indice].str[-2:]
  rodadas[indice] = rodadas[indice].astype('int32')
  rodadas.set_index(indice, inplace=True)
  rodadas.sort_index(ascending=False, inplace=True)
  rodadas.drop(colunas_desconsideradas, axis=1, 
                              inplace=True)
  rodadas.dropna(inplace=True)
  return rodadas


def ler_dados(caminho: str):
    '''
    --> Faz a leitura do arquivo csv

    Keywords arguments
    :param caminho: Endereço do arquivo csv

    return DataFrame com as informações do arquivo csv 
    '''
    return pd.read_csv(caminho)



def indicadores(dados: pd.DataFrame, ultimos_jogos=5):
    '''
    --> Mostra os indicadores na tela

    :param dados: DataFrame com o números das rodadas da liga
    :param ultimos_jogos: Seleção do número de jogos anteriores para cálculo dos indicadores
    '''
    st.markdown('Gols marcados')
    st.text('Média:' + ' ' + str(int(dados['gols_marcados'][:ultimos_jogos].mean().round())))
    st.text('Variação +-' + ' ' + str(int(dados['gols_marcados'][:ultimos_jogos].std().round())))
    st.markdown('Gols sofridos')
    st.text('Média:' + ' ' + str(int(dados['gols_sofridos'][:ultimos_jogos].mean().round())))
    st.text('Variação +-' + ' ' + str(int(dados['gols_sofridos'][:ultimos_jogos].std().round())))
    st.markdown('Posse de bola')
    st.text('Média:' + ' ' + str(int(dados['posse'][:ultimos_jogos].mean().round())) + '%')
    st.text('Variação +-' + ' ' + str(int(dados['posse'][:ultimos_jogos].std().round())) + '%')


def leitura_limpeza_html(url):
  '''
  Retira os espaços e o /n do documento html

  :param url: Endereço url da página

  return: Documento html tratado
  '''
  response = urlopen(url)
  html = response.read().decode('UTF-8')
  html_limpo = ' '.join(html.split()).replace('> <', '><')
  html_soup = BeautifulSoup(html_limpo, 'html.parser')
  return html_soup

def escudos(soup_1, soup_2):
  '''
  --> Retorna o endereço do escudo do time

  :param soup_1: Objeto soup da página html do time mandante
  :param soup_2: Objeto soup da página html do time visitante 

  return: Endereço da logo 
  '''
  logo_time_mandante = soup_1.find('img', {'class': 'teamlogo'})
  logo_time_visitante = soup_2.find('img', {'class': 'teamlogo'})
  logos = [logo_time_mandante.get('src'), logo_time_visitante.get('src')]
  return logos
