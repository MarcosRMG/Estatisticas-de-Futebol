import pandas as pd
import streamlit as st


class indicadores:
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


    def indicador_gols(self):
        '''
        --> Mostra os indicadores referente aos gols
        '''
        #Gols
        media_gols_partida = round(self.dados['gols_partida'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_partida = round(self.dados['gols_partida'][:self.ultimos_jogos].std())
        media_gols_marcados = round(self.dados['gols_marcados'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_marcados = round(self.dados['gols_marcados'][:self.ultimos_jogos].std())
        media_gols_sofridos = round(self.dados['gols_sofridos'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_sofridos = round(self.dados['gols_sofridos'][:self.ultimos_jogos].std())

        st.markdown('RESULTADOS')
        st.markdown(self.dados['resultado'][:self.ultimos_jogos].values)
        #Gols
        st.markdown('GOLS MARCADOS')
        st.text('Média: ' +  str(int(media_gols_marcados)))
        st.text('Intervalo: ' + str(int(media_gols_marcados - desvio_padrao_gols_marcados)) +  ' - ' + str(int(media_gols_marcados + desvio_padrao_gols_marcados)))
        st.markdown('GOLS SOFRIDOS')
        st.text('Média: ' +  str(int(media_gols_sofridos)))
        st.text('Intervalo: ' + str(int(media_gols_sofridos - desvio_padrao_gols_sofridos)) +  ' - ' + str(int(media_gols_sofridos + desvio_padrao_gols_sofridos)))  
        st.markdown('MARCADOS + SOFRIDOS')
        st.text('Média: ' + str(int(media_gols_partida)))
        st.text('Intervalo: ' + str(int(media_gols_partida - desvio_padrao_gols_partida)) +  ' - ' + str(int(media_gols_partida + desvio_padrao_gols_partida)))  


    def indicador_escanteios(self):
        '''
        --> Mostra os indicadores referente aos escanteios
        '''
        #Escanteios
        media_escanteios = round(self.dados['escanteios'][:self.ultimos_jogos].mean())
        desvio_padrao_escanteios = round(self.dados['escanteios'][:self.ultimos_jogos].std())
        
        st.markdown('RESULTADOS')
        st.markdown(self.dados['resultado'][:self.ultimos_jogos].values)
        #Escanteios
        st.markdown('ESCANTEIOS')
        st.text('Média: ' +  str(int(media_escanteios)))
        st.text('Intervalo: ' + str(int(media_escanteios - desvio_padrao_escanteios)) +  '-' + str(int(media_escanteios + desvio_padrao_escanteios)))  

        
    def indicador_controle_jogo(self):
        '''
        --> Mostra os indicadores referente ao controle do jogo
        '''
        #Posse de bola
        media_posse_bola = round(self.dados['posse'][:self.ultimos_jogos].mean())
        desvio_padrao_posse_bola = round(self.dados['posse'][:self.ultimos_jogos].std())
        #Passes
        media_passes_certos = round(self.dados['passes_certos_%'][:self.ultimos_jogos].mean())
        desvio_padrao_passes_certos = round(self.dados['passes_certos_%'][:self.ultimos_jogos].std())

        st.markdown('RESULTADOS')
        st.markdown(self.dados['resultado'][:self.ultimos_jogos].values)
        #Posse de bola
        st.markdown('POSSE DE BOLA')
        st.text('Média: ' +  str(int(media_posse_bola)) + '%')
        st.text('Intervalo: ' + str(int(media_posse_bola - desvio_padrao_posse_bola)) + '%' +  ' - ' + str(int(media_posse_bola + desvio_padrao_posse_bola)) + '%')  
        #Passes
        st.markdown('PASSES CERTOS')
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
        #Visualização
        st.markdown('RESULTADOS')
        st.markdown(self.dados['resultado'][:self.ultimos_jogos].values)
        st.markdown('CHUTES AO GOL')
        st.text('Média: ' +  str(int(media_chutes_gol)) + '%')
        st.text('Intervalo: ' + str(int(media_chutes_gol - desvio_padrao_chutes_gol)) + '%' +  ' - ' + str(int(media_chutes_gol + desvio_padrao_chutes_gol)) + '%')    
        st.markdown('GOL POR CHUTE AO GOL')
        st.text('Média: ' +  str(int(media_gol_chutes_gol)) + '%')
        st.text('Intervalo: ' + str(int(media_gol_chutes_gol - desvio_padrao_gol_chutes_gol)) + '%' +  ' - ' + str(int(media_gol_chutes_gol + desvio_padrao_gol_chutes_gol)) + '%')    