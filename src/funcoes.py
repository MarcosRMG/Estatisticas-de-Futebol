def trata_tabela_rodadas_liga(html: str, dicionario_colunas=colunas_2, indice='rodada',
                      colunas_desconsideradas=['notas', 'publico', 
                                               'relatorio_partida', 'arbitro',
                                               'capitao', 'formacao', 'xga', 'xg',
                                               'horario', 'dia', 'data']):
  '''
  --> Trata a tabela da liga para análise

  :param html: Variável que guarda o endereço html
  :param dicionario_colunas: Dicionário com a descrição da coluna padronizada
  :param indice: Indice da tabela
  :param colunas_desconsideradas: Lista de colunas que não serão analidas

  return: Nota tabela com as informações para análise
  '''
  rodadas = pd.read_html(html)[0]
  rodadas.rename(dicionario_colunas, axis=1, inplace=True)
  rodadas[indice] = rodadas[indice].str[-2:]
  rodadas[indice] = rodadas[indice].astype('int32')
  rodadas.set_index(indice, inplace=True)
  rodadas.sort_index(ascending=False, inplace=True)
  rodadas.drop(colunas_desconsideradas, axis=1, 
                              inplace=True)
  rodadas.dropna(inplace=True)
  return rodadas


def binariza_coluna(dados: pd.DataFrame, colunas: list()):
  '''
  --> Realiza a binarização da coluna

  :param dados: DataFrame com as informações para binarização
  :param colunas: Lista de colunas a ser binarizada

  return Dados binarizados para atribuição excluíndo se a coluna antiga
  '''
  dados = dados.join(pd.get_dummies(dados[colunas]))
  dados.drop(colunas, axis=1, inplace=True)
  dados.rename({'local_Visitante': 'visitante', 'local_Em casa': 'em_casa', 
                'resultado_E': 'empate', 'resultado_D': 'derrota', 
                'resultado_V': 'vitoria'}, axis=1, inplace=True)
  return dados  


def ler_dados(caminho: str):
    '''
    --> Faz a leitura do arquivo csv

    Keywords arguments
    :param caminho: Endereço do arquivo csv

    return DataFrame com as informações do arquivo csv 
    '''
    return pd.read_csv(caminho)

def histograma(dados: pd.DataFrame, coluna: str, titulo: str):
    '''
    --> Mostra o histograma da variável selecionada
    
    :param dados: DataFrame pandas com os dados
    :param coluna: Série pandas da variável específica
    :param titulo: Título do gráfico

    return Histograma 
    '''
    fig, ax = plt.subplots()
    ax = dados[coluna].plot(kind='hist')
    ax.set_title(titulo, loc='left', fontsize=24)
    return fig