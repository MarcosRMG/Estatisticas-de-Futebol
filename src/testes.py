from captura_tratamento_dados import CapturaDados, localiza_adiciona_url

clubes = {
	'Atlético Madrid': ['https://fbref.com/pt/equipes/db3b9613/2020-2021/partidas/s10731/schedule/Atletico-Madrid-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/db3b9613/2020-2021/partidas/s10731/passing_types/Atletico-Madrid-Historicos-dos-Jogos-La-Liga'], 
	
    'Barcelona': ['https://fbref.com/pt/equipes/206d90db/2020-2021/partidas/s10731/schedule/Barcelona-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/206d90db/2020-2021/partidas/s10731/passing_types/Barcelona-Historicos-dos-Jogos-La-Liga'], 
}

localiza_adiciona_url(clubes, 1, ['passing', 'shooting'])


def testa_captura_dados(classe=CapturaDados(clube='Atlético Madrid', 
                                url_resultados=clubes['Atlético Madrid'][0], 
                                url_tipos_passes=clubes['Atlético Madrid'][1], 
                                url_passes=clubes['Atlético Madrid'][2], 
                                url_chutes=clubes['Atlético Madrid'][3], 
                                url_escudo=clubes['Atlético Madrid'][0],
                                caminho_arquivo_rodadas='teste.csv')):
    dados = classe
    dados.trata_url_resultados()
    dados.trata_url_tipos_passes()
    dados.trata_url_passes()
    dados.trata_url_chutes()
    dados.trata_url_escudo()
    dados.resultados_clube()
    #dados.trata_tabela_liga()
    return dados

'''
def testa_captura_dados_completos(clubes=clubes):
    for clube, url in clubes.items():
        testa_captura_dados()
'''