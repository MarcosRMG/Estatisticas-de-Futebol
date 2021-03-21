from analise import Indicadores
from captura_tratamento_dados import leitura_ordenacao_indice
from atualiza_dados import atualizacao_dados
import streamlit as st
import pandas as pd


# Leitura e organização dos dados
# Campeonato Italiano Série A
rodadas_italiano, tabela_italiano = leitura_ordenacao_indice('./dados/italiano/rodadas_liga.csv', 
                                                                   './dados/italiano/tabela_liga.csv')

# Premier League
rodadas_premier, tabela_premier = leitura_ordenacao_indice('./dados/premier_league/rodadas_liga.csv', 
                                                              './dados/premier_league/tabela_liga.csv')

# Bundesliga
rodadas_bundesliga, tabela_bundesliga = leitura_ordenacao_indice('./dados/bundesliga/rodadas_liga.csv', 
                                                              './dados/bundesliga/tabela_liga.csv')

# Liga da França
rodadas_franca, tabela_franca = leitura_ordenacao_indice('./dados/franca/rodadas_liga.csv', 
                                                              './dados/franca/tabela_liga.csv')

# La Liga
rodadas_la_liga, tabela_la_liga = leitura_ordenacao_indice('./dados/la_liga/rodadas_liga.csv', 
                                                              './dados/la_liga/tabela_liga.csv')


def main():
    # Seleção da liga
    st.title('Estatísticas de Clubes de Futebol 20-21')
    ligas = ['Liga Itália Série A', 'Premier League', 'Bundesliga', 'Liga da França', 'La Liga']
    liga = st.sidebar.selectbox('Liga', ligas)
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

    # Seleção do número de jogos
    ultimos_jogos = st.sidebar.selectbox('Últimos Jogos', [tabela['Nº Jogos'].max(), 5])

    # Selção do indicador
    descricao_indicadores_disponiveis = ['Resultados', 'Gols', 'Escanteios', 'Cartões', 'Controle de Jogo', 'Ataque', 'Defesa']
    selecione_indicador = st.sidebar.selectbox('Indicador', descricao_indicadores_disponiveis)

    # Seleção das equipes   
    col_1, col_2 = st.beta_columns(2)
    with col_1:
        # Seleção da equipe 1
        equipe_1 = st.selectbox('Equipe 1', tabela['Equipe'])
        st.image(rodadas.query('clube == @equipe_1')['escudo'].iloc[0])
        # Seleção do local do jogo da equipe 1
        local_equipe_1 = st.selectbox('Local equipe 1', ['Em casa', 'Ambos'])
        # Visualização dos indicadores
        if local_equipe_1 == 'Ambos':
            indicador_local_ambos_1 = Indicadores(dados=rodadas, clube=equipe_1, local_jogo=['Em casa', 'Visitante'],
                                                        ultimos_jogos=ultimos_jogos)
           # Indicador selecionado
            if selecione_indicador == 'Resultados':
                indicador_local_ambos_1.indicador_resultados()
                st.markdown('**RODADAS**')
                Indicadores(dados=rodadas, clube=equipe_1).rodadas_mandante_e_visitante()
            elif selecione_indicador == 'Gols':
                indicador_local_ambos_1.indicador_gols()
            elif selecione_indicador == 'Escanteios':
                indicador_local_ambos_1.indicador_escanteios()
                Indicadores(dados=rodadas, clube=equipe_1, 
                            ultimos_jogos=ultimos_jogos).indicador_escanteios_partidas_mandante_e_visitante()
            elif selecione_indicador == 'Controle de Jogo':
                indicador_local_ambos_1.indicador_controle_jogo()
            elif selecione_indicador == 'Ataque':
                indicador_local_ambos_1.indicador_ofensividade()
            elif selecione_indicador == 'Cartões':
                indicador_local_ambos_1.indicador_cartoes()
            elif selecione_indicador == 'Defesa':
                indicador_local_ambos_1.indicador_defesa()
        elif local_equipe_1 != 'Ambos':
            indicador_local_unico_1 = Indicadores(dados=rodadas, clube=equipe_1, local_jogo=local_equipe_1,
                                                    ultimos_jogos=ultimos_jogos)
            # Indicador selecionado
            if selecione_indicador == 'Resultados':
                indicador_local_unico_1.indicador_resultados()
                st.markdown('**RODADAS**')
                Indicadores(dados=rodadas, clube=equipe_1, local_jogo=local_equipe_1).rodadas_mandante_ou_visitante()
            elif selecione_indicador == 'Gols':
                indicador_local_unico_1.indicador_gols()
            elif selecione_indicador == 'Escanteios':
                indicador_local_unico_1.indicador_escanteios()
                Indicadores(dados=rodadas, clube=equipe_1, local_jogo=local_equipe_1, 
                            ultimos_jogos=ultimos_jogos).indicador_escanteios_partidas_mandante_ou_visitante()
            elif selecione_indicador == 'Controle de Jogo':
                indicador_local_unico_1.indicador_controle_jogo()
            elif selecione_indicador == 'Ataque':
                indicador_local_unico_1.indicador_ofensividade()
            elif selecione_indicador == 'Cartões':
                indicador_local_unico_1.indicador_cartoes()
            elif selecione_indicador == 'Defesa':
                indicador_local_unico_1.indicador_defesa()
    
    with col_2:
        # Seleção da equipe 2
        equipe_2 = st.selectbox('Equipe 2', tabela['Equipe'].sort_index(ascending=False).values)
        st.image(rodadas.query('clube == @equipe_2')['escudo'].iloc[0])
        #Seleção do local da equipe 2
        local_equipe_2 = st.selectbox('Local equipe 2', ['Visitante', 'Ambos'])
        # Visualização dos indicadorers
        if local_equipe_2 == 'Ambos':
            indicador_local_ambos_2 = Indicadores(dados=rodadas, clube=equipe_2, local_jogo=['Em casa', 'Visitante'],
                                                    ultimos_jogos=ultimos_jogos)
            # Indicador selecionado
            if selecione_indicador == 'Resultados':
                indicador_local_ambos_2.indicador_resultados()
                st.markdown('**RODADAS**')
                Indicadores(dados=rodadas, clube=equipe_2).rodadas_mandante_e_visitante()
            elif selecione_indicador == 'Gols':
                indicador_local_ambos_2.indicador_gols()
            elif selecione_indicador == 'Escanteios':
                indicador_local_ambos_2.indicador_escanteios()
                Indicadores(dados=rodadas, clube=equipe_2, 
                            ultimos_jogos=ultimos_jogos).indicador_escanteios_partidas_mandante_e_visitante()
            elif selecione_indicador == 'Controle de Jogo':
                indicador_local_ambos_2.indicador_controle_jogo()
            elif selecione_indicador == 'Ataque':
                indicador_local_ambos_2.indicador_ofensividade()
            elif selecione_indicador == 'Cartões':
                indicador_local_ambos_2.indicador_cartoes()
            elif selecione_indicador == 'Defesa':
                indicador_local_ambos_2.indicador_defesa()
        elif local_equipe_2 != 'Ambos':
            indicador_local_unico_2 = Indicadores(dados=rodadas, clube=equipe_2, local_jogo=local_equipe_2,
                                                    ultimos_jogos=ultimos_jogos)
            # Indicador selecionado
            if selecione_indicador == 'Resultados':
                indicador_local_unico_2.indicador_resultados()
                st.markdown('**RODADAS**')
                Indicadores(dados=rodadas, clube=equipe_2, local_jogo=local_equipe_2).rodadas_mandante_ou_visitante()
            elif selecione_indicador == 'Gols':
                indicador_local_unico_2.indicador_gols()
            elif selecione_indicador == 'Escanteios':
                indicador_local_unico_2.indicador_escanteios()
                Indicadores(dados=rodadas, clube=equipe_2, local_jogo=local_equipe_2, 
                            ultimos_jogos=ultimos_jogos).indicador_escanteios_partidas_mandante_ou_visitante()
            elif selecione_indicador == 'Controle de Jogo':
                indicador_local_unico_2.indicador_controle_jogo()
            elif selecione_indicador == 'Ataque':
                indicador_local_unico_2.indicador_ofensividade()
            elif selecione_indicador == 'Cartões':
                indicador_local_unico_2.indicador_cartoes()
            elif selecione_indicador == 'Defesa':
                indicador_local_unico_2.indicador_defesa()
    if selecione_indicador == 'Resultados':
        st.markdown('**CONFRONTO DIRETO**')
        st.dataframe(rodadas.query('clube == @equipe_1 and oponente == @equipe_2')[['clube', 'resultado', 'gols_marcados', 
                                                                                            'gols_sofridos', 'oponente', 'posse',
                                                                                            'escanteios']].iloc[:, :-1])
        st.markdown('**TABELA DA LIGA**')
        st.dataframe(tabela)
    st.markdown('[GitHub](https://github.com/MarcosRMG/Estatisticas-de-Futebol)')
    st.markdown('Fonte de dados: [FBREF](https://fbref.com/pt/)')


if __name__ == '__main__':
    main()
