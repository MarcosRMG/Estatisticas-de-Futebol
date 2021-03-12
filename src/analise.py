import pandas as pd
import streamlit as st


class Indicadores:
    '''
    --> Calcula os indicadores para visualização
    '''
    def __init__(self, dados=None, ultimos_jogos=None):
        '''
        :param dados: DataFrame contendo as informações para cálculo dos indicadores
        :param ultimos_jogos: Escolha do usuário do número de jogos anteriores para cálculo
        dos indicadores
        '''
        self.dados = dados
        self.ultimos_jogos = ultimos_jogos


    def ultimos_cinco_resultados(self):
        '''
        --> Mostra o resultados das últimas cinco partidas
        '''
        resultados_partidas_list = self.dados['resultado'][:5].values
        resultados_partidas_str = str()
        for i in range(len(resultados_partidas_list)):
            if i == 0:
                resultados_partidas_str = str(resultados_partidas_list[i])
            else:
                resultados_partidas_str = resultados_partidas_str + ' - ' + str(resultados_partidas_list[i])
        st.markdown('**ÚLTIMOS RESULTADOS**')
        st.markdown(resultados_partidas_str)


    def indicador_gols(self):
        '''
        --> Mostra os indicadores referente aos gols
        '''
        #Variáveis
        media_gols_partida = round(self.dados['gols_partida'][:self.ultimos_jogos].mean())
        mais_frequente_gols_partida_list = self.dados['gols_partida'][:self.ultimos_jogos].mode().values
        desvio_padrao_gols_partida = round(self.dados['gols_partida'][:self.ultimos_jogos].std())
        media_gols_marcados = round(self.dados['gols_marcados'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_marcados = round(self.dados['gols_marcados'][:self.ultimos_jogos].std())
        media_gols_sofridos = round(self.dados['gols_sofridos'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_sofridos = round(self.dados['gols_sofridos'][:self.ultimos_jogos].std())
        
        #Visualizações
        st.markdown('**GOLS MARCADOS**')
        st.text('Média: ' +  str(int(media_gols_marcados)))
        st.text('Intervalo: ' + str(int(media_gols_marcados - desvio_padrao_gols_marcados)) +  ' - ' + str(int(media_gols_marcados + desvio_padrao_gols_marcados)))
        st.markdown('**GOLS SOFRIDOS**')
        st.text('Média: ' +  str(int(media_gols_sofridos)))
        st.text('Intervalo: ' + str(int(media_gols_sofridos - desvio_padrao_gols_sofridos)) +  ' - ' + str(int(media_gols_sofridos + desvio_padrao_gols_sofridos)))  
        st.markdown('**MARCADOS + SOFRIDOS**')
        st.text('Média: ' + str(int(media_gols_partida)))
        st.text('Intervalo: ' + str(int(media_gols_partida - desvio_padrao_gols_partida)) +  ' - ' + str(int(media_gols_partida + desvio_padrao_gols_partida)))  
        
        mais_frequente_gols_partida_str = str()
        for i in range(len(mais_frequente_gols_partida_list)):
            if i == 0:
                mais_frequente_gols_partida_str = str(int(mais_frequente_gols_partida_list[i]))
            else:
                mais_frequente_gols_partida_str = mais_frequente_gols_partida_str + ' - ' + str(int(mais_frequente_gols_partida_list[i]))
        st.text('Mais frequênte: ' + mais_frequente_gols_partida_str)


    def indicador_escanteios(self):
        '''
        --> Mostra os indicadores referente aos escanteios
        '''
        #Variáveis
        media_escanteios = round(self.dados['escanteios'][:self.ultimos_jogos].mean())
        desvio_padrao_escanteios = round(self.dados['escanteios'][:self.ultimos_jogos].std())
        mais_frequente_escanteio_list = self.dados['escanteios'][:self.ultimos_jogos].mode().values
        
        #Visualização
        st.markdown('**ESCANTEIOS A FAVOR**')
        st.text('Média: ' +  str(int(media_escanteios)))
        st.text('Intervalo: ' + str(int(media_escanteios - desvio_padrao_escanteios)) +  '-' + str(int(media_escanteios + desvio_padrao_escanteios)))  
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)

    
    def indicador_escanteios_partidas(self):
        '''
        --> Mostra os indicadores referente aos escanteios
        '''
        #Variáveis
        media_escanteios = round(self.dados['escanteios'][:self.ultimos_jogos].mean())
        desvio_padrao_escanteios = round(self.dados['escanteios'][:self.ultimos_jogos].std())
        mais_frequente_escanteio_list = self.dados['escanteios'][:self.ultimos_jogos].mode().values
        
        #Visualização
        st.markdown('**ESCANTEIOS CONTRA E A FAVOR**')
        st.text('Média: ' +  str(int(media_escanteios)))
        st.text('Intervalo: ' + str(int(media_escanteios - desvio_padrao_escanteios)) +  '-' + str(int(media_escanteios + desvio_padrao_escanteios)))  
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)

        
    def indicador_controle_jogo(self):
        '''
        --> Mostra os indicadores referente ao controle do jogo
        '''
        #Variáveis
        media_posse_bola = round(self.dados['posse'][:self.ultimos_jogos].mean())
        desvio_padrao_posse_bola = round(self.dados['posse'][:self.ultimos_jogos].std())
        media_passes_certos = round(self.dados['passes_certos_%'][:self.ultimos_jogos].mean())
        desvio_padrao_passes_certos = round(self.dados['passes_certos_%'][:self.ultimos_jogos].std())

        #Visualização
        st.markdown('**POSSE DE BOLA**')
        st.text('Média: ' +  str(int(media_posse_bola)) + '%')
        st.text('Intervalo: ' + str(int(media_posse_bola - desvio_padrao_posse_bola)) + '%' +  ' - ' + str(int(media_posse_bola + desvio_padrao_posse_bola)) + '%')  
        st.markdown('**PASSES CERTOS**')
        st.text('Média: ' +  str(int(media_passes_certos)) + '%')
        st.text('Intervalo: ' + str(int(media_passes_certos - desvio_padrao_passes_certos)) + '%' +  ' - ' + str(int(media_passes_certos + desvio_padrao_passes_certos)) + '%')  


    def indicador_ofensividade(self):
        '''
        --> Mostra os indicadores de ofensividade
        :param dados: DataFrame com o números das rodadas da liga
        :param ultimos_jogos: Seleção do número de jogos anteriores para cálculo dos indicadores
        '''
        #Variáveis
        media_chutes_gol = round(self.dados['chutes_ao_gol_%'][:self.ultimos_jogos].mean())
        desvio_padrao_chutes_gol = round(self.dados['chutes_ao_gol_%'][:self.ultimos_jogos].std())
        media_gol_chutes_gol = round(self.dados['gols_por_chute_ao_gol_%'][:self.ultimos_jogos].mean())
        desvio_padrao_gol_chutes_gol = round(self.dados['gols_por_chute_ao_gol_%'][:self.ultimos_jogos].std())
        media_chutes = round(self.dados['total_chutes'][:self.ultimos_jogos].mean())
        desvio_padrao_chutes = round(self.dados['total_chutes'][:self.ultimos_jogos].std())
        
        #Visualização
        st.markdown('**TOTAL DE CHUTES**')
        st.text('Média: ' + str(int(media_chutes)))
        st.text('Intervalo: ' + str(int(media_chutes - desvio_padrao_chutes)) +  ' - ' + str(int(media_chutes + desvio_padrao_chutes)))    
        st.markdown('**CHUTES NO GOL**')
        st.text('Média: ' +  str(int(media_chutes_gol)) + '%')
        st.text('Intervalo: ' + str(int(media_chutes_gol - desvio_padrao_chutes_gol)) + '%' +  ' - ' + str(int(media_chutes_gol + desvio_padrao_chutes_gol)) + '%')    
        st.markdown('**GOL POR CHUTE NO GOL**')
        st.text('Média: ' +  str(int(media_gol_chutes_gol)) + '%')
        st.text('Intervalo: ' + str(int(media_gol_chutes_gol - desvio_padrao_gol_chutes_gol)) + '%' +  ' - ' + str(int(media_gol_chutes_gol + desvio_padrao_gol_chutes_gol)) + '%')    
    
