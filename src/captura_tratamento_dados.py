# Bibliotecas
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os.path

class CapturaDados:

    def __init__(self, clube=None, url_resultados=None, url_tipos_passes=None, url_escudo=None, 
                url_tabela_liga=None, tabela_rodadas=pd.DataFrame(), tabela_liga=pd.DataFrame()):
        '''
        --> Captura as informações para cálculo dos indicadores dos resultados do clube

        :param clube: Nome do clube para adicionar ao índice
        :param url_resultados: URL da tabela com as informações dos resultados das rodadas
        :param url_tipos_passes: URL com o número de escanteios por rodada
        :param url_escudo: URL com o endereço da imagem do escudo do clube
        :param url_tabela_liga: URL da tabela da liga
        :param tabela_rodadas: DataFrame pandas para agrupar todas as informações coletadas
        :param tabela_liga: DataFrame pandas com as informações da tabela da liga
        '''
        self.clube = clube
        self.url_resultados = url_resultados
        self.url_tipos_passes = url_tipos_passes
        self.url_escudo = url_escudo
        self.url_tabela_liga = url_tabela_liga
        self.tabela_rodadas = tabela_rodadas
        self.tabela_liga = tabela_liga
        
        
    def trata_url_resultados(self, indice='Rodada', colunas_desconsideradas=['Notas', 'Público', 
                                                                                  'Relatório da Partida', 
                                                                                  'Árbitro', 'Capitão', 
                                                                                  'Formação', 'xGA', 'xG', 
                                                                                  'Horário', 'Dia'],
                                  colunas_renomear={'GP': 'Gols Marcados', 'GC': 'Gols Soridos'}):
        '''
        --> Trata a tabela da liga para análise

        :param html: Variável que guarda o endereço html
        :param indice: Indice da tabela
        :param colunas_desconsideradas: Lista de colunas que não serão analidas
        :param colunas_renomear: Lista de colunas parar renomear

        return: Nova tabela com as informações para análise
        '''
        self.tabela_rodadas = pd.read_html(self.url_resultados)[0]
        self.tabela_rodadas[indice] = self.tabela_rodadas[indice].str[-2:]
        self.tabela_rodadas[indice] = self.tabela_rodadas[indice].astype('int32')
        self.tabela_rodadas.set_index(indice, inplace=True)
        self.tabela_rodadas.sort_index(ascending=False, inplace=True)
        self.tabela_rodadas.rename(colunas_renomear, axis=1, inplace=True)
        self.tabela_rodadas.drop(colunas_desconsideradas, axis=1, inplace=True)
        self.tabela_rodadas.dropna(inplace=True)


    def trata_url_tipos_passes(self, indice='Rodada', colunas_interesse=['In', 'Fora', 'Reto']):
        '''
        --> Adiciona o número de escanteios do jogo

        :param indice: Indice do DataFrame
        :param colunas_interesse: Colunas para cálculo do número de escanteios
        '''
        self.url_tipos_passes = pd.read_html(self.url_tipos_passes, skiprows=1, header=0)[0]
        self.url_tipos_passes.dropna(axis=0, inplace=True)
        self.url_tipos_passes.drop_duplicates(subset=['Rodada'], inplace=True)
        self.url_tipos_passes[indice] = self.url_tipos_passes[indice].str[-2:]
        self.url_tipos_passes[indice] = self.url_tipos_passes[indice].astype('int32')
        self.url_tipos_passes.set_index(indice, inplace=True)
        self.url_tipos_passes.sort_index(ascending=False, inplace=True)
        self.url_tipos_passes = pd.Series(data=self.url_tipos_passes[colunas_interesse].sum(axis=1), name='Escanteios')
        self.tabela_rodadas = self.tabela_rodadas.join(self.url_tipos_passes) 


    def trata_url_escudo(self):
        '''
        --> Retorna o endereço do escudo do time

        :param soup_1: Objeto soup da página html do time mandante
        :param soup_2: Objeto soup da página html do time visitante 

        return: Endereço da logo 
        '''
        response = urlopen(self.url_escudo)
        html = response.read().decode('UTF-8')
        html_limpo = ' '.join(html.split()).replace('> <', '><')
        soup = BeautifulSoup(html_limpo, 'html.parser')
        url_escudo = (soup.find('img', {'class': 'teamlogo'}).get('src'),)
        self.url_escudo = pd.DataFrame(url_escudo, index=[1])
        self.tabela_rodadas = pd.concat([self.tabela_rodadas, self.url_escudo], axis=1) 

    def resultados_clube(self):
        '''
        --> Adiciona o nome do clube ao multiIndex e renomeia as colunas do DataFrame
        '''
        self.clube = pd.Series(self.clube, name='clube', index=[1])
        self.tabela_rodadas = self.tabela_rodadas.join(self.clube)
        self.tabela_rodadas['clube'].fillna(method='ffill', inplace=True)
        self.tabela_rodadas.set_index('clube', append=True, inplace=True)
        self.tabela_rodadas.columns = ['data', 'local', 'resultado', 'gols_marcados', 'gols_sofridos',
                               'oponente', 'posse', 'escanteios', 'escudo']
        if os.path.exists('../dados/italiano_serie_a_20_21/rodadas_liga.csv'):
            self.tabela_rodadas.to_csv('../dados/italiano_serie_a_20_21/rodadas_liga.csv', mode='a', 
                                       header=False)
        else:
            self.tabela_rodadas.to_csv('../dados/italiano_serie_a_20_21/rodadas_liga.csv')

        
    def trata_tabela_liga(self, colunas_desconsideradas=['xG', 'xGA', 'xGD', 'xGD/90', 'Público', 
                                                         'Artilheiro da equipe', 'Goleiro', 'Notas'],
                          renomear_colunas= {'Cl': 'posicao', 'Equipe': 'equipe', 'MP': 'jogos', 
                                              'V': 'vitorias', 'E': 'empates', 'D': 'derrotas', 
                                              'GP': 'gols_marcados', 'GC': 'gols_sofridos',	
                                              'GD': 'saldo_gols', 'Pt': 'pontos', 
                                              'Últimos 5': 'ultimos_5'}):
        '''
        Leitura e limpeza da tabela da liga

        :param: 
        dicionario_colunas: Dicionário com a descrição da coluna padronizada
        colunas_desconsideradas: Lista de colunas que não serão analidas

        return: Nota tabela com as informações para análise
        '''
        self.url_tabela_liga = pd.read_html(self.url_tabela_liga)[0]
        self.url_tabela_liga.drop(colunas_desconsideradas, axis=1, inplace=True)
        self.url_tabela_liga.rename(renomear_colunas, axis=1, inplace=True)
        self.tabela_liga = self.url_tabela_liga
        self.tabela_liga.to_csv('../dados/italiano_serie_a_20_21/tabela_liga.csv', index=False)
