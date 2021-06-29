from analise import IndicadoresFbref, IndicadoresCouk
from captura_tratamento_dados import leitura_dados_fbref
import streamlit as st
import pandas as pd


# Dados Fbref
rodadas_brasileirao, tabela_brasileirao = leitura_dados_fbref('./dados/brasileirao/fbref/rodadas_liga.csv', 
                                                            './dados/brasileirao/fbref/tabela_liga.csv')

# Dados Co.Uk
temporadas_brasileirao_couk = pd.read_csv('./dados/brasileirao/couk/temporadas_baixadas.csv')
rodadas_brasileirao_couk = pd.read_csv('./dados/brasileirao/couk/temporada_atual.csv')


def main():
    # Seleção da liga
    st.title('Estatísticas Campeonato Brasileiro')
    ligas = ['Brasileirão Série A']
    liga = st.sidebar.selectbox('Liga', ligas)
    if liga == 'Brasileirão Série A':
        tabela = tabela_brasileirao
        rodadas = rodadas_brasileirao
        rodadas_couk = rodadas_brasileirao_couk
        temporadas = temporadas_brasileirao_couk

    # Seleção do número de jogos
    ultimos_jogos = st.sidebar.selectbox('Últimos Jogos da Liga', [int(tabela['n_jogos'].max()), 5])

    # Selção do indicador
    descricao_indicadores_disponiveis = ['Resultados Liga/ Confrontos', 'Gols']
    selecione_indicador = st.sidebar.selectbox('Indicador', descricao_indicadores_disponiveis)

    # Seleção das equipes   
    time_1, time_2 = st.beta_columns(2)
    with time_1:
        # Seleção mandante
        mandante = st.selectbox('Mandante', tabela['equipe'])
        mandante_local = 'Em casa'
        st.image(rodadas.query('clube == @mandante')['escudo'].iloc[0])
        # Instanciando indicadores do clube mandante
        indicador_mandante_fbref = IndicadoresFbref(dados=rodadas, clube=mandante, local_jogo=mandante_local,
                                                    ultimos_jogos=ultimos_jogos)
        indicador_mandante_couk = IndicadoresCouk(dados=rodadas_couk, mandante=mandante, ultimos_jogos=ultimos_jogos)
    with time_2:
        # Seleção visitante
        visitante = st.selectbox('Visitante', tabela['equipe'].sort_index(ascending=False).values)
        visitante_local = 'Visitante'
        st.image(rodadas.query('clube == @visitante')['escudo'].iloc[0])
        # Instanciando indicadores do clube visitante
        indicador_visitante_fbref = IndicadoresFbref(dados=rodadas, clube=visitante, local_jogo=visitante_local,
                                                    ultimos_jogos=ultimos_jogos)
        indicador_visitante_couk = IndicadoresCouk(dados=rodadas_couk, visitante=visitante, ultimos_jogos=ultimos_jogos)                                        
    # Instanciando a classe de indicadores COUK de probabilidades
    probabilidades_couk = IndicadoresCouk(dados=rodadas_couk, mandante=mandante, visitante=visitante)
    time_1_indicadores, time_2_indicadores = st.beta_columns(2)
    detalhar = st.sidebar.checkbox('Detalhado')
    # Indicadores Gerais
    if selecione_indicador == 'Gols':
        probabilidades_couk.probabilidade_gols_partida()
    # Indicadores equipe 1
    with time_1_indicadores:
        if selecione_indicador == 'Resultados Liga/ Confrontos':
            indicador_mandante_fbref.indicador_ultimos_5_resultados()
            IndicadoresCouk(temporadas, mandante, visitante).confronto_direto()
        if detalhar:
            if selecione_indicador == 'Gols':
                indicador_mandante_couk.gols_mandante()
    # Indicadores equipe 2
    with time_2_indicadores:
        if selecione_indicador == 'Resultados Liga/ Confrontos':
            indicador_visitante_fbref.indicador_ultimos_5_resultados()
            probabilidades_couk.probabilidade_resultados_liga()
        if detalhar:
            if selecione_indicador == 'Gols':
                indicador_visitante_couk.gols_visitante()
    if detalhar:
        if selecione_indicador == 'Resultados Liga/ Confrontos':    
            st.markdown('**CONFRONTOS 2012-2021**')
            confrontos_diretos = temporadas.query('mandante == @mandante and visitante == @visitante')[['data', 'mandante', 
                                                                                                        'gols_mandante_partida', 
                                                                                                        'gols_visitante_partida', 
                                                                                                        'visitante']]
            confrontos_diretos.columns = ['Data', 'Mandante', 'Gols Mandante', 'Gols Visitante', 'Visitante']                                                                                                  
            st.dataframe(confrontos_diretos)
            st.markdown('**CONFRONTOS NA LIGA ATUAL**')
            jogos_liga = rodadas.query('clube == @mandante and oponente == @visitante')[['data', 'local', 'clube', 'gols_marcados', 
                                                                                        'gols_sofridos', 'oponente']]
            jogos_liga.columns = ['Data', 'Local', 'Clube', 'Gols Marcados', 'Gols Sofridos', 'Oponente']
            st.dataframe(jogos_liga)
            st.markdown('**TABELA DA LIGA**')
            st.dataframe(tabela[['posicao', 'equipe', 'n_jogos', 'pontos', 'ultimos_5']].rename({'posicao': 'Posição', 
                                                                                                'equipe': 'Equipe', 
                                                                                                'n_jogos': 'Jogos', 
                                                                                                'pontos': 'Pontos', 
                                                                                                'ultimos_5': 'Últimos Jogos'}, 
                                                                                                axis=1))
    st.markdown('Repositório no [GitHub](https://github.com/MarcosRMG/Estatisticas-de-Futebol)')
    st.markdown('Fonte de dados: [FBREF](https://fbref.com/pt/) e [Football-Data](https://www.football-data.co.uk/)')
    st.markdown('Última atualização: 29/06/21')    


if __name__ == '__main__':
    main()
