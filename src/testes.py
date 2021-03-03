from captura_tratamento_dados import CapturaDados

url_resultados = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A'
url_tipos_passes = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/passing_types/Internazionale-Historicos-dos-Jogos-Serie-A'
url_escudo = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A'
url_tabela_liga = 'https://fbref.com/pt/comps/11/Serie-A-Estatisticas'

clubes = {
	'Manchester City': ['https://fbref.com/pt/equipes/b8fd03ef/2020-2021/partidas/s10728/schedule/Manchester-City-Resultados-e-Calendarios-Premier-League', 
	'https://fbref.com/pt/equipes/b8fd03ef/2020-2021/partidas/s10728/passing_types/Manchester-City-Historicos-dos-Jogos-Premier-League'], 
	'Manchester Utd': ['https://fbref.com/pt/equipes/19538871/2020-2021/partidas/s10728/schedule/Manchester-United-Resultados-e-Calendarios-Premier-League', 
	'https://fbref.com/pt/equipes/19538871/2020-2021/partidas/s10728/passing_types/Manchester-United-Historicos-dos-Jogos-Premier-League'], 
	'Leicester City': ['https://fbref.com/pt/equipes/a2d435b3/2020-2021/partidas/s10728/schedule/Leicester-City-Resultados-e-Calendarios-Premier-League', 
	'https://fbref.com/pt/equipes/a2d435b3/2020-2021/partidas/s10728/passing_types/Leicester-City-Historicos-dos-Jogos-Premier-League'], 
	'West Ham': ['https://fbref.com/pt/equipes/7c21e445/2020-2021/partidas/s10728/schedule/West-Ham-United-Resultados-e-Calendarios-Premier-League',
	'https://fbref.com/pt/equipes/7c21e445/2020-2021/partidas/s10728/passing_types/West-Ham-United-Historicos-dos-Jogos-Premier-League'],
    'Chelsea': ['https://fbref.com/pt/equipes/cff3d9bb/2020-2021/partidas/s10728/schedule/Chelsea-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/cff3d9bb/2020-2021/partidas/s10728/passing_types/Chelsea-Historicos-dos-Jogos-Premier-League'], 
    'Liverpool': ['https://fbref.com/pt/equipes/822bd0ba/2020-2021/partidas/s10728/schedule/Liverpool-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/822bd0ba/2020-2021/partidas/s10728/passing_types/Liverpool-Historicos-dos-Jogos-Premier-League'], 
    'Everton': ['https://fbref.com/pt/equipes/d3fd31cc/2020-2021/partidas/s10728/schedule/Everton-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/d3fd31cc/2020-2021/partidas/s10728/passing_types/Everton-Historicos-dos-Jogos-Premier-League'], 
    'Tottenham': ['https://fbref.com/pt/equipes/361ca564/2020-2021/partidas/s10728/schedule/Tottenham-Hotspur-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/361ca564/2020-2021/partidas/s10728/passing_types/Tottenham-Hotspur-Historicos-dos-Jogos-Premier-League'], 
    'Aston Villa': ['https://fbref.com/pt/equipes/8602292d/2020-2021/partidas/s10728/schedule/Aston-Villa-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/8602292d/2020-2021/partidas/s10728/passing_types/Aston-Villa-Historicos-dos-Jogos-Premier-League'],
    'Arsenal': ['https://fbref.com/pt/equipes/18bb7c10/2020-2021/partidas/s10728/schedule/Arsenal-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/18bb7c10/2020-2021/partidas/s10728/passing_types/Arsenal-Historicos-dos-Jogos-Premier-League'], 
    'Leeds United': ['https://fbref.com/pt/equipes/5bfb9659/2020-2021/partidas/s10728/schedule/Leeds-United-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/5bfb9659/2020-2021/partidas/s10728/passing_types/Leeds-United-Historicos-dos-Jogos-Premier-League'], 
    'Wolves': ['https://fbref.com/pt/equipes/8cec06e1/2020-2021/partidas/s10728/schedule/Wolverhampton-Wanderers-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/8cec06e1/2020-2021/partidas/s10728/passing_types/Wolverhampton-Wanderers-Historicos-dos-Jogos-Premier-League'], 
    'Crystal Palace': ['https://fbref.com/pt/equipes/47c64c55/2020-2021/partidas/s10728/schedule/Crystal-Palace-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/47c64c55/2020-2021/partidas/s10728/passing_types/Crystal-Palace-Historicos-dos-Jogos-Premier-League'],
    'Southampton': ['https://fbref.com/pt/equipes/33c895d4/2020-2021/partidas/s10728/schedule/Southampton-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/33c895d4/2020-2021/partidas/s10728/passing_types/Southampton-Historicos-dos-Jogos-Premier-League'],
    'Burnley': ['https://fbref.com/pt/equipes/943e8050/2020-2021/partidas/s10728/schedule/Burnley-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/943e8050/2020-2021/partidas/s10728/passing_types/Burnley-Historicos-dos-Jogos-Premier-League'], 
    'Brighton': ['https://fbref.com/pt/equipes/d07537b9/Brighton-and-Hove-Albion-Estatisticas#all_matchlogs_all',
    'https://fbref.com/pt/equipes/d07537b9/2020-2021/partidas/all_comps/passing_types/Brighton-and-Hove-Albion-Historicos-dos-Jogos-Todos-os-campeonatos'], 
    'Newcastle Utd': ['https://fbref.com/pt/equipes/b2b47a98/2020-2021/partidas/s10728/schedule/Newcastle-United-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/b2b47a98/2020-2021/partidas/s10728/passing_types/Newcastle-United-Historicos-dos-Jogos-Premier-League'], 
    'Fulham': ['https://fbref.com/pt/equipes/fd962109/2020-2021/partidas/s10728/schedule/Fulham-Resultados-e-Calendarios-Premier-League', 
    'https://fbref.com/pt/equipes/fd962109/2020-2021/partidas/all_comps/passing_types/Fulham-Historicos-dos-Jogos-Todos-os-campeonatos'],
    'West Brom': ['https://fbref.com/pt/equipes/60c6b05f/2020-2021/partidas/s10728/schedule/West-Bromwich-Albion-Resultados-e-Calendarios-Premier-League',
    'https://fbref.com/pt/equipes/60c6b05f/2020-2021/partidas/s10728/passing_types/West-Bromwich-Albion-Historicos-dos-Jogos-Premier-League'], 
    'Sheffield Utd': ['https://fbref.com/pt/equipes/1df6b87e/2020-2021/partidas/s10728/schedule/Sheffield-United-Resultados-e-Calendarios-Premier-League', 
    'https://fbref.com/pt/equipes/1df6b87e/2020-2021/partidas/s10728/passing_types/Sheffield-United-Historicos-dos-Jogos-Premier-League']
}


def testa_captura_dados(classe=CapturaDados(url_resultados=clubes['Sheffield Utd'][0], 
											url_tipos_passes=clubes['Sheffield Utd'][1],
											url_escudo=clubes['Sheffield Utd'][0])):
    dados = classe
    dados.trata_url_resultados()
    #dados.trata_url_tipos_passes()
    #dados.trata_url_escudo()
    #dados.resultados_clube()
    #dados.trata_tabela_liga()
    return dados


'''
def testa_captura_dados_completos(clubes=clubes):
    for clube, url in clubes.items():
        testa_captura_dados()
'''