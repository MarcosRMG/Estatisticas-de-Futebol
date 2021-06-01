import pandas as pd
import streamlit as st
import plotly_express as px


class IndicadoresFbref:
    '''
    --> Calcula os indicadores para visualização dos dados capturados no site https://fbref.com/pt/
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

    
    def indicador_ultimos_5_resultados(self):
        '''
        --> Últimos cinco resultados da equipe
        '''
        if self.dados.query('clube == @self.clube and local == @self.local_jogo')['resultado'].empty:
            st.markdown('**ÚLTIMOS RESULTADOS**')
            st.text('Resultados indisponíveis')
        else:
            resultados_partidas_list = self.dados.query('clube == @self.clube and local == @self.local_jogo')['resultado'][:5].values
            resultados_partidas_str = str()
            for i in range(len(resultados_partidas_list)):
                if i == 0:
                    resultados_partidas_str = str(resultados_partidas_list[i])
                else:
                    resultados_partidas_str = resultados_partidas_str + ' - ' + str(resultados_partidas_list[i])
            st.markdown('**ÚLTIMOS RESULTADOS**')
            st.markdown(resultados_partidas_str[::-1])

    
    def probabilidades_indicador_resultados(self):
        '''
        --> Últimos cinco resultados e previsão do próximo resultado
        '''
        resultados_partidas = self.dados.query('clube == @self.clube and local == @self.local_jogo')['resultado'][:self.ultimos_jogos]
        if self.local_jogo == 'Em casa':
            time = 'Mandante'
        else:
            time = 'Visitante'
        if resultados_partidas.empty:
            fig = px.histogram(pd.DataFrame({'x': [0], 'y': [0]}) ,x='x', y='y', width=400, height=600)
            fig.update_layout(
                title=f'Probabilidade {time} na Liga',
                xaxis_title='Probabilidades Indisponíveis',
                yaxis_title='',)
            st.plotly_chart(fig)
        else:
            fig = px.histogram(y=resultados_partidas, histnorm='probability density', cumulative=False, width=400, height=600)
            fig.update_layout(
                title=f'Probabilidade {time} na Liga',
                xaxis_title='Probabilidades',
                yaxis_title='Resultado',
                bargroupgap=.1)
            st.plotly_chart(fig)


class IndicadoresCouk:
    '''
    --> Calcula os indicadores para visualização dos dados coletados no site https://www.football-data.co.uk/
    '''
    def __init__(self, dados=None, mandante=None, visitante=None, ultimos_jogos=None):
        '''
        :param dados: DataFrame contendo os registros dos jogos
        :param mandante: Clube mandante selecionado pelo usuário
        :param visitante: Clube visitante selecionado pelo usuário
        :param
        '''
        self.dados = dados
        self.mandante = mandante
        self.visitante = visitante
        self.ultimos_jogos = ultimos_jogos

    
    def confronto_direto(self):
        # Probabilidades confronto direto
        probabilidade_confronto_direto = self.dados.query('mandante == @self.mandante and visitante == @self.visitante')['resultado']
        if probabilidade_confronto_direto.empty:
            fig = px.histogram(pd.DataFrame({'x': [0], 'y': [0]}) ,x='x', y='y', width=400, height=600)
            fig.update_layout(
                title='Confronto Direto 12 A 21',
                xaxis_title='Probabilidades Indisponíveis',
                yaxis_title='',)
            st.plotly_chart(fig)
        else:
            fig = px.histogram(y=probabilidade_confronto_direto, histnorm='probability density', cumulative=False, width=400, height=600)
            fig.update_layout(
                title='Confronto Direto 2012 A 2021',
                xaxis_title='Probabilidades',
                yaxis_title='',
                bargroupgap=.1)
            st.plotly_chart(fig)
            
            
    def probabilidade_resultados_liga(self):
        '''
        --> Plota a probabilidade do resultado com base nos resultados da liga
        '''
        probabilidade_resultados_liga = self.dados.query('mandante == @self.mandante or visitante == @self.visitante')['resultado']
        if probabilidade_resultados_liga.empty:
            fig = px.histogram(pd.DataFrame({'x': [0], 'y': [0]}) ,x='x', y='y', width=400, height=600)
            fig.update_layout(
                title='Jogos da Liga 2021',
                xaxis_title='Probabilidades Indisponíveis',
                yaxis_title='',)
            st.plotly_chart(fig)
        else:
            fig = px.histogram(y=probabilidade_resultados_liga, histnorm='probability density', cumulative=False, width=400, height=600)
            fig.update_layout(
                title='Jogos da Liga 2021',
                xaxis_title='Probabilidades',
                yaxis_title='',
                bargroupgap=.1)
            st.plotly_chart(fig)

    
    def gols_mandante(self):
        '''
        --> Mostra os indicadores referente aos gols
        '''
        #Verificando existência de dados
        if self.dados.query('mandante == @self.mandante').empty:
            st.text('Estatísticas indisponíveis')
        else:
            #Variáveis
            #Gols partida
            # Dados da temporada atual
            dados_gols_partida = self.dados.query('mandante == @self.mandante')['gols_partida'][:self.ultimos_jogos]
            media_gols_partida = round(dados_gols_partida.mean(), 1)
            desvio_padrao_gols_partida = round(dados_gols_partida.std())
            mais_frequente_gols_partida_list = dados_gols_partida.mode().values
            #Gols marcados
            dados_gols_marcados = self.dados.query('mandante == @self.mandante')['gols_mandante_partida'][:self.ultimos_jogos]
            media_gols_marcados = round(dados_gols_marcados.mean(), 1)
            desvio_padrao_gols_marcados = round(dados_gols_marcados.std())
            mais_frequente_gols_marcados_list = dados_gols_marcados.mode().values
            #Gols sofridos
            dados_gols_sofridos = self.dados.query('mandante == @self.mandante')['gols_visitante_partida'][:self.ultimos_jogos]
            media_gols_sofridos = round(dados_gols_sofridos.mean(), 1)
            desvio_padrao_gols_sofridos = round(dados_gols_sofridos.std())
            mais_frequente_gols_sofridos_list = dados_gols_sofridos.mode().values

            #Visualizações
            #Gols marcados
            st.markdown('**MARCADOS**')
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
            st.markdown('**SOFRIDOS**')
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


    def gols_visitante(self):
        #Verificando existência de dados
        if self.dados.query('visitante == @self.visitante').empty:
            st.text('Estatísticas indisponíveis')
        else:
            #Variáveis
            #Gols partida
            # Dados da temporada atual
            dados_gols_partida = self.dados.query('visitante == @self.visitante')['gols_partida'][:self.ultimos_jogos]
            media_gols_partida = round(dados_gols_partida.mean(), 1)
            desvio_padrao_gols_partida = round(dados_gols_partida.std())
            mais_frequente_gols_partida_list = dados_gols_partida.mode().values
            #Gols marcados
            dados_gols_marcados = self.dados.query('visitante == @self.visitante')['gols_visitante_partida'][:self.ultimos_jogos]
            media_gols_marcados = round(dados_gols_marcados.mean(), 1)
            desvio_padrao_gols_marcados = round(dados_gols_marcados.std())
            mais_frequente_gols_marcados_list = dados_gols_marcados.mode().values
            #Gols sofridos
            dados_gols_sofridos = self.dados.query('visitante == @self.visitante')['gols_mandante_partida'][:self.ultimos_jogos]
            media_gols_sofridos = round(dados_gols_sofridos.mean(), 1)
            desvio_padrao_gols_sofridos = round(dados_gols_sofridos.std())
            mais_frequente_gols_sofridos_list = dados_gols_sofridos.mode().values

            #Visualizações
            #Gols marcados
            st.markdown('**MARCADOS**')
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
            st.markdown('**SOFRIDOS**')
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


    def probabilidade_gols_partida(self):
        '''
        --> Plota o gráfico de probabilidade do número de gols para a partida
        '''
        if self.dados.query('mandante == @self.mandante').empty or self.dados.query('visitante == @self.visitante').empty:
            fig = px.histogram(pd.DataFrame({'x': [0], 'y': [0]}) ,x='x', y='y', width=600, height=600)
            fig.update_layout(
                title='Probabilidades indisponíveis',
                xaxis_title='Probabilidades',
                yaxis_title='Gols partida',
                bargroupgap=.1)
            st.plotly_chart(fig)
        else:
            n_jogos_mandante = len(self.dados.query('mandante == @self.mandante')['gols_partida'])
            n_jogos_visitante = len(self.dados.query('visitante == @self.visitante')['gols_partida'])
            menor_numero_jogos = min(n_jogos_mandante, n_jogos_visitante)
            gols_partida_mandante = self.dados.query('mandante == @self.mandante')['gols_partida'][:menor_numero_jogos].values
            gols_partida_visitante = self.dados.query('visitante == @self.visitante')['gols_partida'][:menor_numero_jogos].values
            probabilidades_gols_partida = (gols_partida_mandante + gols_partida_visitante) / 2
            # Probabilidades do número de gols
            fig = px.histogram(y=probabilidades_gols_partida, histnorm='probability density', cumulative=False, width=600, height=600)
            fig.update_layout(
                title='Probabilidades de Gols',
                xaxis_title='Probabilidades',
                yaxis_title='Gols partida',
                bargroupgap=.1)
            st.plotly_chart(fig)

    
    def probabilidade_escanteios_partida(self):
        '''
        --> Plota o gráfico de probabilidade do número de escanteios para a partida
        '''
        n_jogos_mandante = len(self.dados.query('mandante == @self.mandante')['escanteios_partida'])
        n_jogos_visitante = len(self.dados.query('visitante == @self.visitante')['escanteios_partida'])
        menor_numero_jogos = min(n_jogos_mandante, n_jogos_visitante)
        escanteios_partida_mandante = self.dados.query('mandante == @self.mandante')['escanteios_partida'][:menor_numero_jogos].values
        escanteios_partida_visitante = self.dados.query('visitante == @self.visitante')['escanteios_partida'][:menor_numero_jogos].values
        probabilidades_escanteios_partida = (escanteios_partida_mandante + escanteios_partida_visitante) / 2
        fig = px.histogram(y=probabilidades_escanteios_partida, histnorm='probability density', cumulative=False, width=600, 
                        height=600)
        fig.update_layout(
            title='Probabilidade de Escanteios',
            xaxis_title='Probabilidades',
            yaxis_title='Escanteios partida',
            bargroupgap=.1
        )
        st.plotly_chart(fig)


    def escanteios_mandante(self):
        '''
        --> Mostra os indicadores referente aos escanteios
        '''
        #Escanteios
        #Partida
        dados_escanteios_partida = self.dados.query('mandante == @self.mandante')['escanteios_partida'][:self.ultimos_jogos]
        media_escanteios_partida = round(dados_escanteios_partida.mean())
        desvio_padrao_escanteios_partida = round(dados_escanteios_partida.std())
        mais_frequente_escanteio_partida_list = dados_escanteios_partida.mode().values
        #A favor
        dados_escanteios = self.dados.query('mandante == @self.mandante')['escanteios_mandante'][:self.ultimos_jogos]
        media_escanteios = round(dados_escanteios.mean())
        desvio_padrao_escanteios = round(dados_escanteios.std())
        mais_frequente_escanteio_list = dados_escanteios.mode().values
        
        #Visualização
        st.markdown('**A FAVOR**')
        st.text('Média: ' +  str(media_escanteios))
        st.text('Variação: ' + str(media_escanteios - desvio_padrao_escanteios) +  '-' + str(media_escanteios + desvio_padrao_escanteios))  
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)

        st.markdown('**CONTRA/ A FAVOR**')
        st.text('Média: ' +  str(media_escanteios_partida))
        st.text('Variação: ' + str(media_escanteios_partida - desvio_padrao_escanteios_partida) +  '-' + str(media_escanteios_partida + desvio_padrao_escanteios_partida))
        
        mais_frequente_escanteio_partida_str = str()
        for i in range(len(mais_frequente_escanteio_partida_list)):
            if i == 0:
                mais_frequente_escanteio_partida_str = str(int(mais_frequente_escanteio_partida_list[i]))
            else:
                mais_frequente_escanteio_partida_str = mais_frequente_escanteio_partida_str + ' - ' + str(int(mais_frequente_escanteio_partida_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_partida_str)


    def escanteios_visitante(self):
        '''
        --> Mostra os indicadores referente aos escanteios
        '''
        #Escanteios
        #Partida
        dados_escanteios_partida = self.dados.query('visitante == @self.visitante')['escanteios_partida'][:self.ultimos_jogos]
        media_escanteios_partida = round(dados_escanteios_partida.mean())
        desvio_padrao_escanteios_partida = round(dados_escanteios_partida.std())
        mais_frequente_escanteio_partida_list = dados_escanteios_partida.mode().values
        #A favor
        dados_escanteios = self.dados.query('visitante == @self.visitante')['escanteios_visitante'][:self.ultimos_jogos]
        media_escanteios = round(dados_escanteios.mean())
        desvio_padrao_escanteios = round(dados_escanteios.std())
        mais_frequente_escanteio_list = dados_escanteios.mode().values
        
        #Visualização
        st.markdown('**A FAVOR**')
        st.text('Média: ' +  str(media_escanteios))
        st.text('Variação: ' + str(media_escanteios - desvio_padrao_escanteios) +  '-' + str(media_escanteios + desvio_padrao_escanteios))  
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)

        st.markdown('**CONTRA/ A FAVOR**')
        st.text('Média: ' +  str(media_escanteios_partida))
        st.text('Variação: ' + str(media_escanteios_partida - desvio_padrao_escanteios_partida) +  '-' + str(media_escanteios_partida + desvio_padrao_escanteios_partida))
        
        mais_frequente_escanteio_partida_str = str()
        for i in range(len(mais_frequente_escanteio_partida_list)):
            if i == 0:
                mais_frequente_escanteio_partida_str = str(int(mais_frequente_escanteio_partida_list[i]))
            else:
                mais_frequente_escanteio_partida_str = mais_frequente_escanteio_partida_str + ' - ' + str(int(mais_frequente_escanteio_partida_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_partida_str)


    def cartoes_mandante(self):
        '''
        --> Indicador do número de cartões
        '''
        #Total cartẽos
        dados_cartoes_total = self.dados.query('mandante == @self.mandante')['total_cartoes_partida'][:self.ultimos_jogos]
        media_cartoes_total = round(dados_cartoes_total.mean())
        desvio_padrao_cartoes_total = round(dados_cartoes_total.std())
        #cartões amarelos
        dados_cartoes_amarelos = self.dados.query('mandante == @self.mandante')['cartoes_amarelos_mandante'][:self.ultimos_jogos] 
        media_cartoes_amarelos = round(dados_cartoes_amarelos.mean())
        desvio_padrao_cartoes_amarelos = round(dados_cartoes_amarelos.std())
        #cartões vermelhos
        dados_cartoes_vermelhos = self.dados.query('mandante == @self.mandante')['cartoes_vermelhos_mandante'][:self.ultimos_jogos]
        media_cartoes_vermelhos = round(dados_cartoes_vermelhos.mean())
        desvio_padrao_cartoes_vermelhos = round(dados_cartoes_vermelhos.std())

        #Visualização
        st.markdown('**AMARELOS**')
        st.text('Média: ' +  str(media_cartoes_amarelos))
        st.text('Variação: ' + str(media_cartoes_amarelos - desvio_padrao_cartoes_amarelos) +  '-' + str(media_cartoes_amarelos + desvio_padrao_cartoes_amarelos))

        st.markdown('**VERMELHOS**')
        st.text('Média: ' +  str(media_cartoes_vermelhos))
        st.text('Variação: ' + str(media_cartoes_vermelhos - desvio_padrao_cartoes_vermelhos) +  '-' + str(media_cartoes_vermelhos + desvio_padrao_cartoes_vermelhos))

        st.markdown('**CONTRA/ A FAVOR**')
        st.text('Média: ' +  str(media_cartoes_total))
        st.text('Variação: ' + str(media_cartoes_total - desvio_padrao_cartoes_total) +  '-' + str(media_cartoes_total + desvio_padrao_cartoes_total))


    def cartoes_visitante(self):
        '''
        --> Indicador do número de cartões
        '''
        #Total cartẽos
        dados_cartoes_total = self.dados.query('visitante == @self.visitante')['total_cartoes_partida'][:self.ultimos_jogos]
        media_cartoes_total = round(dados_cartoes_total.mean())
        desvio_padrao_cartoes_total = round(dados_cartoes_total.std())
        #cartões amarelos
        dados_cartoes_amarelos = self.dados.query('visitante == @self.visitante')['cartoes_amarelos_visitante'][:self.ultimos_jogos] 
        media_cartoes_amarelos = round(dados_cartoes_amarelos.mean())
        desvio_padrao_cartoes_amarelos = round(dados_cartoes_amarelos.std())
        #cartões vermelhos
        dados_cartoes_vermelhos = self.dados.query('visitante == @self.visitante')['cartoes_vermelhos_visitante'][:self.ultimos_jogos]
        media_cartoes_vermelhos = round(dados_cartoes_vermelhos.mean())
        desvio_padrao_cartoes_vermelhos = round(dados_cartoes_vermelhos.std())

        #Visualização
        st.markdown('**AMARELOS**')
        st.text('Média: ' +  str(media_cartoes_amarelos))
        st.text('Variação: ' + str(media_cartoes_amarelos - desvio_padrao_cartoes_amarelos) +  '-' + str(media_cartoes_amarelos + desvio_padrao_cartoes_amarelos))

        st.markdown('**VERMELHOS**')
        st.text('Média: ' +  str(media_cartoes_vermelhos))
        st.text('Variação: ' + str(media_cartoes_vermelhos - desvio_padrao_cartoes_vermelhos) +  '-' + str(media_cartoes_vermelhos + desvio_padrao_cartoes_vermelhos))

        st.markdown('**CONTRA/ A FAVOR**')
        st.text('Média: ' +  str(media_cartoes_total))
        st.text('Variação: ' + str(media_cartoes_total - desvio_padrao_cartoes_total) +  '-' + str(media_cartoes_total + desvio_padrao_cartoes_total))


    def probabilidade_cartoes_partida(self):
        '''
        --> Plota o gráfico de probabilidade do número de cartões para a partida
        '''
        n_jogos_mandante = len(self.dados.query('mandante == @self.mandante')['total_cartoes_partida'])
        n_jogos_visitante = len(self.dados.query('visitante == @self.visitante')['total_cartoes_partida'])
        menor_numero_jogos = min(n_jogos_mandante, n_jogos_visitante)
        cartoes_partida_mandante = self.dados.query('mandante == @self.mandante')['total_cartoes_partida'][:menor_numero_jogos].values
        cartoes_partida_visitante = self.dados.query('visitante == @self.visitante')['total_cartoes_partida'][:menor_numero_jogos].values
        probabilidades_cartoes_partida = (cartoes_partida_mandante + cartoes_partida_visitante) / 2
        fig = px.histogram(y=probabilidades_cartoes_partida, histnorm='probability density', cumulative=False, width=600, 
                        height=600)
        fig.update_layout(
            title='Probabilidade Cartões',
            xaxis_title='Probabilidades',
            yaxis_title='Cartões partida',
            bargroupgap=.1
        )
        st.plotly_chart(fig)
