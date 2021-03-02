from analise import indicadores
import streamlit as st
import pandas as pd


# Leitura dos arquivos
rodadas_liga_italia_21 = pd.read_csv('../dados/italiano_serie_a_20_21/rodadas_liga.csv')
rodadas_liga_italia_21.rename({'Unnamed: 0': 'rodada'}, axis=1, inplace=True)
rodadas_liga_italia_21.sort_values(['clube', 'rodada'], ascending=False, inplace=True)
tabela_liga_italia_21 = pd.read_csv('../dados/italiano_serie_a_20_21/tabela_liga.csv')


def main():
    numero_jogos = range(2, tabela_liga_italia_21['jogos'].max())
    st.title('Liga Italiana Série A 20-21')
    ultimos_jogos = st.selectbox('Últimos Jogos', numero_jogos)
    col_1, col_2 = st.beta_columns(2)
    with col_1:
        equipe_1 = st.selectbox('Equipe Mandante', tabela_liga_italia_21['equipe'].values)
        st.image(rodadas_liga_italia_21.query('clube == @equipe_1')['escudo'].iloc[-1])
        indicadores(rodadas_liga_italia_21.query('clube == @equipe_1'), ultimos_jogos=ultimos_jogos)
        st.dataframe(rodadas_liga_italia_21.query('clube == @equipe_1').iloc[:ultimos_jogos, :-1])
    with col_2:
        equipe_2 = st.selectbox('Equipe Visitante', tabela_liga_italia_21['equipe'][1:].values)
        st.image(rodadas_liga_italia_21.query('clube == @equipe_2')['escudo'].iloc[-1])
        indicadores(rodadas_liga_italia_21.query('clube == @equipe_2'), ultimos_jogos=ultimos_jogos)
        st.dataframe(rodadas_liga_italia_21.query('clube == @equipe_2').iloc[:ultimos_jogos, :-1])

if __name__ == '__main__':
    main()
