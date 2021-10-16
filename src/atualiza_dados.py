from captura_tratamento_dados import CapturaDadosFbref, CapturaDadosCoUk, GeraUrlFbref
import os.path


# Site de referência: https://fbref.com/pt/
# Urls das ligas por equipe


# Brasileiro Série A
url_tabela_brasileirao = 'https://fbref.com/pt/comps/24/Serie-A-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela_brasileirao, padrao_2_url_resultados='/2021/partidas/s10986/schedule/', 
						padrao_3_url_resultados='-Resultados-e-Calendarios-Serie-A')
url_clube.equipes_liga()
clubes_brasileirao = url_clube.gera_url()

# Atualizando dados
class atualiza_dados_fbref:
	'''
	--> Atualiza os dados coletados no site https://fbref.com/pt/
	'''
	def __init__(self, url_tabela_liga=None, caminho_arquivo_tabela=None, clubes=None, 
				caminho_arquivo_rodadas=None, classe_captura=CapturaDadosFbref):
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
	'Brasileiro': [url_tabela_brasileirao, './dados/brasileirao/fbref/tabela_liga.csv', clubes_brasileirao, 
				'./dados/brasileirao/fbref/rodadas_liga.csv']}):
	'''
	--> Atualiza todas as ligas disponíveis
	'''
	for chave, valores in ligas.items():
		atualizacao_fbref = atualiza_dados_fbref(url_tabela_liga=ligas[chave][0], caminho_arquivo_tabela=ligas[chave][1], 
												clubes=ligas[chave][2], caminho_arquivo_rodadas=ligas[chave][3])
		atualizacao_fbref.atualizacao_dados()


#Comente a função para não executar
atualiza_todas_ligas_fbref()
#------------------------------------------------------------------------------------------------------------

def atualizacao_dados_couk(url_variacao_liga={'Brasil': '/BRA.csv'}):
	'''
	--> Atualiza os dados coletados no site https://www.football-data.co.uk/

	:param url_variacao_liga: Dicionário contendo a identificação do país e a respectiva variação da URL na página com o arquivo de
	interessse
	'''
	for pais, liga in url_variacao_liga.items():
		if pais == 'Brasil':
			temporadas = CapturaDadosCoUk(liga, destino_arquivo_temporadas_anteriores='./dados/brasileirao/couk/temporadas_anteriores.csv', 
										destino_arquivo_temporada_atual='./dados/brasileirao/couk/temporada_atual.csv',
										destino_arquivo_temporadas_disponiveis='./dados/brasileirao/couk/temporadas_baixadas.csv')
			temporadas.temporadas_disponiveis()
#Comente a função para não executar
atualizacao_dados_couk()
