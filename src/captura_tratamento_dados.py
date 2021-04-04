# Bibliotecas
import pandas as pd
import numpy as np
from urllib.request import urlopen
import streamlit as st
from bs4 import BeautifulSoup
import os.path
import requests


class CapturaDadosFbref:
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
        :param clube_escudo: DataFrame contendo os clubes da liga e o respectivo link com a imagem do escudo
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
        self.url_cartoes['cartoes_total'] = self.url_cartoes['cartoes_amarelos'] + self.url_cartoes['cartoes_vermelhos'] 
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
                                       header=False, index=False)
        else:
            self.tabela_rodadas.to_csv(self.caminho_arquivo_rodadas, index=False)

        
    def trata_tabela_liga(self, colunas_selecionadas=['Cl', 'Equipe', 'MP', 'V', 'E', 'D', 'GP', 'GC',
    	                                            'GD', 'Pt', 'Últimos 5']):
        '''
        Leitura e limpeza da tabela da liga

        :param colunas_selecionadas: Colunas da tabela selecionadas

        return: Tabela da liga com as informações para análise
        '''
        self.url_tabela_liga = pd.read_html(self.url_tabela_liga)[0]
        self.url_tabela_liga = self.url_tabela_liga[colunas_selecionadas]
        self.url_tabela_liga.columns = ['posicao', 'equipe', 'n_jogos', 'vitorias', 'empates', 'derrotas', 'gols_marcados', 
                                        'gols_sofridos', 'saldo_gols', 'pontos', 'ultimos_5']
        self.tabela_liga = self.url_tabela_liga
        self.tabela_liga.to_csv(self.caminho_arquivo_tabela, index=False)


class CapturaDadosCoUk:
    '''
    Baixa os arquivos do site https://www.football-data.co.uk e agrupa em um DataFrame pandas.
    '''
    def __init__(self, url_variacao_liga=None, destino_arquivo_temporadas_anteriores=None, temporada_atual=None, 
                destino_arquivo_temporada_atual=None, destino_arquivo_temporadas_baixadas=None,
                url_variacao_temporadas_anteriores=['1920', '1819', '1718', '1617', '1516'],
                url_variacao_temporada_atual='2021', colunas_selecionadas=['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 
                                                                        'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST', 'HC', 'AC', 
                                                                        'HF', 'AF', 'HY', 'AY', 'HR', 'AR'], 
                renomear_colunas=['data', 'mandante', 'visitante', 'gols_mandante_partida', 'gols_visitante_partida', 'resultado', 
                                'gols_mandante_primeiro_tempo', 'gols_visitante_primeiro_tempo', 'resultado_primeiro_tempo', 
                                'chutes_mandante', 'chutes_visitante', 'chutes_no_gol_mandante', 'chutes_no_gol_visitante', 
                                'escanteios_mandante', 'escanteios_visitante', 'faltas_cometidas_mandante', 
                                'faltas_cometidas_visitante', 'cartoes_amarelos_mandante', 'cartoes_amarelos_visitante', 
                                'cartoes_vermelhos_mandante', 'cartoes_vermelhos_visitante'],
                renomear_clubes = [['Verona', 'Man City', 'Sheffield United', 'Leicester', 'Man United', 'Newcastle', 'Leeds', 
                                    'Ein Frankfurt', 'FC Koln', "M'gladbach", 'Mainz', 'Hertha', 'Ath Bilbao', 'Alaves', 'Celta', 
                                    'Sociedad', 'Cadiz', 'Ath Madrid', 'Paris SG', 'St Etienne', 'Nimes'], ['Hellas Verona', 
                                    'Manchester City', 'Sheffield Utd', 'Leicester City','Manchester Utd', 'Newcastle Utd', 
                                    'Leeds United', 'Eint Frankfurt', 'Köln', "M'Gladbach", 'Mainz 05', 'Hertha BSC', 
                                    'Athletic Club', 'Alavés', 'Celta Vigo', 'Real Sociedad', 'Cádiz', 'Atlético Madrid', 
                                    'Paris S-G', 'Saint-Étienne', 'Nîmes']],
                url_modelo='https://www.football-data.co.uk/mmz4281/'):
        '''    
        :param url_variacao_liga: Variação da url que identifica a liga no site
        :param destino_arquivo_temporadas_anteriores: Arquivo que irá receber os dados das temporadas anteriores
        :param temporada_atual: Data Frame com os dados da temporada atual
        :param destino_arquivo_temporada_atual: Arquivo que irá receber os dados da temporada atual
        :param colunas_selecionadas: Colunas selecionadas para análise
        :param renomear_colunas: Lista com a nova descrição das colunas
        :param destino_arquivo_temporadas_baixadas: Arquivo que irá receber os arquivo das temporadas anteriores e atual
        :param url_variacao_temporadas_anteriores: Variação na url que identifica as temporadas anteriores no site
        :param url_variacao_temporada_atual: Variação na url que identifica a temporada atual no site
        :param renomear_clubes: Lista contendo duas lista, onde o index 0 são os nomes atuais e o index 1 os nomes alterados
        :param url_modelo: Parte da url que não sofre alteração na identificação de todas as temporadas
        '''
        self._url_variacao_liga = url_variacao_liga
        self._destino_arquivo_temporadas_anteriores = destino_arquivo_temporadas_anteriores
        self._temporada_atual = temporada_atual
        self._colunas_selecionadas = colunas_selecionadas
        self._renomear_colunas = renomear_colunas
        self._destino_arquivo_temporada_atual = destino_arquivo_temporada_atual
        self._destino_arquivo_temporadas_baixadas = destino_arquivo_temporadas_baixadas
        self._url_variacao_temporadas_anteriores = url_variacao_temporadas_anteriores
        self._url_variacao_temporada_atual = url_variacao_temporada_atual
        self._renomear_clubes = renomear_clubes
        self._url_modelo = url_modelo

    
    def temporadas_anteriores(self):
        '''
        --> Captura o histórico da liga no site https://www.football-data.co.uk/ e salva na pasta 
        correspondente
        '''
        temporadas_anteriores = pd.DataFrame()
        for temporada in self._url_variacao_temporadas_anteriores:
            r = requests.get(self._url_modelo + temporada + self._url_variacao_liga)
            with open(self._destino_arquivo_temporadas_anteriores, 'wb') as code:
                code.write(r.content)
            temporadas_anteriores_temp = pd.read_csv(self._destino_arquivo_temporadas_anteriores)
            temporadas_anteriores_temp = temporadas_anteriores_temp[self._colunas_selecionadas]
            temporadas_anteriores_temp.columns = self._renomear_colunas
            temporadas_anteriores = temporadas_anteriores.append(temporadas_anteriores_temp, ignore_index=True)
        os.remove(self._destino_arquivo_temporadas_anteriores)
        temporadas_anteriores['escanteios_partida'] = temporadas_anteriores[['escanteios_mandante', 
                                                                            'escanteios_visitante']].sum(axis=1)
        temporadas_anteriores['gols_partida'] = temporadas_anteriores[['gols_mandante_partida', 
                                                                        'gols_visitante_partida']].sum(axis=1)
        temporadas_anteriores['total_cartões_mandante'] = temporadas_anteriores[['cartoes_amarelos_mandante',
                                                                                'cartoes_vermelhos_mandante',]].sum(axis=1)
        temporadas_anteriores['total_cartões_visitante'] = temporadas_anteriores[['cartoes_amarelos_visitante',
                                                                                'cartoes_vermelhos_visitante']].sum(axis=1)                                                               
        temporadas_anteriores['total_cartoes_partida'] = temporadas_anteriores[['cartoes_amarelos_mandante',
                                                                                'cartoes_amarelos_visitante',
                                                                                'cartoes_vermelhos_mandante',
                                                                                'cartoes_vermelhos_visitante']].sum(axis=1)
        temporadas_anteriores['resultado'] = temporadas_anteriores['resultado'].map({'H': 'Vitória Mandante', 'D': 'Empate', 'A': 'Vitória Visitante'})
        temporadas_anteriores['data'] = pd.to_datetime(temporadas_anteriores['data'])
        temporadas_anteriores.sort_values('data', ascending=False, inplace=True)
        temporadas_anteriores.to_csv(self._destino_arquivo_temporadas_anteriores, index=False)


    def temporada_atual(self):
        '''
        --> Captura o histórico da liga  atual no site https://www.football-data.co.uk/ e salva na pasta 
        correspondente
        '''
        r = requests.get(self._url_modelo + self._url_variacao_temporada_atual + self._url_variacao_liga)
        with open(self._destino_arquivo_temporada_atual, 'wb') as code:
            code.write(r.content)
        self._temporada_atual = pd.read_csv(self._destino_arquivo_temporada_atual)
        self._temporada_atual = self._temporada_atual[self._colunas_selecionadas]
        self._temporada_atual.columns = self._renomear_colunas
        self._temporada_atual['escanteios_partida'] = self._temporada_atual[['escanteios_mandante', 
                                                                            'escanteios_visitante']].sum(axis=1)
        self._temporada_atual['gols_partida'] = self._temporada_atual[['gols_mandante_partida', 
                                                                    'gols_visitante_partida']].sum(axis=1)
        self._temporada_atual['total_cartões_mandante'] = self._temporada_atual[['cartoes_amarelos_mandante',
                                                                                'cartoes_vermelhos_mandante',]].sum(axis=1)
        self._temporada_atual['total_cartões_visitante'] = self._temporada_atual[['cartoes_amarelos_visitante',
                                                                                'cartoes_vermelhos_visitante']].sum(axis=1)                                                               
        self._temporada_atual['total_cartoes_partida'] = self._temporada_atual[['cartoes_amarelos_mandante','cartoes_amarelos_visitante',
                                                                        'cartoes_vermelhos_mandante',
                                                                        'cartoes_vermelhos_visitante']].sum(axis=1)
        self._temporada_atual['resultado'] = self._temporada_atual['resultado'].map({'H': 'Vitória Mandante', 'D': 'Empate', 
                                                                                    'A': 'Vitória Visitante'})
        self._temporada_atual['data'] = pd.to_datetime(self._temporada_atual['data'])
        self._temporada_atual.sort_values('data', ascending=False, inplace=True) 
        self._temporada_atual = self._temporada_atual.replace(self._renomear_clubes[0], self._renomear_clubes[1])
        os.remove(self._destino_arquivo_temporada_atual)
        self._temporada_atual.to_csv(self._destino_arquivo_temporada_atual, index=False)


    def data_frame_temporadas(self):
        '''
        --> Gera um dataframe pandas com os arquivos das temporadas anteriores e da atual baixadas
        '''
        todas_temporadas_baixadas = pd.concat([self._temporada_atual, pd.read_csv(self._destino_arquivo_temporadas_anteriores)])
        todas_temporadas_baixadas = todas_temporadas_baixadas.replace(self._renomear_clubes[0], self._renomear_clubes[1])
        todas_temporadas_baixadas['data'] = pd.to_datetime(todas_temporadas_baixadas['data'])
        todas_temporadas_baixadas.sort_values('data', ascending=False, inplace=True)
        todas_temporadas_baixadas.to_csv(self._destino_arquivo_temporadas_baixadas, index=False)
        

def leitura_dados_fbref(caminho_rodadas: str, caminho_tabela: str):
    '''
    --> Realiza a leitura das rodadas e da tabela da liga

    :param caminho_rodadas: Caminho do arquivo referente as rodadas da liga
    :param caminho_tabela: Caminho do arquivo referente a tabela da liga

    return rodadas, tabela
    '''
    rodadas = pd.read_csv(caminho_rodadas)
    tabela = pd.read_csv(caminho_tabela)
    return rodadas, tabela
