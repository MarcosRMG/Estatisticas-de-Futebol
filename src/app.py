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

ligas = {'Liga Itália Série A': [rodadas_italiano,
                                tabela_italiano],
        'Premier League': [rodadas_premier,
                           tabela_premier]}

def main():
    st.selectbox('Liga', ligas.keys())
    numero_jogos = range(2, tabela_liga_italia_21['jogos'].max())
    
    ultimos_jogos = st.selectbox('Últimos Jogos', numero_jogos)
    col_1, col_2 = st.beta_columns(2)

    with col_1:
        # Filtros
        equipe_1 = st.selectbox('Equipe 1', tabela_liga_italia_21['equipe'].values)
        local_equipe_1 = st.selectbox('Local Equipe 1', ['Ambos', 'Em casa', 'Visitante'])
        # Visualizações
        if local_equipe_1 == 'Ambos':
            st.image(rodadas_liga_italia_21.query('clube == @equipe_1')['escudo'].iloc[-1])
            indicadores(rodadas_liga_italia_21.query('clube == @equipe_1'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas_liga_italia_21.query('clube == @equipe_1').iloc[:ultimos_jogos, :-1])
        elif local_equipe_1 != 'Ambos':
            st.image(rodadas_liga_italia_21.query('clube == @equipe_1')['escudo'].iloc[-1])
            indicadores(rodadas_liga_italia_21.query('clube == @equipe_1 and local == @local_equipe_1'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas_liga_italia_21.query('clube == @equipe_1 and local == @local_equipe_1').iloc[:ultimos_jogos, :-1])
    with col_2:
        # Filtros
        equipe_2 = st.selectbox('Equipe 2', tabela_liga_italia_21['equipe'][1:].values)
        local_equipe_2 = st.selectbox('Local Equipe 2', ['Ambos', 'Em casa', 'Visitante'])
        # Visualizações
        if local_equipe_2 == 'Ambos':
            st.image(rodadas_liga_italia_21.query('clube == @equipe_2')['escudo'].iloc[-1])
            indicadores(rodadas_liga_italia_21.query('clube == @equipe_2'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas_liga_italia_21.query('clube == @equipe_2').iloc[:ultimos_jogos, :-1])
        elif local_equipe_2 != 'Ambos':
            st.image(rodadas_liga_italia_21.query('clube == @equipe_2')['escudo'].iloc[-1])
            indicadores(rodadas_liga_italia_21.query('clube == @equipe_2 and local == @local_equipe_2'), ultimos_jogos=ultimos_jogos)
            st.dataframe(rodadas_liga_italia_21.query('clube == @equipe_2 and local == @local_equipe_2').iloc[:ultimos_jogos, :-1])

    st.dataframe(tabela_liga_italia_21)

if __name__ == '__main__':
    main()
