import pandas as pd
import streamlit as st

def indicadores(dados: pd.DataFrame, ultimos_jogos=5):
    '''
    --> Mostra os indicadores na tela

    :param dados: DataFrame com o números das rodadas da liga
    :param ultimos_jogos: Seleção do número de jogos anteriores para cálculo dos indicadores
    '''
    media_gols_partida = round(dados['gols_marcados'][:ultimos_jogos].mean() + dados['gols_sofridos'][:ultimos_jogos].mean())
    desvio_padrao_gols_partida = round(dados['gols_marcados'][:ultimos_jogos].std() + dados['gols_sofridos'][:ultimos_jogos].std())
    media_gols_marcados = round(dados['gols_marcados'][:ultimos_jogos].mean())
    desvio_padrao_gols_marcados = round(dados['gols_marcados'][:ultimos_jogos].std())
    media_gols_sofridos = round(dados['gols_sofridos'][:ultimos_jogos].mean())
    desvio_padrao_gols_sofridos = round(dados['gols_sofridos'][:ultimos_jogos].std())
    media_posse_bola = round(dados['posse'][:ultimos_jogos].mean())
    desvio_padrao_posse_bola = round(dados['posse'][:ultimos_jogos].std())
    media_escanteios = round(dados['escanteios'][:ultimos_jogos].mean())
    desvio_padrao_escanteios = round(dados['escanteios'][:ultimos_jogos].std())

    st.markdown('RESULTADOS')
    st.markdown(dados['resultado'][:ultimos_jogos].values)
    st.markdown('GOLS POR PARTIDA')
    st.text('Média ' + str(int(media_gols_partida)))
    st.text('Intervalo: ' + str(int(media_gols_partida - desvio_padrao_gols_partida)) +  '-' + str(int(media_gols_partida + desvio_padrao_gols_partida)))  
    st.markdown('GOLS MARCADOS')
    st.text('Média: ' +  str(int(media_gols_marcados)))
    st.text('Intervalo: ' + str(int(media_gols_marcados - desvio_padrao_gols_marcados)) +  '-' + str(int(media_gols_marcados + desvio_padrao_gols_marcados)))  
    st.markdown('GOLS SOFRIDOS')
    st.text('Média: ' +  str(int(media_gols_sofridos)))
    st.text('Intervalo: ' + str(int(media_gols_sofridos - desvio_padrao_gols_sofridos)) +  '-' + str(int(media_gols_sofridos + desvio_padrao_gols_sofridos)))  
    st.markdown('POSSE DE BOLA')
    st.text('Média: ' +  str(int(media_posse_bola)))
    st.text('Intervalo: ' + str(int(media_posse_bola - desvio_padrao_posse_bola)) +  '-' + str(int(media_posse_bola + desvio_padrao_posse_bola)))  
    st.markdown('ESCANTEIOS')
    st.text('Média: ' +  str(int(media_escanteios)))
    st.text('Intervalo: ' + str(int(media_escanteios - desvio_padrao_escanteios)) +  '-' + str(int(media_escanteios + desvio_padrao_escanteios)))  
