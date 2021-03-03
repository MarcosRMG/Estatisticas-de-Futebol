from captura_tratamento_dados import CapturaDados
import os.path


# Italiano
url_tabela_liga_italiano_a_20_21 = 'https://fbref.com/pt/comps/11/Serie-A-Estatisticas'

clubes_italiano_a_20_21 = {'Inter': ['https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A',
	   'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/passing_types/Internazionale-Historicos-dos-Jogos-Serie-A'], 
 
 'Milan': ['https://fbref.com/pt/equipes/dc56fe14/2020-2021/partidas/s10730/schedule/Milan-Resultados-e-Calendarios-Serie-A',
 	    'https://fbref.com/pt/equipes/dc56fe14/2020-2021/partidas/s10730/passing_types/Milan-Historicos-dos-Jogos-Serie-A'],
 
 'Juventus': ['https://fbref.com/pt/equipes/e0652b02/2020-2021/partidas/s10730/schedule/Juventus-Resultados-e-Calendarios-Serie-A',
 	      'https://fbref.com/pt/equipes/e0652b02/2020-2021/partidas/s10730/passing_types/Juventus-Historicos-dos-Jogos-Serie-A'],
 
 'Atalanta': ['https://fbref.com/pt/equipes/922493f3/2020-2021/partidas/s10730/schedule/Atalanta-Resultados-e-Calendarios-Serie-A',
 	      'https://fbref.com/pt/equipes/922493f3/2020-2021/partidas/s10730/passing_types/Atalanta-Historicos-dos-Jogos-Serie-A'],
 	      
 'Roma': ['https://fbref.com/pt/equipes/cf74a709/2020-2021/partidas/s10730/schedule/Roma-Resultados-e-Calendarios-Serie-A',
 	  'https://fbref.com/pt/equipes/cf74a709/2020-2021/partidas/s10730/passing_types/Roma-Historicos-dos-Jogos-Serie-A'],
 
 'Lazio': ['https://fbref.com/pt/equipes/7213da33/2020-2021/partidas/s10730/schedule/Lazio-Resultados-e-Calendarios-Serie-A',
 	   'https://fbref.com/pt/equipes/7213da33/2020-2021/partidas/s10730/passing_types/Lazio-Historicos-dos-Jogos-Serie-A'],
 	   
 'Napoli': ['https://fbref.com/pt/equipes/d48ad4ff/2020-2021/partidas/s10730/schedule/Napoli-Resultados-e-Calendarios-Serie-A',
 	    'https://fbref.com/pt/equipes/d48ad4ff/2020-2021/partidas/s10730/passing_types/Napoli-Historicos-dos-Jogos-Serie-A'],
 	    
 'Sassuolo': ['https://fbref.com/pt/equipes/e2befd26/2020-2021/partidas/s10730/schedule/Sassuolo-Resultados-e-Calendarios-Serie-A',
 	      'https://fbref.com/pt/equipes/e2befd26/2020-2021/partidas/s10730/passing_types/Sassuolo-Historicos-dos-Jogos-Serie-A'],
 	      
 'Hellas Verona': ['https://fbref.com/pt/equipes/0e72edf2/2020-2021/partidas/s10730/schedule/Hellas-Verona-Resultados-e-Calendarios-Serie-A',
 		   'https://fbref.com/pt/equipes/0e72edf2/2020-2021/partidas/s10730/passing_types/Hellas-Verona-Historicos-dos-Jogos-Serie-A'],
 		   
 'Sampdoria': ['https://fbref.com/pt/equipes/8ff9e3b3/2020-2021/partidas/s10730/schedule/Sampdoria-Resultados-e-Calendarios-Serie-A',
 		'https://fbref.com/pt/equipes/8ff9e3b3/2020-2021/partidas/s10730/passing_types/Sampdoria-Historicos-dos-Jogos-Serie-A'],
 			
 'Bologna': ['https://fbref.com/pt/equipes/1d8099f8/2020-2021/partidas/s10730/schedule/Bologna-Resultados-e-Calendarios-Serie-A',
 	     'https://fbref.com/pt/equipes/1d8099f8/2020-2021/partidas/s10730/passing_types/Bologna-Historicos-dos-Jogos-Serie-A'],
 	     
 'Udinese': ['https://fbref.com/pt/equipes/04eea015/2020-2021/partidas/s10730/schedule/Udinese-Resultados-e-Calendarios-Serie-A',
 	     'https://fbref.com/pt/equipes/04eea015/2020-2021/partidas/s10730/passing_types/Udinese-Historicos-dos-Jogos-Serie-A'],
 	     
 'Genoa': ['https://fbref.com/pt/equipes/658bf2de/2020-2021/partidas/s10730/schedule/Genoa-Resultados-e-Calendarios-Serie-A',
 	   'https://fbref.com/pt/equipes/658bf2de/2020-2021/partidas/s10730/passing_types/Genoa-Historicos-dos-Jogos-Serie-A'],
 	   
 'Fiorentina': ['https://fbref.com/pt/equipes/421387cf/2020-2021/partidas/s10730/schedule/Fiorentina-Resultados-e-Calendarios-Serie-A',
 		'https://fbref.com/pt/equipes/421387cf/2020-2021/partidas/s10730/passing_types/Fiorentina-Historicos-dos-Jogos-Serie-A'],
 		
 'Spezia': ['https://fbref.com/pt/equipes/68449f6d/2020-2021/partidas/s10730/schedule/Spezia-Resultados-e-Calendarios-Serie-A',
 	    'https://fbref.com/pt/equipes/68449f6d/2020-2021/partidas/s10730/passing_types/Spezia-Historicos-dos-Jogos-Serie-A'],
 	    
 'Benevento': ['https://fbref.com/pt/equipes/4fcb34fd/2020-2021/partidas/s10730/schedule/Benevento-Resultados-e-Calendarios-Serie-A',
 		'https://fbref.com/pt/equipes/4fcb34fd/2020-2021/partidas/s10730/passing_types/Benevento-Historicos-dos-Jogos-Serie-A'],
 		
 'Torino': ['https://fbref.com/pt/equipes/105360fe/2020-2021/partidas/s10730/schedule/Torino-Resultados-e-Calendarios-Serie-A',
 	    'https://fbref.com/pt/equipes/105360fe/2020-2021/partidas/s10730/passing_types/Torino-Historicos-dos-Jogos-Serie-A'],
 	    
 'Cagliari': ['https://fbref.com/pt/equipes/c4260e09/2020-2021/partidas/s10730/schedule/Cagliari-Resultados-e-Calendarios-Serie-A',
 	      'https://fbref.com/pt/equipes/c4260e09/2020-2021/partidas/s10730/passing_types/Cagliari-Historicos-dos-Jogos-Serie-A'],
 	      
 'Parma': ['https://fbref.com/pt/equipes/eab4234c/2020-2021/partidas/s10730/schedule/Parma-Resultados-e-Calendarios-Serie-A',
 	   'https://fbref.com/pt/equipes/eab4234c/2020-2021/partidas/s10730/passing_types/Parma-Historicos-dos-Jogos-Serie-A'],
 	   
 'Crotone': ['https://fbref.com/pt/equipes/3074d7b1/2020-2021/partidas/s10730/schedule/Crotone-Resultados-e-Calendarios-Serie-A',
 	     'https://fbref.com/pt/equipes/3074d7b1/2020-2021/partidas/s10730/passing_types/Crotone-Historicos-dos-Jogos-Serie-A']}

# Premier League
url_tabela_premier_league_20_21 = 'https://fbref.com/pt/comps/9/Premier-League-Estatisticas'

clubes_premier_league_20_21 = {
	'Manchester City': ['https://fbref.com/pt/equipes/b8fd03ef/2020-2021/partidas/s10728/schedule/Manchester-City-Resultados-e-Calendarios-Premier-League', 
	'https://fbref.com/pt/equipes/b8fd03ef/2020-2021/partidas/s10728/passing_types/Manchester-City-Historicos-dos-Jogos-Premier-League'], 
	'Manchester Utd'['https://fbref.com/pt/equipes/19538871/2020-2021/partidas/s10728/schedule/Manchester-United-Resultados-e-Calendarios-Premier-League', 
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

def atualiza_tabela(url_tabela_liga, caminho_arquivo_tabela, classe=CapturaDados):
	'''
	--> Atualiza a tabela da liga

	:param classe: Classe que captura as informações da tabela da liga
	:param url_tabela_liga: URL com as informações da tabela da liga
	:param metodo: Método da classe que realiza o tratamento da tabela da liga
	'''
	dados = classe(url_tabela_liga=url_tabela_liga, caminho_arquivo_tabela=caminho_arquivo_tabela)
	dados.trata_tabela_liga()


def atualiza_rodadas(clubes, url_tabela_liga, caminho_arquivo_rodadas, classe=CapturaDados):
	'''
	--> Atualiza as rodadas da liga

	:param clubes: Dicionário com a identificação do clube e as URL das rodadas e do número de 
	escanteios
	:param classe: Classe que captura e trata as informações
	:param url_tabela_liga: URL que contem as informações da liga
	'''
	if os.path.exists(caminho_arquivo_rodadas):
		os.remove(caminho_arquivo_rodadas)
	for clube, url in clubes.items():
		dados = classe(clube, url[0], url[1], url[0], url_tabela_liga)
		dados.trata_url_resultados()
		dados.trata_url_tipos_passes()
		dados.trata_url_escudo()
		dados.resultados_clube()


atualiza_tabela(url_tabela_liga=url_tabela_premier_league_20_21, 
				caminho_arquivo_tabela='../dados/premier_league_20_21/tabela_liga.csv')
#atualiza_rodadas()