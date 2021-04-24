from captura_tratamento_dados import CapturaDadosFbref, CapturaDadosCoUk, GeraUrlFbref
import os.path


# Site de referência: https://fbref.com/pt/
# Urls das ligas por equipe


# Italiano
url_tabela_italiano = 'https://fbref.com/pt/comps/11/Serie-A-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_italiano, padrao_2_url_resultados='/2020-2021/partidas/s10730/schedule/', 
						padrao_3_url_resultados='-Resultados-e-Calendarios-Serie-A')
url_clube.equipes_liga()
clubes_italiano = url_clube.gera_url()


# Premier League
url_tabela_premier_league = 'https://fbref.com/pt/comps/9/Premier-League-Estatisticas'		
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_premier_league, padrao_2_url_resultados='/2020-2021/partidas/s10728/schedule/', 
						padrao_3_url_resultados='-Resultados-e-Calendarios-Premier-League')
url_clube.equipes_liga()
clubes_premier_league = url_clube.gera_url()


# Budesliga
url_tabela_bundesliga = 'https://fbref.com/pt/comps/20/Bundesliga-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_bundesliga, padrao_2_url_resultados='/2020-2021/partidas/s10737/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Bundesliga')
url_clube.equipes_liga()
clubes_bundesliga = url_clube.gera_url()


# La Liga
url_tabela_la_liga = 'https://fbref.com/pt/comps/12/La-Liga-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_la_liga, padrao_2_url_resultados='/2020-2021/partidas/s10731/schedule/', 
						padrao_3_url_resultados='-Resultados-e-Calendarios-La-Liga')
url_clube.equipes_liga()
clubes_la_liga = url_clube.gera_url()


# Liga da França
url_tabela_franca = 'https://fbref.com/pt/comps/13/Ligue-1-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_franca, padrao_2_url_resultados='/2020-2021/partidas/s10732/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Ligue-1')
url_clube.equipes_liga()
clubes_franca = url_clube.gera_url()


# Scócia Premiership
'''
url_tabela_escocia = 'https://fbref.com/pt/comps/40/Scottish-Premiership-Stats'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_escocia, padrao_2_url_resultados='/2020-2021/partidas/s10750/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Scottish-Premiership')
url_clube.equipes_liga()
clubes_escocia = url_clube.gera_url()
'''

# Portugal 
url_tabela_portugal = 'https://fbref.com/pt/comps/32/Primeira-Liga-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_portugal, padrao_2_url_resultados='/2020-2021/partidas/s10744/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Primeira-Liga')
url_clube.equipes_liga()
clubes_portugal = url_clube.gera_url()


# Belgica
url_tabela_belgica = 'https://fbref.com/pt/comps/37/Belgian-First-Division-A-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_belgica, padrao_2_url_resultados='/2020-2021/partidas/s10748/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Belgian-First-Division-A')
url_clube.equipes_liga()
clubes_belgica = url_clube.gera_url()


# Turquia
url_tabela_turquia = 'https://fbref.com/pt/comps/26/Super-Lig-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_turquia, padrao_2_url_resultados='/2020-2021/partidas/s10740/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Super-Lig')
url_clube.equipes_liga()
clubes_turquia = url_clube.gera_url()


# Grécia
'''
url_tabela_grecia = 'https://fbref.com/pt/comps/27/Super-League-Greece-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_grecia, padrao_2_url_resultados='/2020-2021/partidas/s10741/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Super-League-Greece')
url_clube.equipes_liga()
clubes_grecia = url_clube.gera_url()
'''
# Atualizando dados
class atualiza_dados_fbref:
	'''
	--> Atualiza os dados coletados no site https://fbref.com/pt/
	'''
	def __init__(self, url_tabela_liga=None, caminho_arquivo_tabela=None, clubes=None, caminho_arquivo_rodadas=None, 
				classe_captura=CapturaDadosFbref):
		'''
		:param url_tabela_liga: URL referente a tabela da liga
		:param caminho_arquivo_tabela: Endereço onde será gerado o arquivo csv da tabela da liga
		:param clubes: Dicionário com a descrição dos clubes da liga
		:param caminho_arquivo_rodadas: Endereço onde será gerado o arquivo csv dos jogos da liga
		:param classe_captura: Classe que captura as informações na internet
		''' 
		self._url_tabela_liga = url_tabela_liga
		self._caminho_arquivo_tabela = caminho_arquivo_tabela
		self._clubes = clubes
		self._caminho_arquivo_rodadas = caminho_arquivo_rodadas
		self._classe_captura = classe_captura


	def atualiza_tabela(self):
		'''
		--> Atualiza a tabela da liga
		'''
		dados = self._classe_captura(url_tabela_liga=self._url_tabela_liga, caminho_arquivo_tabela=self._caminho_arquivo_tabela)
		dados.trata_tabela_liga()

	
	def atualiza_rodadas(self):
		'''
		--> Atualiza as rodadas da liga
		'''
		if os.path.exists(self._caminho_arquivo_rodadas):
			os.remove(self._caminho_arquivo_rodadas)
		for clube, url in self._clubes.items():
			dados = self._classe_captura(clube=clube, url_resultados=url[0], url_escudo=url[0], 
                                        caminho_arquivo_rodadas=self._caminho_arquivo_rodadas)
			dados.trata_url_resultados()
			dados.trata_url_escudo()
			dados.resultados_clube()

	
	def atualizacao_dados(self):
		'''
		--> Chama as funções de atualização de dados

		:param escanteios: Variação da URL da página com as informações do número de escanteios
		:param cartoes: Variação da URL da página com as informações do número de cartões
		'''
		self.atualiza_tabela()
		self.atualiza_rodadas()


def atualiza_todas_ligas_fbref(ligas = {
	'Bundesliga': [url_tabela_bundesliga, './dados/bundesliga/fbref/tabela_liga.csv', clubes_bundesliga, 
				'./dados/bundesliga/fbref/rodadas_liga.csv'],
	
	'Franca': [url_tabela_franca, './dados/franca/fbref/tabela_liga.csv', clubes_franca,'./dados/franca/fbref/rodadas_liga.csv'],

	'Italiano': [url_tabela_italiano, './dados/italiano/fbref/tabela_liga.csv', clubes_italiano, 
				'./dados/italiano/fbref/rodadas_liga.csv'],

	'La Liga': [url_tabela_la_liga, './dados/la_liga/fbref/tabela_liga.csv', clubes_la_liga,
			'./dados/la_liga/fbref/rodadas_liga.csv'],

	'Premier League': [url_tabela_premier_league, './dados/premier_league/fbref/tabela_liga.csv', clubes_premier_league,
					'./dados/premier_league/fbref/rodadas_liga.csv'],
					
	'Portugal': [url_tabela_portugal, './dados/portugal/fbref/tabela_liga.csv', clubes_portugal,
					'./dados/portugal/fbref/rodadas_liga.csv'],
					
	'Belgica': [url_tabela_belgica, './dados/belgica/fbref/tabela_liga.csv', clubes_belgica,
					'./dados/belgica/fbref/rodadas_liga.csv'],
					
	'Turquia': [url_tabela_turquia, './dados/turquia/fbref/tabela_liga.csv', clubes_turquia,
					'./dados/turquia/fbref/rodadas_liga.csv']}):
	'''
	--> Atualiza todas as ligas disponíveis
	'''
	for chave, valores in ligas.items():
		atualizacao_fbref = atualiza_dados_fbref(url_tabela_liga=ligas[chave][0], caminho_arquivo_tabela=ligas[chave][1], 
												clubes=ligas[chave][2], caminho_arquivo_rodadas=ligas[chave][3])
		atualizacao_fbref.atualizacao_dados()


#Comente a função para não executar
#atualiza_todas_ligas_fbref()
#------------------------------------------------------------------------------------------------------------

def atualizacao_dados_couk(url_variacao_liga={'Italia': '/I1.csv', 'Inglaterra': '/E0.csv', 'Alemanha': '/D1.csv', 
											'Espanha': '/SP1.csv', 'França': '/F1.csv', 'Portugal': '/P1.csv',
											'Turquia': '/T1.csv', 'Bélgica': '/B1.csv'}):
	'''
	--> Atualiza os dados coletados no site https://www.football-data.co.uk/

	:param url_variacao_liga: Dicionário contendo a identificação do país e a respectiva variação da URL na página com o arquivo de
	interessse
	'''
	for pais, liga in url_variacao_liga.items():
		if pais == 'Italia':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/italiano/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/italiano/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/italiano/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			#temporadas.temporada_atual()
			#temporadas.data_frame_temporadas()
		elif pais == 'Inglaterra':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/premier_league/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/premier_league/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/premier_league/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			#temporadas.temporada_atual()
			#temporadas.data_frame_temporadas()
		elif pais == 'Alemanha':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/bundesliga/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/bundesliga/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/bundesliga/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			#temporadas.temporada_atual()
			#temporadas.data_frame_temporadas()
		elif pais == 'Espanha':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/la_liga/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/la_liga/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/la_liga/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			#temporadas.temporada_atual()
			#temporadas.data_frame_temporadas()
		elif pais == 'França':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/franca/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/franca/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/franca/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			#temporadas.temporada_atual()
			#temporadas.data_frame_temporadas()	
		elif pais == 'Portugal':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/portugal/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/portugal/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/portugal/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			temporadas.temporada_atual()
			temporadas.data_frame_temporadas()
		elif pais == 'Turquia':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/turquia/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/turquia/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/turquia/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			temporadas.temporada_atual()
			temporadas.data_frame_temporadas()
		elif pais == 'Bélgica':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/belgica/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/belgica/couk/temporada_atual.csv',
										destino_arquivo_temporadas_baixadas='./dados/belgica/couk/temporadas_baixadas.csv')
			#temporadas.temporadas_anteriores()
			temporadas.temporada_atual()
			temporadas.data_frame_temporadas()

#Comente a função para não executar
atualizacao_dados_couk()