from analise import indicadores
from captura_tratamento_dados import leitura_ordenacao_indice
import streamlit as st
import pandas as pd

# Leitura e organização dos dados
# Campeonato Italiano Série A
rodadas_italiano, tabela_italiano = leitura_ordenacao_indice('../dados/italiano/rodadas_liga.csv', 
                                                                   '../dados/italiano/tabela_liga.csv')

# Premier League
rodadas_premier, tabela_premier = leitura_ordenacao_indice('../dados/premier_league/rodadas_liga.csv', 
                                                              '../dados/premier_league/tabela_liga.csv')

# Bundesliga
rodadas_bundesliga, tabela_bundesliga = leitura_ordenacao_indice('../dados/bundesliga/rodadas_liga.csv', 
                                                              '../dados/bundesliga/tabela_liga.csv')

# Liga da França
rodadas_franca, tabela_franca = leitura_ordenacao_indice('../dados/franca/rodadas_liga.csv', 
                                                              '../dados/franca/tabela_liga.csv')

# La Liga
rodadas_la_liga, tabela_la_liga = leitura_ordenacao_indice('../dados/la_liga/rodadas_liga.csv', 
                                                              '../dados/la_liga/tabela_liga.csv')


def main():
    # Seleção da liga
    ligas = ['Liga Itália Série A', 'Premier League', 'Bundesliga', 'Liga da França', 'La Liga']
    liga = st.selectbox('Liga', ligas)
    if liga == 'Liga Itália Série A':
        tabela = tabela_italiano
        rodadas = rodadas_italiano
    elif liga == 'Premier League':
        tabela = tabela_premier
        rodadas = rodadas_premier
    elif liga == 'Bundesliga':
        tabela = tabela_bundesliga
        rodadas = rodadas_bundesliga
    elif liga == 'Liga da França':
        tabela = tabela_franca
        rodadas = rodadas_franca
    elif liga == 'La Liga':
        tabela = tabela_la_liga
        rodadas = rodadas_la_liga

    numero_jogos = range(2, tabela['jogos'].max())
    
    # Seleção do número de jogos
    ultimos_jogos = st.selectbox('Últimos Jogos', numero_jogos)

       # Selção do indicador
    descricao_indicadores_disponiveis = ['Gols', 'Escanteios', 'Controle de Jogo', 'Ofensividade']
    selecione_indicador = st.selectbox('Indicador', descricao_indicadores_disponiveis)

    # Seleção das equipes   
    col_1, col_2 = st.beta_columns(2)
    with col_1:
        # Seleção da equipe 1
        equipe_1 = st.selectbox('Equipe 1', tabela['equipe'])
        st.image(rodadas.query('clube == @equipe_1')['escudo'].iloc[-1])
        # Seleção do local do jogo da equipe 1
        local_equipe_1 = st.selectbox('Local Equipe 1', ['Em casa', 'Ambos'])
        # Visualização dos indicadores
        if local_equipe_1 == 'Ambos':
            # Indicador selecionado
            if selecione_indicador == 'Gols':
                indicadores(rodadas.query('clube == @equipe_1'), ultimos_jogos).indicador_gols()
            elif selecione_indicador == 'Escanteios':
                indicadores(rodadas.query('clube == @equipe_1'), ultimos_jogos).indicador_escanteios()
            elif selecione_indicador == 'Controle de Jogo':
                indicadores(rodadas.query('clube == @equipe_1'), ultimos_jogos).indicador_controle_jogo()
            elif selecione_indicador == 'Ofensividade':
                indicadores(rodadas.query('clube == @equipe_1'), ultimos_jogos).indicador_ofensividade()
            st.dataframe(rodadas.query('clube == @equipe_1').iloc[:ultimos_jogos, :-1])
        elif local_equipe_1 != 'Ambos':
            # Indicador selecionado
            if selecione_indicador == 'Gols':
                indicadores(rodadas.query('clube == @equipe_1 and local == @local_equipe_1'), ultimos_jogos).indicador_gols()
            elif selecione_indicador == 'Escanteios':
                indicadores(rodadas.query('clube == @equipe_1 and local == @local_equipe_1'), ultimos_jogos).indicador_escanteios()
            elif selecione_indicador == 'Controle de Jogo':
                indicadores(rodadas.query('clube == @equipe_1 and local == @local_equipe_1'), ultimos_jogos).indicador_controle_jogo()
            elif selecione_indicador == 'Ofensividade':
                indicadores(rodadas.query('clube == @equipe_1 and local == @local_equipe_1'), ultimos_jogos).indicador_ofensividade()
            st.dataframe(rodadas.query('clube == @equipe_1 and local == @local_equipe_1').iloc[:ultimos_jogos, :-1])
    
    with col_2:
        # Seleção da equipe 2
        equipe_2 = st.selectbox('Equipe 2', tabela['equipe'][1:].values)
        st.image(rodadas.query('clube == @equipe_2')['escudo'].iloc[-1])
        #Seleção do local da equipe 2
        local_equipe_2 = st.selectbox('Local Equipe 2', ['Visitante', 'Ambos'])
        # Visualização dos indicadorers
        if local_equipe_2 == 'Ambos':
            # Indicador selecionado
            if selecione_indicador == 'Gols':
                indicadores(rodadas.query('clube == @equipe_2'), ultimos_jogos).indicador_gols
            elif selecione_indicador == 'Escanteios':
                indicadores(rodadas.query('clube == @equipe_2'), ultimos_jogos).indicador_escanteios()
            elif selecione_indicador == 'Controle de Jogo':
                indicadores(rodadas.query('clube == @equipe_2'), ultimos_jogos).indicador_controle_jogo()
            elif selecione_indicador == 'Ofensividade':
                indicadores(rodadas.query('clube == @equipe_2'), ultimos_jogos).indicador_ofensividade()
            st.dataframe(rodadas.query('clube == @equipe_2').iloc[:ultimos_jogos, :-1])
        elif local_equipe_2 != 'Ambos':
            # Indicador selecionado
            if selecione_indicador == 'Gols':
                indicadores(rodadas.query('clube == @equipe_2 and local == @local_equipe_2'), ultimos_jogos).indicador_gols()
            elif selecione_indicador == 'Escanteios':
                indicadores(rodadas.query('clube == @equipe_2 and local == @local_equipe_2'), ultimos_jogos).indicador_escanteios()
            elif selecione_indicador == 'Controle de Jogo':
                indicadores(rodadas.query('clube == @equipe_2 and local == @local_equipe_2'), ultimos_jogos).indicador_controle_jogo()
            elif selecione_indicador == 'Ofensividade':
                indicadores(rodadas.query('clube == @equipe_2 and local == @local_equipe_2'), ultimos_jogos).indicador_ofensividade()
            st.dataframe(rodadas.query('clube == @equipe_2 and local == @local_equipe_2').iloc[:ultimos_jogos, :-1])

    st.dataframe(tabela)

if __name__ == '__main__':
    main()
