# Bibliotecas
import pandas as pd
from urllib.request import urlopen
import streamlit as st
from bs4 import BeautifulSoup
import os.path

class CapturaDados:
    '''
    --> Captura as informações no site https://fbref.com/ e trata as páginas e informações de
    interesse para análise estatística
    '''

    def __init__(self, clube=None, url_resultados=None, caminho_arquivo_rodadas=None, 
                url_tabela_liga=None, caminho_arquivo_tabela=None, url_tipos_passes=None, 
                url_passes=None, url_chutes=None, url_escudo=None, tabela_rodadas=pd.DataFrame(), 
                tabela_liga=pd.DataFrame()):
        '''
        --> Captura as informações para cálculo dos indicadores dos resultados do clube

        :param clube: Nome do clube para adicionar ao índice
        :param url_resultados: URL da tabela com as informações dos resultados das rodadas
        :param caminho_arquivo_rodadas: Local para gerar o arquivo csv referente as rodadas
        :param url_tabela_liga: URL da tabela da liga
        :param caminho_arquivo_tabela: Local para salvar o arquivo da tabela da liga
        :param url_tipos_passes: URL com o número de escanteios por rodada
        :param url_passes: URL com o percentual de passes certos
        :para url_chutes: URL com o percentual de chutes
        :param url_escudo: URL com o endereço da imagem do escudo do clube
        :param tabela_rodadas: DataFrame pandas para agrupar todas as informações coletadas
        :param tabela_liga: DataFrame pandas com as informações da tabela da liga
        '''
        self.clube = clube
        self.url_resultados = url_resultados
        self.url_tipos_passes = url_tipos_passes
        self.url_passes = url_passes
        self.url_chutes = url_chutes
        self.url_escudo = url_escudo
        self.url_tabela_liga = url_tabela_liga
        self.caminho_arquivo_rodadas = caminho_arquivo_rodadas
        self.caminho_arquivo_tabela = caminho_arquivo_tabela
        self.tabela_rodadas = tabela_rodadas
        self.tabela_liga = tabela_liga
        
        
    def trata_url_resultados(self, indice='Rodada', colunas_desconsideradas=['Notas', 'Público', 
                                                                            'Relatório da Partida', 
                                                                            'Árbitro', 'Capitão', 
                                                                            'Formação', 'xGA', 'xG', 
                                                                            'Horário', 'Dia']):
        '''
        --> Captura os resultados das rodadas por equipe e seleciona as colunas de interesse para
        análise, adicionando o número de gols da partida, gols marcados e sofridos

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
        self.tabela_rodadas.drop(colunas_desconsideradas, axis=1, inplace=True)
        self.tabela_rodadas.dropna(inplace=True)
        self.tabela_rodadas['gols_partida'] = self.tabela_rodadas['GP'] + self.tabela_rodadas['GC']


    def trata_url_tipos_passes(self, indice='Rodada', colunas_interesse='CK'):
        '''
        --> Adiciona o número de escanteios do jogo a tabela com os resultados por rodada

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
        self.url_tipos_passes = pd.Series(data=self.url_tipos_passes[colunas_interesse], name='Escanteios')
        self.tabela_rodadas = self.tabela_rodadas.join(self.url_tipos_passes) 


    def trata_url_passes(self, indice='Rodada', colunas_interesse='Cmp%'):
        '''
        --> Adiciona o percentual de passes certos a tabela de resultados por rodada

        :param indice: Indice do DataFrame
        :param colunas_interesse: Coluna com o percentual de passes certos
        '''
        self.url_passes = pd.read_html(self.url_passes, skiprows=1, header=0)[0]
        self.url_passes.dropna(axis=0, inplace=True)
        self.url_passes.drop_duplicates(subset=['Rodada'], inplace=True)
        self.url_passes[indice] = self.url_passes[indice].str[-2:]
        self.url_passes[indice] = self.url_passes[indice].astype('int32')
        self.url_passes.set_index(indice, inplace=True)
        self.url_passes.sort_index(ascending=False, inplace=True)
        self.url_passes = pd.Series(data=self.url_passes[colunas_interesse], name='Passes')
        self.url_passes = self.url_passes / 10
        self.tabela_rodadas = self.tabela_rodadas.join(self.url_passes)


    def trata_url_chutes(self, indice='Rodada', colunas_interesse=['TC', 'CaG', 'SoT%', 'G/SoT']):
        '''
        --> Adiciona o percentual de chutes a tabela de resultados por rodada

        :param indice: Indice do DataFrame
        :param colunas_interesse: Coluna com o percentual de passes certos
        '''
        self.url_chutes = pd.read_html(self.url_chutes, skiprows=1, header=0)[0]
        self.url_chutes.dropna(axis=0, inplace=True)
        self.url_chutes.drop_duplicates(subset=['Rodada'], inplace=True)
        self.url_chutes[indice] = self.url_chutes[indice].str[-2:]
        self.url_chutes[indice] = self.url_chutes[indice].astype('int32')
        self.url_chutes.set_index(indice, inplace=True)
        self.url_chutes.sort_index(ascending=False, inplace=True)
        self.url_chutes = pd.DataFrame(data=self.url_chutes[colunas_interesse])
        self.url_chutes['SoT%'] = self.url_chutes['SoT%'] / 10
        self.tabela_rodadas = self.tabela_rodadas.join(self.url_chutes) 


    def trata_url_escudo(self):
        '''
        --> Retorna o endereço web do escudo do time e adiciona a tabela de rodadas

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
        --> Adiciona o nome do clube ao multiIndex e renomeia as colunas do DataFrame final para
        análise das rodadas e gera o arquivo csv
        '''
        self.clube = pd.Series(self.clube, name='clube', index=[1])
        self.tabela_rodadas = self.tabela_rodadas.join(self.clube)
        self.tabela_rodadas['clube'].fillna(method='ffill', inplace=True)
        self.tabela_rodadas.set_index('clube', append=True, inplace=True)
        self.tabela_rodadas.columns = ['data', 'local', 'resultado', 'gols_marcados', 'gols_sofridos',
                                        'oponente', 'posse', 'gols_partida', 'escanteios', 'passes_certos_%', 
                                        'total_chutes', 'chutes_a_gol', 'chutes_ao_gol_%', 
                                        'gols_por_chute_ao_gol_%', 'escudo']
        self.tabela_rodadas['escudo'].fillna(method='ffill', inplace=True)
        if os.path.exists(self.caminho_arquivo_rodadas):
            self.tabela_rodadas.to_csv(self.caminho_arquivo_rodadas, mode='a', 
                                       header=False)
        else:
            self.tabela_rodadas.to_csv(self.caminho_arquivo_rodadas)

        
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
        self.tabela_liga.to_csv(self.caminho_arquivo_tabela, index=False)


@st.cache
def leitura_ordenacao_indice(caminho_rodadas: str, caminho_tabela: str):
    '''
    --> Realiza a leitura das rodadas e da tabela e ordena as rodadas pela partida mais recente

    :param caminho_rodadas: Caminho do arquivo referente as rodadas da liga
    :param caminho_tabela: Caminho do arquivo referente a tabela da liga

    return rodadas, tabela
    '''
    rodadas = pd.read_csv(caminho_rodadas)
    rodadas.rename({'Unnamed: 0': 'rodada'}, axis=1, inplace=True)
    rodadas['data'] = pd.to_datetime(rodadas['data'])
    rodadas.sort_values('data', ascending=False, inplace=True)
    tabela = pd.read_csv(caminho_tabela)
    return rodadas, tabela


@st.cache
def localiza_adiciona_url(clubes: dict(), url_modelo: int, variacao_url: list(),
                        url_padrao_inicio=64, url_padrao_fim=77):
    '''
    --> Gerar o endereço html repetindo as informações padrão do html modelo e alterando a
    variação da URL de interesse

    :param clubes: Dicionário com o nome do clube e a url modelo para adicionar as 
    novas urls
    :param url_modelo: ìndice da url modelo salva no dicionário
    :param url_variacao: Variação da url para localizar a página de interesse
    :url_padrao_inicio: Informação que se repete no início da URL
    :url_padrao_fim: Informação que se repete no fim da URL
    '''
    for clube in clubes.keys():
        for url in variacao_url:
            clubes[clube].append(clubes[clube][url_modelo][:url_padrao_inicio] + url + clubes[clube][url_modelo][url_padrao_fim:])
