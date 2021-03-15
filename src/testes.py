from captura_tratamento_dados import CapturaDados, localiza_adiciona_url


url_tabela_premier_league = 'https://fbref.com/pt/comps/9/Premier-League-Estatisticas'		
clubes = {
	'Manchester City': ['https://fbref.com/pt/equipes/b8fd03ef/2020-2021/partidas/s10728/schedule/Manchester-City-Resultados-e-Calendarios-Premier-League', 
	'https://fbref.com/pt/equipes/b8fd03ef/2020-2021/partidas/s10728/passing_types/Manchester-City-Historicos-dos-Jogos-Premier-League'],
}

localiza_adiciona_url(clubes, 1, ['passing', 'shooting', 'misc', 'keeper'])


def testa_captura_dados(classe=CapturaDados(clube='Manchester City', 
                                url_resultados=clubes['Manchester City'][0], 
                                url_tipos_passes=clubes['Manchester City'][1], 
                                url_passes=clubes['Manchester City'][2], 
                                url_chutes=clubes['Manchester City'][3],
                                url_cartoes=clubes['Manchester City'][4],
                                url_goleiro=clubes['Manchester City'][5],
                                url_escudo=clubes['Manchester City'][0],
                                caminho_arquivo_rodadas='teste.csv',
                                url_tabela_liga=url_tabela_premier_league,
                                caminho_arquivo_tabela='./dados/bundesliga/tabela.csv')):
    #dados = classe
    #dados.trata_url_resultados()
    #dados.trata_url_tipos_passes()
    #dados.trata_url_passes()
    #dados.trata_url_chutes()
    #dados.trata_url_cartoes()
    #dados.trata_url_goleiro()
    #dados.trata_url_escudo()
    #dados.resultados_clube()
    #dados.trata_tabela_liga()
    return dados

'''
def testa_captura_dados_completos(clubes=clubes):
    for clube, url in clubes.items():
        testa_captura_dados()
'''