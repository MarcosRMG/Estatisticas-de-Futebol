from analise import indicadores
from captura_tratamento_dados import leitura_ordenacao_indice
import streamlit as st
import pandas as pd


# Campeonato Italiano Série A
rodadas_italiano, tabela_italiano = leitura_ordenacao_indice('../dados/italiano/rodadas_liga.csv', 
                                                                   '../dados/italiano/tabela_liga.csv')

# Premier League
rodadas_premier, tabela_premier = leitura_ordenacao_indice('../dados/premier_league/rodadas_liga.csv', 
                                                              '../dados/premier_league/tabela_liga.csv')

ligas = ['Liga Itália Série A', 'Premier League']

def main():
    # Seleção da liga
    liga = st.selectbox('Liga', ligas)
    if liga == 'Liga Itália Série A':
        tabela = tabela_italiano
        rodadas = rodadas_italiano
    elif liga == 'Premier League':
        tabela = tabela_premier
        rodadas = rodadas_premier

    numero_jogos = range(2, tabela['jogos'].max())
    
    # Seleção do número de jogos
    ultimos_jogos = st.selectbox('Últimos Jogos', numero_jogos)
    col_1, col_2 = st.beta_columns(2)

    with col_1:
        # Seleção da equipe 1
        equipe_1 = st.selectbox('Equipe 1', tabela['equipe'])
        local_equipe_1 = st.selectbox('Local Equipe 1', ['Ambos', 'Em casa', 'Visitante'])
        # Seleção do local do jogo
        if local_equipe_1 == 'Ambos':
            st.image(rodadas.query('clube == @equipe_1')['escudo'].iloc[-1])
            indicadores(rodadas.query('clube == @equipe_1'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas.query('clube == @equipe_1').iloc[:ultimos_jogos, :-1])
        elif local_equipe_1 != 'Ambos':
            st.image(rodadas.query('clube == @equipe_1')['escudo'].iloc[-1])
            indicadores(rodadas.query('clube == @equipe_1 and local == @local_equipe_1'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas.query('clube == @equipe_1 and local == @local_equipe_1').iloc[:ultimos_jogos, :-1])
    with col_2:
        # Seleção da equipe 2
        equipe_2 = st.selectbox('Equipe 2', tabela['equipe'][1:].values)
        local_equipe_2 = st.selectbox('Local Equipe 2', ['Ambos', 'Em casa', 'Visitante'])
        # Leleção do local do jogo
        if local_equipe_2 == 'Ambos':
            st.image(rodadas.query('clube == @equipe_2')['escudo'].iloc[-1])
            indicadores(rodadas.query('clube == @equipe_2'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas.query('clube == @equipe_2').iloc[:ultimos_jogos, :-1])
        elif local_equipe_2 != 'Ambos':
            st.image(rodadas.query('clube == @equipe_2')['escudo'].iloc[-1])
            indicadores(rodadas.query('clube == @equipe_2 and local == @local_equipe_2'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas.query('clube == @equipe_2 and local == @local_equipe_2').iloc[:ultimos_jogos, :-1])

    st.dataframe(tabela)

if __name__ == '__main__':
    main()
