from analise import IndicadoresFbref, IndicadoresCouk
from captura_tratamento_dados import leitura_ordenacao_indice_fbref
from atualiza_dados import atualizacao_dados
import streamlit as st
import pandas as pd


# Dados Fbref
rodadas_italiano, tabela_italiano = leitura_ordenacao_indice_fbref('./dados/italiano/fbref/rodadas_liga.csv', 
                                                                   './dados/italiano/fbref/tabela_liga.csv')
rodadas_premier, tabela_premier = leitura_ordenacao_indice_fbref('./dados/premier_league/fbref/rodadas_liga.csv', 
                                                              './dados/premier_league/fbref/tabela_liga.csv')
rodadas_bundesliga, tabela_bundesliga = leitura_ordenacao_indice_fbref('./dados/bundesliga/fbref/rodadas_liga.csv', 
                                                              './dados/bundesliga/fbref/tabela_liga.csv')
rodadas_franca, tabela_franca = leitura_ordenacao_indice_fbref('./dados/franca/fbref/rodadas_liga.csv', 
                                                              './dados/franca/fbref/tabela_liga.csv')
rodadas_la_liga, tabela_la_liga = leitura_ordenacao_indice_fbref('./dados/la_liga/fbref/rodadas_liga.csv', 
                                                              './dados/la_liga/fbref/tabela_liga.csv')

# Dados Co.Uk
temporadas_bundesliga_couk = pd.read_csv('./dados/bundesliga/couk/temporadas_baixadas.csv')
rodadas_bundesliga_couk = pd.read_csv('./dados/bundesliga/couk/temporada_atual.csv')

temporadas_franca_couk = pd.read_csv('./dados/franca/couk/temporadas_baixadas.csv')
rodadas_franca_couk = pd.read_csv('./dados/franca/couk/temporada_atual.csv')

temporadas_italiano_couk = pd.read_csv('./dados/italiano/couk/temporadas_baixadas.csv')
rodadas_italiano_couk = pd.read_csv('./dados/italiano/couk/temporada_atual.csv')

temporadas_la_liga_couk = pd.read_csv('./dados/la_liga/couk/temporadas_baixadas.csv')
rodadas_la_liga_couk = pd.read_csv('./dados/la_liga/couk/temporada_atual.csv')

temporadas_premier_league_couk = pd.read_csv('./dados/premier_league/couk/temporadas_baixadas.csv')
rodadas_premier_league_couk = pd.read_csv('./dados/premier_league/couk/temporada_atual.csv')


def main():
    # Seleção da liga
    st.title('Estatísticas de Clubes de Futebol')
    ligas = ['Liga Itália Série A', 'Premier League', 'Bundesliga', 'Liga da França', 'La Liga']
    liga = st.sidebar.selectbox('Liga', ligas)
    if liga == 'Liga Itália Série A':
        tabela = tabela_italiano
        rodadas = rodadas_italiano
        rodadas_couk = rodadas_italiano_couk
        temporadas = temporadas_italiano_couk
    elif liga == 'Premier League':
        tabela = tabela_premier
        rodadas = rodadas_premier
        rodadas_couk = rodadas_premier_league_couk
        temporadas = temporadas_premier_league_couk
    elif liga == 'Bundesliga':
        tabela = tabela_bundesliga
        rodadas = rodadas_bundesliga
        rodadas_couk = rodadas_bundesliga_couk
        temporadas = temporadas_bundesliga_couk
    elif liga == 'Liga da França':
        tabela = tabela_franca
        rodadas = rodadas_franca
        rodadas_couk = rodadas_franca_couk
        temporadas = temporadas_franca_couk
    elif liga == 'La Liga':
        tabela = tabela_la_liga
        rodadas = rodadas_la_liga
        rodadas_couk = rodadas_la_liga_couk
        temporadas = temporadas_la_liga_couk

    # Seleção do número de jogos
    ultimos_jogos = st.sidebar.selectbox('Últimos Jogos', [tabela['n_jogos'].max(), 5])

    # Selção do indicador
    descricao_indicadores_disponiveis = ['Confrontos Diretos', 'Resultados Liga', 'Gols', 'Escanteios', 'Cartões']
    selecione_indicador = st.sidebar.selectbox('Indicador', descricao_indicadores_disponiveis)

    # Seleção das equipes   
    col_1, col_2 = st.beta_columns(2)
    with col_1:
        # Seleção mandante
        mandante = st.selectbox('Mandante', tabela['equipe'])
        mandante_local = 'Em casa'
        st.image(rodadas.query('clube == @mandante')['escudo'].iloc[0])
        # Visualização dos indicadores da liga atual
        indicador_mandante_fbref = IndicadoresFbref(dados=rodadas, clube=mandante, local_jogo=mandante_local,
                                                    ultimos_jogos=ultimos_jogos)
        indicador_mandante_couk = IndicadoresCouk(dados=rodadas_couk, mandante=mandante, ultimos_jogos=ultimos_jogos)
        # Indicador selecionado
        if selecione_indicador == 'Resultados Liga':
            indicador_mandante_fbref.indicador_resultados()
        elif selecione_indicador == 'Gols':
            indicador_mandante_couk.gols_mandante()
        elif selecione_indicador == 'Escanteios':
            indicador_mandante_couk.escanteios_mandante()
        elif selecione_indicador == 'Cartões':
            indicador_mandante_couk.cartoes_mandante()
    with col_2:
        # Seleção visitante
        visitante = st.selectbox('Visitante', tabela['equipe'].sort_index(ascending=False).values)
        visitante_local = 'Visitante'
        st.image(rodadas.query('clube == @visitante')['escudo'].iloc[0])
        # Visualização dos indicadorers
        indicador_visitante_fbref = IndicadoresFbref(dados=rodadas, clube=visitante, local_jogo=visitante_local,
                                                    ultimos_jogos=ultimos_jogos)
        indicador_visitante_couk = IndicadoresCouk(dados=rodadas_couk, visitante=visitante, ultimos_jogos=ultimos_jogos)                                    
        # Indicador selecionado
        if selecione_indicador == 'Resultados Liga':
            indicador_visitante_fbref.indicador_resultados()
        elif selecione_indicador == 'Gols':
            indicador_visitante_couk.gols_visitante()
        elif selecione_indicador == 'Escanteios':
            indicador_visitante_couk.escanteios_visitante()
        elif selecione_indicador == 'Cartões':
            indicador_visitante_couk.cartoes_visitante()
    # Indicadores da liga atual e das ligas anteriores
    if selecione_indicador == 'Confrontos Diretos':
        IndicadoresCouk(temporadas, mandante, visitante).confronto_direto()
    elif selecione_indicador == 'Resultados Liga':
        confronto = rodadas.query('clube == @mandante and oponente == @visitante')[['data', 'local', 'clube', 'gols_marcados', 
                                                                                    'gols_sofridos', 'oponente']]
        confronto.columns = ['Data', 'Local', 'Clube', 'Gols Marcados', 'Gols Sofridos', 'Oponente']
        st.markdown('**CONFRONTO**')
        st.dataframe(confronto)
        st.markdown('**TABELA DA LIGA**')
        st.dataframe(tabela)
    st.markdown('Repositório no [GitHub](https://github.com/MarcosRMG/Estatisticas-de-Futebol)')
    st.markdown('Fonte de dados: [FBREF](https://fbref.com/pt/) e [Football-Data](https://www.football-data.co.uk/)')


if __name__ == '__main__':
    main()
