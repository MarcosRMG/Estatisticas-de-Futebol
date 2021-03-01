from captura_tratamento_dados import CapturaDados
import os.path


url_tabela_liga = 'https://fbref.com/pt/comps/11/Serie-A-Estatisticas'

clubes = {'Inter': ['https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A',
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


def atualiza_tabela(classe=CapturaDados, url_tabela_liga=url_tabela_liga):
	'''
	--> Atualiza a tabela da liga

	:param classe: Classe que captura as informações da tabela da liga
	:param url_tabela_liga: URL com as informações da tabela da liga
	:param metodo: Método da classe que realiza o tratamento da tabela da liga
	'''
	dados = classe(url_tabela_liga=url_tabela_liga)
	dados.trata_tabela_liga()


def atualiza_rodadas(clubes=clubes, classe=CapturaDados, url_tabela_liga=url_tabela_liga):
	'''
	--> Atualiza as rodadas da liga

	:param clubes: Dicionário com a identificação do clube e as URL das rodadas e do número de 
	escanteios
	:param classe: Classe que captura e trata as informações
	:param url_tabela_liga: URL que contem as informações da liga
	'''
	if os.path.exists('../dados/italiano_serie_a_20_21/rodadas_liga.csv'):
		os.remove('../dados/italiano_serie_a_20_21/rodadas_liga.csv')
	for clube, url in clubes.items():
		dados = classe(clube, url[0], url[1], url[0], url_tabela_liga)
		dados.trata_url_resultados()
		dados.trata_url_tipos_passes()
		dados.trata_url_escudo()
		dados.resultados_clube()

#atualiza_tabela()
atualiza_rodadas()