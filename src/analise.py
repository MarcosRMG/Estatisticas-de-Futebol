import pandas as pd
import streamlit as st
import plotly_express as px
import pickle


class Indicadores:
    '''
    --> Calcula os indicadores para visualização
    '''
    def __init__(self, dados=None, clube=None, local_jogo=None, ultimos_jogos=None):
        '''
        :param dados: DataFrame contendo os registros dos jogos
        :param clube: Clube selecionado pelo usuário
        :local_jogo: Se o clube é mandante, visitante ou dados tanto como mandante e visitante
        :ultimos_jogos: Seleção do número de jogos anteriores
        '''
        self.dados = dados
        self.clube = clube
        self.local_jogo = local_jogo
        self.ultimos_jogos = ultimos_jogos

    
    def indicador_resultados(self):
        '''
        --> Últimos cinco resultados e previsão do próximo resultado
        '''
        resultados_partidas = self.dados.query('clube == @self.clube and local == @self.local_jogo')['resultado'][:self.ultimos_jogos].values
        resultados_partidas_list = self.dados.query('clube == @self.clube and local == @self.local_jogo')['resultado'][:5].values
        resultados_partidas_str = str()
        for i in range(len(resultados_partidas_list)):
            if i == 0:
                resultados_partidas_str = str(resultados_partidas_list[i])
            else:
                resultados_partidas_str = resultados_partidas_str + ' - ' + str(resultados_partidas_list[i])
        st.markdown('**ÚLTIMOS RESULTADOS**')
        st.markdown(resultados_partidas_str[::-1])

        # Probabilidades para o resultado
        st.markdown('**PROBABILIDADES**')
        fig = px.histogram(y=resultados_partidas, histnorm='probability density', cumulative=False, width=400, height=600)
        fig.update_layout(
            xaxis_title='Probabilidades',
            yaxis_title='Resultado',
            bargroupgap=.1
        )
        st.plotly_chart(fig)

        # Previsão do próximo jogo
        abrir_pipeline = open('./modelos/resultado_partida_random_forest', 'rb')
        pipeline = pickle.load(abrir_pipeline)
        abrir_pipeline.close()
        dados = self.dados.query('clube == @self.clube and local == @self.local_jogo')[:self.ultimos_jogos]
        entrada =  [[self.local_jogo, round(dados['gols_marcados'].mean(), 1), round(dados['gols_sofridos'].mean(), 1),  
                    round(dados['posse'].mean(), 1), round(dados['gols_partida'].mean(), 1), round(dados['escanteios'].mean(), 1), 
                    round(dados['passes_certos_%'].mean(),1), round(dados['total_chutes'].mean(), 1), 
                    round(dados['chutes_a_gol_%'].mean(), 1), round(dados['chutes_por_gol'].mean(), 1), 
                    round(dados['cartoes_amarelos'].mean(), 1), round(dados['cartoes_vermelhos'].mean(), 1), 
                    round(dados['faltas_cometidas'].mean(), 1), 
                    round(dados['cartoes_total'].mean(), 1), round(dados['chutes_contra_o_gol'].mean(), 1), 
                    round(dados['defesas_%'].mean(), 1), round(dados['sem_vazamento'].mean(), 1)]]
        st.markdown('**RESULTADO PREVISTO**')
        st.text(pipeline.predict(entrada)[0])


    def indicador_gols(self):
        '''
        --> Mostra os indicadores referente aos gols
        '''
        #Variáveis
        #Gols partida
        dados_gols_partida = self.dados.query('clube == @self.clube and local == @self.local_jogo')['gols_partida'][:self.ultimos_jogos]
        media_gols_partida = round(dados_gols_partida.mean(), 1)
        desvio_padrao_gols_partida = round(dados_gols_partida.std())
        mais_frequente_gols_partida_list = dados_gols_partida.mode().values
        #Gols marcados
        dados_gols_marcados = self.dados.query('clube == @self.clube and local == @self.local_jogo')['gols_marcados'][:self.ultimos_jogos]
        media_gols_marcados = round(dados_gols_marcados.mean(), 1)
        desvio_padrao_gols_marcados = round(dados_gols_marcados.std())
        mais_frequente_gols_marcados_list = dados_gols_marcados.mode().values
        #Gols sofridos
        dados_gols_sofridos = self.dados.query('clube == @self.clube and local == @self.local_jogo')['gols_sofridos'][:self.ultimos_jogos]
        media_gols_sofridos = round(dados_gols_sofridos.mean(), 1)
        desvio_padrao_gols_sofridos = round(dados_gols_sofridos.std())
        mais_frequente_gols_sofridos_list = dados_gols_sofridos.mode().values
        
        #Visualizações
        #Gols marcados
        st.markdown('**GOLS MARCADOS**')
        st.text('Média: ' +  str(media_gols_marcados))
        st.text('Variação: ' + str(round(media_gols_marcados - desvio_padrao_gols_marcados)) +  ' - ' + str(round(media_gols_marcados + desvio_padrao_gols_marcados)))
        mais_frequente_gols_marcados_str = str()
        for i in range(len(mais_frequente_gols_marcados_list)):
            if i == 0:
                mais_frequente_gols_marcados_str = str(int(mais_frequente_gols_marcados_list[i]))
            else:
                mais_frequente_gols_marcados_str = mais_frequente_gols_marcados_str + ' - ' + str(int(mais_frequente_gols_marcados_list[i]))
        st.text('Mais frequênte: ' + mais_frequente_gols_marcados_str)
        #Gols sofridos
        st.markdown('**GOLS SOFRIDOS**')
        st.text('Média: ' +  str(media_gols_sofridos))
        st.text('Variação: ' + str(round(media_gols_sofridos - desvio_padrao_gols_sofridos)) +  ' - ' + str(round(media_gols_sofridos + desvio_padrao_gols_sofridos))) 
        mais_frequente_gols_sofridos_str = str()
        for i in range(len(mais_frequente_gols_sofridos_list)):
            if i == 0:
                mais_frequente_gols_sofridos_str = str(int(mais_frequente_gols_sofridos_list[i]))
            else:
                mais_frequente_gols_sofridos_str = mais_frequente_gols_sofridos_str + ' - ' + str(int(mais_frequente_gols_sofridos_list[i]))
        st.text('Mais frequênte: ' + mais_frequente_gols_sofridos_str)
        #Gols partida
        st.markdown('**MARCADOS + SOFRIDOS**')
        st.text('Média: ' + str(media_gols_partida))
        st.text('Variação: ' + str(round(media_gols_partida - desvio_padrao_gols_partida)) +  ' - ' + str(round(media_gols_partida + desvio_padrao_gols_partida)))
        mais_frequente_gols_partida_str = str()
        for i in range(len(mais_frequente_gols_partida_list)):
            if i == 0:
                mais_frequente_gols_partida_str = str(int(mais_frequente_gols_partida_list[i]))
            else:
                mais_frequente_gols_partida_str = mais_frequente_gols_partida_str + ' - ' + str(int(mais_frequente_gols_partida_list[i]))
        st.text('Mais frequênte: ' + mais_frequente_gols_partida_str)

        # Probabilidades do número de gols
        st.markdown('**PROBABILIDADES**')
        fig = px.histogram(y=dados_gols_partida, histnorm='probability density', cumulative=False, width=400, height=600)
        fig.update_layout(
            xaxis_title='Probabilidades',
            yaxis_title='Gols Marcados + Sofridos',
            bargroupgap=.1
        )
        st.plotly_chart(fig)


    def indicador_escanteios(self):
        '''
        --> Mostra os indicadores referente aos escanteios
        '''
        #Escanteios
        dados_escanteios = self.dados.query('clube == @self.clube and local == @self.local_jogo')['escanteios'][:self.ultimos_jogos]
        media_escanteios = round(dados_escanteios.mean())
        desvio_padrao_escanteios = round(dados_escanteios.std())
        mais_frequente_escanteio_list = dados_escanteios.mode().values
        
        #Visualização
        st.markdown('**ESCANTEIOS A FAVOR**')
        st.text('Média: ' +  str(media_escanteios))
        st.text('Variação: ' + str(media_escanteios - desvio_padrao_escanteios) +  '-' + str(media_escanteios + desvio_padrao_escanteios))  
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)

    
    def indicador_escanteios_partidas_mandante_ou_visitante(self):
        '''
        --> Mostra os indicadores referente ao total de escanteios (contra e a favor) na partida do clube selecionando como mandante ou visitante
        '''
        #escanteios
        dados_escanteios_partidas_local_unico = self.dados.query('clube == @self.clube and local == @self.local_jogo or oponente == @self.clube and local != @self.local_jogo').groupby('data', 
                                                                                                                                                                sort=False).sum()['escanteios'][:self.ultimos_jogos]
        media_escanteios = round(dados_escanteios_partidas_local_unico.mean())
        desvio_padrao_escanteios = round(dados_escanteios_partidas_local_unico.std())
        mais_frequente_escanteio_list = dados_escanteios_partidas_local_unico.mode().values
        
        #Visualização
        st.markdown('**ESCANTEIOS CONTRA/ A FAVOR**')
        st.text('Média: ' +  str(media_escanteios))
        st.text('Variação: ' + str(media_escanteios - desvio_padrao_escanteios) +  '-' + str(media_escanteios + desvio_padrao_escanteios))
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)
        #Probabilidades
        st.markdown('**PROBABILIDADES**')
        fig = px.histogram(y=dados_escanteios_partidas_local_unico, histnorm='probability density', 
                        cumulative=False, width=400, height=600)
        fig.update_layout(
            xaxis_title='Probabilidades',
            yaxis_title='Escanteios Contra/ A Favor',
            bargroupgap=.1
        )
        st.plotly_chart(fig)
    

    def indicador_escanteios_partidas_mandante_e_visitante(self):
        '''
        --> Mostra os indicadores referente ao total de escanteios (contra e a favor) na partida do clube selecionando como mandante e visitante
        '''
        #escanteios
        dados_escanteios_partidas_local_ambos = self.dados.query('clube == @self.clube or oponente == @self.clube').groupby('data', 
                                                                                                                            sort=False).sum()['escanteios'][:self.ultimos_jogos]
        media_escanteios = round(dados_escanteios_partidas_local_ambos.mean())
        desvio_padrao_escanteios = round(dados_escanteios_partidas_local_ambos.std())
        mais_frequente_escanteio_list = dados_escanteios_partidas_local_ambos.mode().values
        
        #Visualização
        st.markdown('**ESCANTEIOS CONTRA/ A FAVOR**')
        st.text('Média: ' +  str(media_escanteios))
        st.text('Variação: ' + str(media_escanteios - desvio_padrao_escanteios) +  '-' + str(media_escanteios + desvio_padrao_escanteios))
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)
        #Probabilidades
        st.markdown('**PROBABILIDADES**')
        fig = px.histogram(y=dados_escanteios_partidas_local_ambos, histnorm='probability density', 
                        cumulative=False, width=400, height=600)
        fig.update_layout(
            xaxis_title='Probabilidades',
            yaxis_title='Escanteios Contra/ A Favor',
            bargroupgap=.1
        )
        st.plotly_chart(fig)


    def indicador_cartoes(self):
        '''
        --> Indicador do número de cartões
        '''
        #Total cartẽos
        dados_cartoes_total = self.dados.query('clube == @self.clube and local == @self.local_jogo')['cartoes_total'][:self.ultimos_jogos]
        media_cartoes_total = round(dados_cartoes_total.mean())
        desvio_padrao_cartoes_total = round(dados_cartoes_total.std())
        #cartões amarelos
        dados_cartoes_amarelos = self.dados.query('clube == @self.clube and local == @self.local_jogo')['cartoes_amarelos'][:self.ultimos_jogos] 
        media_cartoes_amarelos = round(dados_cartoes_amarelos.mean())
        desvio_padrao_cartoes_amarelos = round(dados_cartoes_amarelos.std())
        #cartões vermelhos
        dados_cartoes_vermelhos = self.dados.query('clube == @self.clube and local == @self.local_jogo')['cartoes_vermelhos'][:self.ultimos_jogos]
        media_cartoes_vermelhos = round(dados_cartoes_vermelhos.mean())
        desvio_padrao_cartoes_vermelhos = round(dados_cartoes_vermelhos.std())

        #Visualização
        st.markdown('**TOTAL CARTÕES**')
        st.text('Média: ' +  str(media_cartoes_total))
        st.text('Variação: ' + str(media_cartoes_total - desvio_padrao_cartoes_total) +  '-' + str(media_cartoes_total + desvio_padrao_cartoes_total))

        st.markdown('**CARTÕES AMARELOS**')
        st.text('Média: ' +  str(media_cartoes_amarelos))
        st.text('Variação: ' + str(media_cartoes_amarelos - desvio_padrao_cartoes_amarelos) +  '-' + str(media_cartoes_amarelos + desvio_padrao_cartoes_amarelos))

        st.markdown('**CARTÕES VERMELHOS**')
        st.text('Média: ' +  str(media_cartoes_vermelhos))
        st.text('Variação: ' + str(media_cartoes_vermelhos - desvio_padrao_cartoes_vermelhos) +  '-' + str(media_cartoes_vermelhos + desvio_padrao_cartoes_vermelhos))
        #Probabilidades
        st.markdown('**PROBABILIDADES TOTAL CARTÕES**')
        fig = px.histogram(y=dados_cartoes_total, histnorm='probability density', cumulative=False,
                        width=400, height=600)
        fig.update_layout(
            xaxis_title='Probabilidades',
            yaxis_title='Número de cartões',
            bargroupgap=.1
        )
        st.plotly_chart(fig)
        

    def indicador_controle_jogo(self):
        '''
        --> Mostra os indicadores referente ao controle do jogo
        '''
        #posse de bola
        dados_posse_bola = self.dados.query('clube == @self.clube and local == @self.local_jogo')['posse'][:self.ultimos_jogos]
        media_posse_bola = round(dados_posse_bola.mean())
        desvio_padrao_posse_bola = round(dados_posse_bola.std())
        #passes certos
        dados_passes_certos = self.dados.query('clube == @self.clube and local == @self.local_jogo')['passes_certos_%'][:self.ultimos_jogos]
        media_passes_certos = round(dados_passes_certos.mean())
        desvio_padrao_passes_certos = round(dados_passes_certos.std())

        #Visualização
        st.markdown('**POSSE DE BOLA**')
        st.text('Média: ' +  str(media_posse_bola) + '%')
        st.text('Intervalo: ' + str(media_posse_bola - desvio_padrao_posse_bola) + '%' +  ' - ' + str(media_posse_bola + desvio_padrao_posse_bola) + '%')  
        st.markdown('**PASSES CERTOS**')
        st.text('Média: ' +  str(media_passes_certos) + '%')
        st.text('Variação: ' + str(media_passes_certos - desvio_padrao_passes_certos) + '%' +  ' - ' + str(media_passes_certos + desvio_padrao_passes_certos) + '%')  


    def indicador_ofensividade(self):
        '''
        --> Mostra os indicadores de ofensividade
        '''
        #chutes a gol
        dados_chutes_a_gol = self.dados.query('clube == @self.clube and local == @self.local_jogo')['chutes_a_gol_%'][:self.ultimos_jogos]
        media_chutes_a_gol = round(dados_chutes_a_gol.mean())
        desvio_padrao_chutes_a_gol = round(dados_chutes_a_gol.std())
        #chutes por gol
        dados_chutes_por_gol = self.dados.query('clube == @self.clube and local == @self.local_jogo')['chutes_por_gol'][:self.ultimos_jogos]
        media_chutes_por_gol = round(dados_chutes_por_gol.mean())
        desvio_padrao_chutes_por_gol = round(dados_chutes_por_gol.std())
        #total chutes
        dados_chutes = self.dados.query('clube == @self.clube and local == @self.local_jogo')['total_chutes'][:self.ultimos_jogos]
        media_chutes = round(dados_chutes.mean())
        desvio_padrao_chutes = round(dados_chutes.std())
        
        #Visualização
        st.markdown('**TOTAL DE CHUTES**')
        st.text('Média: ' + str(media_chutes))
        st.text('Variação: ' + str(media_chutes - desvio_padrao_chutes) +  ' - ' + str(media_chutes + desvio_padrao_chutes))    
        st.markdown('**CHUTES NO GOL**')
        st.text('Média: ' +  str(media_chutes_a_gol) + '%')
        st.text('Variação: ' + str(media_chutes_a_gol - desvio_padrao_chutes_a_gol) + '%' +  ' - ' + str(media_chutes_a_gol + desvio_padrao_chutes_a_gol) + '%')    
        st.markdown('**NÚMERO DE CHUTES PARA CADA GOL**')
        st.text('Média: ' +  str(int(media_chutes_por_gol)))
        st.text('Variação: ' + str(media_chutes_por_gol - desvio_padrao_chutes_por_gol) +  ' - ' + str(media_chutes_por_gol + desvio_padrao_chutes_por_gol))    
    

    def indicador_defesa(self):
        '''
        --> Indicadores do sistema defensivo
        '''
        #chutes_contra_gol
        dados_chutes_contra_gol = self.dados.query('clube == @self.clube and local == @self.local_jogo')['chutes_contra_o_gol'][:self.ultimos_jogos]
        media_chutes_contra_gol = round(dados_chutes_contra_gol.mean())
        desvio_padrao_chutes_contra_gol = round(dados_chutes_contra_gol.std())
        #defesas
        dados_defesas = self.dados.query('clube == @self.clube and local == @self.local_jogo')['defesas_%'][:self.ultimos_jogos]
        media_defesas = round(dados_defesas.mean())
        desvio_padrao_defesas = round(dados_defesas.std())
        #sem vazamento
        dados_sem_vazamento = self.dados.query('clube == @self.clube and local == @self.local_jogo')['sem_vazamento'][:self.ultimos_jogos]
        media_sem_vazamento = round(dados_sem_vazamento.mean(), 1)
        desvio_padrao_sem_vazamento = round(dados_sem_vazamento.std())
        
        #Visualização
        st.markdown('**CHUTES CONTRA O GOL**')
        st.text('Média: ' + str(media_chutes_contra_gol))
        st.text('Variação: ' + str(media_chutes_contra_gol - desvio_padrao_chutes_contra_gol) +  ' - ' + str(media_chutes_contra_gol + desvio_padrao_chutes_contra_gol))    
        st.markdown('**CHUTES DEFENDIDOS**')
        st.text('Média: ' +  str(media_defesas) + '%')
        st.text('Variação: ' + str(media_defesas - desvio_padrao_defesas) + '%' +  ' - ' + str(media_defesas + desvio_padrao_defesas) + '%')    
        st.markdown('**SEM VAZAMENTO**')
        st.text('Média: ' +  str(int(media_sem_vazamento)))
        st.text('Variação: ' + str(media_sem_vazamento - desvio_padrao_sem_vazamento) +  ' - ' + str(media_sem_vazamento + desvio_padrao_sem_vazamento))

    
    def rodadas_mandante_e_visitante(self):
        '''
        --> DataFrame referente aos jogos do clube como mandante e visitante
        '''
        st.dataframe(self.dados.query('clube == @self.clube')[['clube', 'resultado', 'gols_marcados',
                                                            'gols_sofridos', 'oponente', 'posse',
                                                            'escanteios']].iloc[:self.ultimos_jogos, :-1])


    def rodadas_mandante_ou_visitante(self):
        '''
        --> Data Frame com os jogos do clube como mandante ou visitante
        '''
        st.dataframe(self.dados.query('clube == @self.clube and local == @self.local_jogo')[['clube', 'resultado', 'gols_marcados',
                                                                                        'gols_sofridos', 'oponente', 'posse',
                                                                                        'escanteios']].iloc[:self.ultimos_jogos, :-1])
