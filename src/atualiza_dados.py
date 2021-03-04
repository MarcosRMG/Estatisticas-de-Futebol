from captura_tratamento_dados import CapturaDados
import os.path


# Italiano
url_tabela_liga_italiano = 'https://fbref.com/pt/comps/11/Serie-A-Estatisticas'

clubes_italiano = {'Inter': ['https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A',
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
url_tabela_premier_league = 'https://fbref.com/pt/comps/9/Premier-League-Estatisticas'		

clubes_premier_league = {

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

    'Brighton': ['https://fbref.com/pt/equipes/d07537b9/2020-2021/partidas/s10728/schedule/Brighton-and-Hove-Albion-Resultados-e-Calendarios-Premier-League',
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

# Budesliga
url_tabela_bundesliga = 'https://fbref.com/pt/comps/20/Bundesliga-Estatisticas'

clubes_bundesliga = {
	'Bayern Munich':['https://fbref.com/pt/equipes/054efa67/2020-2021/partidas/s10737/schedule/Bayern-Munich-Resultados-e-Calendarios-Bundesliga', 
	'https://fbref.com/pt/equipes/054efa67/2020-2021/partidas/s10737/passing_types/Bayern-Munich-Historicos-dos-Jogos-Bundesliga'], 
	'RB Leipzig': ['https://fbref.com/pt/equipes/acbb6a5b/2020-2021/partidas/s10737/schedule/RB-Leipzig-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/acbb6a5b/2020-2021/partidas/s10737/passing_types/RB-Leipzig-Historicos-dos-Jogos-Bundesliga'], 
	'Wolfsburg': ['https://fbref.com/pt/equipes/4eaa11d7/2020-2021/partidas/s10737/schedule/Wolfsburg-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/4eaa11d7/2020-2021/partidas/s10737/passing_types/Wolfsburg-Historicos-dos-Jogos-Bundesliga'], 
	'Eint Frankfurt': ['https://fbref.com/pt/equipes/f0ac8ee6/2020-2021/partidas/s10737/schedule/Eintracht-Frankfurt-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/f0ac8ee6/2020-2021/partidas/s10737/passing_types/Eintracht-Frankfurt-Historicos-dos-Jogos-Bundesliga'],
    'Dortmund': ['https://fbref.com/pt/equipes/add600ae/2020-2021/partidas/s10737/schedule/Dortmund-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/add600ae/2020-2021/partidas/s10737/passing_types/Dortmund-Historicos-dos-Jogos-Bundesliga'], 
	'Leverkusen': ['https://fbref.com/pt/equipes/c7a9f859/2020-2021/partidas/s10737/schedule/Bayer-Leverkusen-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/c7a9f859/2020-2021/partidas/s10737/passing_types/Bayer-Leverkusen-Historicos-dos-Jogos-Bundesliga'], 
	'Union Berlin': ['https://fbref.com/pt/equipes/7a41008f/2020-2021/partidas/s10737/schedule/Union-Berlin-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/7a41008f/2020-2021/partidas/s10737/passing_types/Union-Berlin-Historicos-dos-Jogos-Bundesliga'], 
	'Freiburg': ['https://fbref.com/pt/equipes/a486e511/2020-2021/partidas/s10737/schedule/Freiburg-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/a486e511/2020-2021/partidas/s10737/passing_types/Freiburg-Historicos-dos-Jogos-Bundesliga'], 
	"M'Gladbach": ['https://fbref.com/pt/equipes/32f3ee20/2020-2021/partidas/s10737/schedule/Monchengladbach-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/32f3ee20/2020-2021/partidas/s10737/passing_types/Monchengladbach-Historicos-dos-Jogos-Bundesliga'],
    'Stuttgart': ['https://fbref.com/pt/equipes/598bc722/2020-2021/partidas/s10737/schedule/Stuttgart-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/598bc722/2020-2021/partidas/s10737/passing_types/Stuttgart-Historicos-dos-Jogos-Bundesliga'], 
	'Hoffenheim': ['https://fbref.com/pt/equipes/033ea6b8/2020-2021/partidas/s10737/schedule/Hoffenheim-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/033ea6b8/2020-2021/partidas/s10737/passing_types/Hoffenheim-Historicos-dos-Jogos-Bundesliga'], 
	'Werder Bremen': ['https://fbref.com/pt/equipes/62add3bf/2020-2021/partidas/s10737/schedule/Werder-Bremen-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/62add3bf/2020-2021/partidas/s10737/passing_types/Werder-Bremen-Historicos-dos-Jogos-Bundesliga'], 
	'Augsburg': ['https://fbref.com/pt/equipes/0cdc4311/2020-2021/partidas/s10737/schedule/Augsburg-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/0cdc4311/2020-2021/partidas/s10737/passing_types/Augsburg-Historicos-dos-Jogos-Bundesliga'], 
	'Köln': ['https://fbref.com/pt/equipes/bc357bf7/2020-2021/partidas/s10737/schedule/Koln-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/bc357bf7/2020-2021/partidas/s10737/passing_types/Koln-Historicos-dos-Jogos-Bundesliga'],
    'Hertha BSC': ['https://fbref.com/pt/equipes/2818f8bc/2020-2021/partidas/s10737/schedule/Hertha-BSC-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/2818f8bc/2020-2021/partidas/s10737/passing_types/Hertha-BSC-Historicos-dos-Jogos-Bundesliga'], 
	'Arminia': ['https://fbref.com/pt/equipes/247c4b67/2020-2021/partidas/s10737/schedule/Arminia-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/247c4b67/2020-2021/partidas/s10737/passing_types/Arminia-Historicos-dos-Jogos-Bundesliga'], 
	'Mainz 05': ['https://fbref.com/pt/equipes/a224b06a/2020-2021/partidas/s10737/schedule/Mainz-05-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/a224b06a/2020-2021/partidas/s10737/passing_types/Mainz-05-Historicos-dos-Jogos-Bundesliga'], 
	'Schalke 04': ['https://fbref.com/pt/equipes/c539e393/2020-2021/partidas/s10737/schedule/Schalke-04-Resultados-e-Calendarios-Bundesliga',
	'https://fbref.com/pt/equipes/c539e393/2020-2021/partidas/s10737/passing_types/Schalke-04-Historicos-dos-Jogos-Bundesliga']
}

# La Liga
url_tabela_la_liga = 'https://fbref.com/pt/comps/12/La-Liga-Estatisticas'

clubes_la_liga = {
	'Atlético Madrid': ['https://fbref.com/pt/equipes/db3b9613/2020-2021/partidas/s10731/schedule/Atletico-Madrid-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/db3b9613/2020-2021/partidas/s10731/passing_types/Atletico-Madrid-Historicos-dos-Jogos-La-Liga'], 
	'Barcelona': ['https://fbref.com/pt/equipes/206d90db/2020-2021/partidas/s10731/schedule/Barcelona-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/206d90db/2020-2021/partidas/s10731/passing_types/Barcelona-Historicos-dos-Jogos-La-Liga'], 
	'Real Madrid': ['https://fbref.com/pt/equipes/53a2f082/2020-2021/partidas/s10731/schedule/Real-Madrid-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/53a2f082/2020-2021/partidas/s10731/passing_types/Real-Madrid-Historicos-dos-Jogos-La-Liga'], 
	'Sevilla': ['https://fbref.com/pt/equipes/ad2be733/2020-2021/partidas/s10731/schedule/Sevilla-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/ad2be733/2020-2021/partidas/s10731/passing_types/Sevilla-Historicos-dos-Jogos-La-Liga'],
    'Real Sociedad': ['https://fbref.com/pt/equipes/e31d1cd9/2020-2021/partidas/s10731/schedule/Real-Sociedad-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/e31d1cd9/2020-2021/partidas/s10731/passing_types/Real-Sociedad-Historicos-dos-Jogos-La-Liga'], 
	'Betis': ['https://fbref.com/pt/equipes/fc536746/2020-2021/partidas/s10731/schedule/Real-Betis-Resultados-e-Calendarios-La-Liga', 
	'https://fbref.com/pt/equipes/fc536746/2020-2021/partidas/s10731/passing_types/Real-Betis-Historicos-dos-Jogos-La-Liga'], 
	'Villarreal': ['https://fbref.com/pt/equipes/2a8183b3/2020-2021/partidas/s10731/schedule/Villarreal-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/2a8183b3/2020-2021/partidas/s10731/passing_types/Villarreal-Historicos-dos-Jogos-La-Liga'], 
	'Granada': ['https://fbref.com/pt/equipes/a0435291/2020-2021/partidas/s10731/schedule/Granada-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/a0435291/2020-2021/partidas/s10731/passing_types/Granada-Historicos-dos-Jogos-La-Liga'], 
	'Levante': ['https://fbref.com/pt/equipes/9800b6a1/2020-2021/partidas/s10731/schedule/Levante-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/9800b6a1/2020-2021/partidas/s10731/passing_types/Levante-Historicos-dos-Jogos-La-Liga'],
    'Athletic Club': ['https://fbref.com/pt/equipes/2b390eca/2020-2021/partidas/s10731/schedule/Athletic-Club-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/2b390eca/2020-2021/partidas/s10731/passing_types/Athletic-Club-Historicos-dos-Jogos-La-Liga'], 
	'Celta Vigo': ['https://fbref.com/pt/equipes/f25da7fb/2020-2021/partidas/s10731/schedule/Celta-Vigo-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/f25da7fb/2020-2021/partidas/s10731/passing_types/Celta-Vigo-Historicos-dos-Jogos-La-Liga'], 
	'Osasuna': ['https://fbref.com/pt/equipes/03c57e2b/2020-2021/partidas/s10731/schedule/Osasuna-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/03c57e2b/2020-2021/partidas/s10731/passing_types/Osasuna-Historicos-dos-Jogos-La-Liga'], 
	'Getafe': ['https://fbref.com/pt/equipes/7848bd64/2020-2021/partidas/s10731/schedule/Getafe-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/7848bd64/2020-2021/partidas/all_comps/passing_types/Getafe-Historicos-dos-Jogos-Todos-os-campeonatos'], 
	'Valencia': ['https://fbref.com/pt/equipes/dcc91a7b/2020-2021/partidas/s10731/schedule/Valencia-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/dcc91a7b/2020-2021/partidas/s10731/passing_types/Valencia-Historicos-dos-Jogos-La-Liga'],
    'Cádiz': ['https://fbref.com/pt/equipes/ee7c297c/2020-2021/partidas/s10731/schedule/Cadiz-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/ee7c297c/2020-2021/partidas/s10731/passing_types/Cadiz-Historicos-dos-Jogos-La-Liga'], 
	'Eibar': ['https://fbref.com/pt/equipes/bea5c710/2020-2021/partidas/s10731/schedule/Eibar-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/bea5c710/2020-2021/partidas/s10731/passing_types/Eibar-Historicos-dos-Jogos-La-Liga'], 
	'Valladolid': ['https://fbref.com/pt/equipes/17859612/2020-2021/partidas/s10731/schedule/Valladolid-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/17859612/2020-2021/partidas/s10731/passing_types/Valladolid-Historicos-dos-Jogos-La-Liga'], 
	'Alavés': ['https://fbref.com/pt/equipes/8d6fd021/2020-2021/partidas/s10731/schedule/Alaves-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/8d6fd021/2020-2021/partidas/s10731/passing_types/Alaves-Historicos-dos-Jogos-La-Liga'], 
	'Elche': ['https://fbref.com/pt/equipes/6c8b07df/2020-2021/partidas/s10731/schedule/Elche-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/6c8b07df/2020-2021/partidas/s10731/passing_types/Elche-Historicos-dos-Jogos-La-Liga'], 
	'Huesca': ['https://fbref.com/pt/equipes/c6c493e6/2020-2021/partidas/s10731/schedule/Huesca-Resultados-e-Calendarios-La-Liga',
	'https://fbref.com/pt/equipes/c6c493e6/2020-2021/partidas/s10731/passing_types/Huesca-Historicos-dos-Jogos-La-Liga']
}

url_tabela_liga_franca = 'https://fbref.com/pt/comps/13/Ligue-1-Estatisticas'

clubes_liga_franca = {
	'Lille': ['https://fbref.com/pt/equipes/cb188c0c/2020-2021/partidas/s10732/schedule/Lille-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/cb188c0c/2020-2021/partidas/s10732/passing_types/Lille-Historicos-dos-Jogos-Ligue-1'], 
	'Paris S-G': ['https://fbref.com/pt/equipes/e2d8892c/2020-2021/partidas/s10732/schedule/Paris-Saint-Germain-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/e2d8892c/2020-2021/partidas/s10732/passing_types/Paris-Saint-Germain-Historicos-dos-Jogos-Ligue-1'], 
	'Lyon': ['https://fbref.com/pt/equipes/d53c0b06/2020-2021/partidas/s10732/schedule/Lyon-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/d53c0b06/2020-2021/partidas/s10732/passing_types/Lyon-Historicos-dos-Jogos-Ligue-1'], 
	'Monaco': ['https://fbref.com/pt/equipes/fd6114db/2020-2021/partidas/s10732/schedule/Monaco-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/fd6114db/2020-2021/partidas/s10732/passing_types/Monaco-Historicos-dos-Jogos-Ligue-1'], 
	'Metz': ['https://fbref.com/pt/equipes/f83960ae/2020-2021/partidas/s10732/schedule/Metz-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/f83960ae/2020-2021/partidas/s10732/passing_types/Metz-Historicos-dos-Jogos-Ligue-1'], 
	'Lens': ['https://fbref.com/pt/equipes/fd4e0f7d/2020-2021/partidas/s10732/schedule/Lens-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/fd4e0f7d/2020-2021/partidas/s10732/passing_types/Lens-Historicos-dos-Jogos-Ligue-1'],
    'Marseille': ['https://fbref.com/pt/equipes/5725cc7b/2020-2021/partidas/s10732/schedule/Marseille-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/5725cc7b/2020-2021/partidas/s10732/passing_types/Marseille-Historicos-dos-Jogos-Ligue-1'], 
	'Montpellier': ['https://fbref.com/pt/equipes/281b0e73/2020-2021/partidas/s10732/schedule/Montpellier-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/281b0e73/2020-2021/partidas/s10732/passing_types/Montpellier-Historicos-dos-Jogos-Ligue-1'], 
	'Rennes': ['https://fbref.com/pt/equipes/b3072e00/2020-2021/partidas/s10732/schedule/Rennes-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/b3072e00/2020-2021/partidas/s10732/passing_types/Rennes-Historicos-dos-Jogos-Ligue-1'], 
	'Angers': ['https://fbref.com/pt/equipes/69236f98/2020-2021/partidas/s10732/schedule/Angers-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/69236f98/2020-2021/partidas/s10732/passing_types/Angers-Historicos-dos-Jogos-Ligue-1'], 
	'Bordeaux': ['https://fbref.com/pt/equipes/123f3efe/2020-2021/partidas/s10732/schedule/Bordeaux-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/123f3efe/2020-2021/partidas/s10732/passing_types/Bordeaux-Historicos-dos-Jogos-Ligue-1'], 
	'Nice': ['https://fbref.com/pt/equipes/132ebc33/2020-2021/partidas/s10732/schedule/Nice-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/132ebc33/2020-2021/partidas/s10732/passing_types/Nice-Historicos-dos-Jogos-Ligue-1'],
    'Reims': ['https://fbref.com/pt/equipes/7fdd64e0/2020-2021/partidas/s10732/schedule/Reims-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/7fdd64e0/2020-2021/partidas/s10732/passing_types/Reims-Historicos-dos-Jogos-Ligue-1'], 
	'Brest': ['https://fbref.com/pt/equipes/fb08dbb3/2020-2021/partidas/s10732/schedule/Brest-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/fb08dbb3/2020-2021/partidas/s10732/passing_types/Brest-Historicos-dos-Jogos-Ligue-1'], 
	'Strasbourg': ['https://fbref.com/pt/equipes/c0d3eab4/2020-2021/partidas/s10732/schedule/Strasbourg-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/c0d3eab4/2020-2021/partidas/s10732/passing_types/Strasbourg-Historicos-dos-Jogos-Ligue-1'], 
	'Saint-Étienne': ['https://fbref.com/pt/equipes/d298ef2c/2020-2021/partidas/s10732/schedule/Saint-Etienne-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/d298ef2c/2020-2021/partidas/s10732/passing_types/Saint-Etienne-Historicos-dos-Jogos-Ligue-1'], 
	'Lorient': ['https://fbref.com/pt/equipes/d2c87802/2020-2021/partidas/s10732/schedule/Lorient-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/d2c87802/2020-2021/partidas/s10732/passing_types/Lorient-Historicos-dos-Jogos-Ligue-1'],
    'Nîmes': ['https://fbref.com/pt/equipes/1cbf5f9e/2020-2021/partidas/s10732/schedule/Nimes-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/1cbf5f9e/2020-2021/partidas/s10732/passing_types/Nimes-Historicos-dos-Jogos-Ligue-1'], 
	'Nantes': ['https://fbref.com/pt/equipes/d7a486cd/2020-2021/partidas/s10732/schedule/Nantes-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/d7a486cd/2020-2021/partidas/s10732/passing_types/Nantes-Historicos-dos-Jogos-Ligue-1'], 
	'Dijon': ['https://fbref.com/pt/equipes/8dfb7350/2020-2021/partidas/s10732/schedule/Dijon-Resultados-e-Calendarios-Ligue-1',
	'https://fbref.com/pt/equipes/8dfb7350/2020-2021/partidas/s10732/passing_types/Dijon-Historicos-dos-Jogos-Ligue-1']}

def atualiza_tabela(url_tabela_liga, caminho_arquivo_tabela, classe=CapturaDados):
	'''
	--> Atualiza a tabela da liga

	:param classe: Classe que captura as informações da tabela da liga
	:param url_tabela_liga: URL com as informações da tabela da liga
	:param metodo: Método da classe que realiza o tratamento da tabela da liga
	'''
	dados = classe(url_tabela_liga=url_tabela_liga, caminho_arquivo_tabela=caminho_arquivo_tabela)
	dados.trata_tabela_liga()


def atualiza_rodadas(clubes: dict(), caminho_arquivo_rodadas: str,	classe=CapturaDados):
	'''
	--> Atualiza as rodadas da liga

	:param clubes: Dicionário com a identificação do clube e as URL das rodadas, escudos e do número de 
	escanteios
	:param caminho_arquivo_rodadas: Local onde o arquivo será salvo
	:param classe: Classe que captura e trata as informações
	'''
	if os.path.exists(caminho_arquivo_rodadas):
		os.remove(caminho_arquivo_rodadas)
	for clube, url in clubes.items():
		dados = classe(clube=clube, url_resultados=url[0], 
					   caminho_arquivo_rodadas=caminho_arquivo_rodadas, url_tipos_passes=url[1], 
					   url_escudo=url[0])
		dados.trata_url_resultados()
		dados.trata_url_tipos_passes()
		dados.trata_url_escudo()
		dados.resultados_clube()


#atualiza_tabela(url_tabela_liga=url_tabela_liga_italiano, 
#				caminho_arquivo_tabela='../dados/italiano/tabela_liga.csv')
atualiza_rodadas(clubes_italiano, '../dados/italiano/rodadas_liga.csv')
