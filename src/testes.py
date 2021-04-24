from captura_tratamento_dados import GeraUrlFbref

url_tabela = 'https://fbref.com/pt/comps/37/Belgian-First-Division-A-Estatisticas'
url_clube = GeraUrlFbref(url_tabela_liga=url_tabela, padrao_2_url_resultados='/2020-2021/partidas/s10740/schedule/',
						padrao_3_url_resultados='-Resultados-e-Calendarios-Super-Lig')
url_clube.equipes_liga()
clubes = url_clube.gera_url()