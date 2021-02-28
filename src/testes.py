from captura_tratamento_dados import CapturaDados

url_resultados = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A'
url_tipos_passes = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/passing_types/Internazionale-Historicos-dos-Jogos-Serie-A'
url_escudo = 'https://fbref.com/pt/equipes/d609edc0/2020-2021/partidas/s10730/schedule/Internazionale-Resultados-e-Calendarios-Serie-A'

def testa_captura_dados(classe=CapturaDados('Inter', url_resultados, url_tipos_passes, url_escudo), 
                        url_resultados=url_resultados, url_tipos_passes=url_tipos_passes, 
                        url_escudo=url_escudo):

                        dados = classe
                        dados.trata_url_resultados()
                        dados.trata_url_tipos_passes()
                        dados.trata_url_escudo()
                        dados.resultados_clube()
                        return dados.tabela
