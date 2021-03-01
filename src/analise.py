import pandas as pd
import streamlit as st

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
