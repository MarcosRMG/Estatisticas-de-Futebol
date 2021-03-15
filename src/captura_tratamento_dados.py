# Bibliotecas
import pandas as pd
import numpy as np
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
                url_passes=None, url_chutes=None, url_cartoes=None, url_goleiro=None, url_escudo=None, 
                tabela_rodadas=pd.DataFrame(), tabela_liga=pd.DataFrame()):
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
        self.url_cartoes = url_cartoes
        self.url_goleiro = url_goleiro
        self.url_escudo = url_escudo
        self.url_tabela_liga = url_tabela_liga
        self.caminho_arquivo_rodadas = caminho_arquivo_rodadas
        self.caminho_arquivo_tabela = caminho_arquivo_tabela
        self.tabela_rodadas = tabela_rodadas
        self.tabela_liga = tabela_liga
        
        
    def trata_url_resultados(self, colunas_selecionadas=['Data', 'Rodada', 'Local', 'Resultado', 'GP', 
                                                    'GC', 'Oponente', 'Posse']):
        '''
        --> Captura os resultados das rodadas por equipe e seleciona as colunas de interesse para
        análise, adicionando o número de gols da partida, gols marcados e sofridos

        :param colunas_selecionadas: Lista de colunas selecionadas

        return: Nova tabela com as informações para análise
        '''
        self.tabela_rodadas = pd.read_html(self.url_resultados)[0]
        self.tabela_rodadas = self.tabela_rodadas[colunas_selecionadas]
        self.tabela_rodadas.columns = ['data', 'rodada', 'local', 'resultado', 'gols_marcados', 
                                        'gols_sofridos', 'oponente', 'posse']
        self.tabela_rodadas = self.tabela_rodadas[self.tabela_rodadas['resultado'].isna() == False] 
        self.tabela_rodadas['rodada'] = self.tabela_rodadas['rodada'].str[-2:]
        self.tabela_rodadas['data'] = pd.to_datetime(self.tabela_rodadas['data'])
        self.tabela_rodadas.set_index('data', inplace=True)
        self.tabela_rodadas.sort_index(ascending=False, inplace=True)
        self.tabela_rodadas['gols_partida'] = self.tabela_rodadas['gols_marcados'] + self.tabela_rodadas['gols_sofridos']


    def trata_url_tipos_passes(self, colunas_selecionadas=['Data', 'CK']):
        '''
        --> Adiciona o número de escanteios do jogo a tabela com os resultados por rodada

        :param colunas_selecionadas: Colunas para cálculo do número de escanteios
        '''
        self.url_tipos_passes = pd.read_html(self.url_tipos_passes, skiprows=1, header=0)[0]
        self.url_tipos_passes = self.url_tipos_passes[colunas_selecionadas]
        self.url_tipos_passes.columns = ['data', 'escanteios']
        self.url_tipos_passes.dropna(inplace=True)
        self.url_tipos_passes['data'] = pd.to_datetime(self.url_tipos_passes['data'])
        self.url_tipos_passes.set_index('data', inplace=True)
        self.url_tipos_passes.sort_index(ascending=False, inplace=True)
        self.tabela_rodadas = self.tabela_rodadas.merge(self.url_tipos_passes, right_index=True,
                                                        left_index=True, validate='1:1') 


    def trata_url_passes(self, colunas_selecionadas=['Data', 'Cmp%']):
        '''
        --> Adiciona o percentual de passes certos a tabela de resultados por rodada

        :param colunas_selecionadas: Coluna com o percentual de passes certos
        '''
        self.url_passes = pd.read_html(self.url_passes, skiprows=1, header=0)[0]
        self.url_passes = self.url_passes[colunas_selecionadas]
        self.url_passes.columns = ['data', 'passes_certos_%']
        self.url_passes.dropna(inplace=True)
        self.url_passes['passes_certos_%'] = self.url_passes['passes_certos_%'] / 10
        self.url_passes['data'] = pd.to_datetime(self.url_passes['data'])
        self.url_passes.set_index('data', inplace=True)
        self.url_passes.sort_index(ascending=False, inplace=True)
        self.tabela_rodadas = self.tabela_rodadas.merge(self.url_passes, right_index=True, left_index=True,
                                                    validate='1:1')


    def trata_url_chutes(self, colunas_selecionadas=['Data', 'TC', 'SoT%']):
        '''
        --> Adiciona o percentual de chutes a tabela de resultados por rodada

        :param colunas_selecionadas: Colunas referente aos chutes
        '''
        self.url_chutes = pd.read_html(self.url_chutes, skiprows=1, header=0)[0]
        self.url_chutes = self.url_chutes[colunas_selecionadas]
        self.url_chutes.columns = ['data', 'total_chutes', 'chutes_a_gol_%']
        self.url_chutes.dropna(inplace=True)
        self.url_chutes['data'] =  pd.to_datetime(self.url_chutes['data'])
        self.url_chutes.set_index('data', inplace=True)
        self.url_chutes.sort_index(ascending=False, inplace=True)
        self.url_chutes['chutes_por_gol'] = self.url_chutes['total_chutes'] / self.tabela_rodadas['gols_marcados']
        self.url_chutes['chutes_por_gol'].replace([np.inf, -np.inf], 0, inplace=True)
        self.url_chutes['chutes_a_gol_%'] = self.url_chutes['chutes_a_gol_%'] / 10
        self.tabela_rodadas = self.tabela_rodadas.merge(self.url_chutes, right_index=True, left_index=True,
                                                        validate='1:1') 

    
    def trata_url_cartoes(self, colunas_selecionadas=['Data', 'CrtsA', 'CrtV', 'Fts']):
        '''
        --> Adiciona o número de cartões amarelos e vermelho no jogo

        :param colunas_selecionadas: Colunas com o número de cartões no jogo
        '''
        self.url_cartoes = pd.read_html(self.url_cartoes, skiprows=1, header=0)[0]
        self.url_cartoes = self.url_cartoes[colunas_selecionadas]
        self.url_cartoes.columns = ['data', 'cartoes_amarelos', 'cartoes_vermelhos', 'faltas_cometidas']
        self.url_cartoes.dropna(axis=0, inplace=True)
        self.url_cartoes['data'] = pd.to_datetime(self.url_cartoes['data'])
        self.url_cartoes.set_index('data', inplace=True)
        self.url_cartoes.sort_index(ascending=False, inplace=True)
        self.tabela_rodadas = self.tabela_rodadas.merge(self.url_cartoes, right_index=True, left_index=True,
                                                validate='1:1') 


    def trata_url_goleiro(self, colunas_selecionadas=['Data', 'CaGC', '%Defesas', 'SV']):
        '''
        --> Adiciona o número de defesas no jogo

        :param colunas_selecionadas: Colunas com o número de cartões no jogo
        '''
        self.url_goleiro = pd.read_html(self.url_goleiro, skiprows=1, header=0)[0]
        self.url_goleiro = self.url_goleiro[colunas_selecionadas]
        self.url_goleiro.columns = ['data', 'chutes_contra_o_gol', 'defesas_%', 'sem_vazamento']
        self.url_goleiro['data'] = pd.to_datetime(self.url_goleiro['data'])
        self.url_goleiro.set_index('data', inplace=True)
        self.url_goleiro.sort_index(ascending=False, inplace=True)
        self.url_goleiro['defesas_%'] = self.url_goleiro['defesas_%'] / 10 
        self.tabela_rodadas = self.tabela_rodadas.merge(self.url_goleiro, right_index=True, left_index=True,
                                                        validate='1:1') 


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
        self.url_escudo = pd.Series(soup.find('img', {'class': 'teamlogo'}).get('src'), name='escudo')
        self.tabela_rodadas.reset_index(inplace=True)
        self.tabela_rodadas = self.tabela_rodadas.join(self.url_escudo)


    def resultados_clube(self):
        '''
        --> Adiciona o nome do clube a tabela e gera o arquivo csv com o resultado dos jogos
        '''
        self.clube = pd.Series(self.clube, name='clube')
        self.tabela_rodadas = pd.concat([self.clube, self.tabela_rodadas], axis=1)
        self.tabela_rodadas['clube'].fillna(method='ffill', inplace=True)
        if os.path.exists(self.caminho_arquivo_rodadas):
            self.tabela_rodadas.to_csv(self.caminho_arquivo_rodadas, mode='a', 
                                       header=False)
        else:
            self.tabela_rodadas.to_csv(self.caminho_arquivo_rodadas)

        
    def trata_tabela_liga(self, colunas_selecionadas=['Cl', 'Equipe', 'MP', 'V', 'E', 'D', 'GP', 'GC',
    	                                            'GD', 'Pt', 'Últimos 5']):
        '''
        Leitura e limpeza da tabela da liga

        :param colunas_selecionadas: Colunas da tabela selecionadas

        return: Tabela da liga com as informações para análise
        '''
        self.url_tabela_liga = pd.read_html(self.url_tabela_liga)[0]
        self.url_tabela_liga = self.url_tabela_liga[colunas_selecionadas]
        self.url_tabela_liga.columns = ['Posição', 'Equipe', 'Nº Jogos', 'Vitórias', 'Empates',
                                        'Derrotas', 'Gols Marcados', 'Gols Sofridos', 'Saldo de Gols',
                                        'Pontos', 'Últimos 5']
        self.tabela_liga = self.url_tabela_liga
        self.tabela_liga.to_csv(self.caminho_arquivo_tabela, index=False)


def leitura_ordenacao_indice(caminho_rodadas: str, caminho_tabela: str):
    '''
    --> Realiza a leitura das rodadas e da tabela e ordena as rodadas pela partida mais recente

    :param caminho_rodadas: Caminho do arquivo referente as rodadas da liga
    :param caminho_tabela: Caminho do arquivo referente a tabela da liga

    return rodadas, tabela
    '''
    rodadas = pd.read_csv(caminho_rodadas)
    rodadas.drop('Unnamed: 0', axis=1, inplace=True)
    tabela = pd.read_csv(caminho_tabela)
    return rodadas, tabela


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
