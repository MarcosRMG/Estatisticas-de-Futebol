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
        #Gols partida
        media_gols_partida = round(self.dados['gols_partida'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_partida = round(self.dados['gols_partida'][:self.ultimos_jogos].std())
        mais_frequente_gols_partida_list = self.dados['gols_partida'][:self.ultimos_jogos].mode().values
        #Gols marcados
        media_gols_marcados = round(self.dados['gols_marcados'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_marcados = round(self.dados['gols_marcados'][:self.ultimos_jogos].std())
        mais_frequente_gols_marcados_list = self.dados['gols_marcados'][:self.ultimos_jogos].mode().values
        #Gols sofridos
        media_gols_sofridos = round(self.dados['gols_sofridos'][:self.ultimos_jogos].mean())
        desvio_padrao_gols_sofridos = round(self.dados['gols_sofridos'][:self.ultimos_jogos].std())
        mais_frequente_gols_sofridos_list = self.dados['gols_sofridos'][:self.ultimos_jogos].mode().values
        
        #Visualizações
        #Gols marcados
        st.markdown('**GOLS MARCADOS**')
        st.text('Média: ' +  str(media_gols_marcados))
        st.text('Variação: ' + str(media_gols_marcados - desvio_padrao_gols_marcados) +  ' - ' + str(media_gols_marcados + desvio_padrao_gols_marcados))
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
        st.text('Variação: ' + str(media_gols_sofridos - desvio_padrao_gols_sofridos) +  ' - ' + str(media_gols_sofridos + desvio_padrao_gols_sofridos)) 
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
        st.text('Variação: ' + str(media_gols_partida - desvio_padrao_gols_partida) +  ' - ' + str(media_gols_partida + desvio_padrao_gols_partida))
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
        st.text('Média: ' +  str(media_escanteios))
        st.text('Variação: ' + str(media_escanteios - desvio_padrao_escanteios) +  '-' + str(media_escanteios + desvio_padrao_escanteios))  
        
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
        st.text('Média: ' +  str(media_escanteios))
        st.text('Variação: ' + str(media_escanteios - desvio_padrao_escanteios) +  '-' + str(media_escanteios + desvio_padrao_escanteios))
        
        mais_frequente_escanteio_str = str()
        for i in range(len(mais_frequente_escanteio_list)):
            if i == 0:
                mais_frequente_escanteio_str = str(int(mais_frequente_escanteio_list[i]))
            else:
                mais_frequente_escanteio_str = mais_frequente_escanteio_str + ' - ' + str(int(mais_frequente_escanteio_list[i]))
        st.text('Mais Frequênte: ' + mais_frequente_escanteio_str)


    def indicador_cartoes(self):
        '''
        --> Indicador do número de cartões vermelhos e amarelos
        '''
        #Variáveis
        media_cartoes = round((self.dados['cartoes_amarelos'] + self.dados['cartoes_vermelhos']).mean())
        desvio_padrao_cartoes = round((self.dados['cartoes_amarelos'] + self.dados['cartoes_vermelhos']).std())
        media_cartao_amarelo = round(self.dados['cartoes_amarelos'][:self.ultimos_jogos].mean())
        desvio_padrao_cartao_amarelo = round(self.dados['cartoes_amarelos'][:self.ultimos_jogos].std())
        media_cartao_vermelho = round(self.dados['cartoes_vermelhos'][:self.ultimos_jogos].mean())
        desvio_padrao_cartao_vermelho = round(self.dados['cartoes_vermelhos'][:self.ultimos_jogos].std())

        #Visualização
        st.markdown('**CARTÕES**')
        st.text('Média: ' +  str(media_cartoes))
        st.text('Variação: ' + str(media_cartoes - desvio_padrao_cartoes) +  '-' + str(media_cartoes + desvio_padrao_cartoes))

        st.markdown('**CARTÕES AMARELOS**')
        st.text('Média: ' +  str(media_cartao_amarelo))
        st.text('Variação: ' + str(media_cartao_amarelo - desvio_padrao_cartao_amarelo) +  '-' + str(media_cartao_amarelo + desvio_padrao_cartao_amarelo))

        st.markdown('**CARTÕES VERMELHOS**')
        st.text('Média: ' +  str(media_cartao_vermelho))
        st.text('Variação: ' + str(media_cartao_vermelho - desvio_padrao_cartao_vermelho) +  '-' + str(media_cartao_vermelho + desvio_padrao_cartao_vermelho))
        

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
        st.text('Média: ' +  str(media_posse_bola) + '%')
        st.text('Intervalo: ' + str(media_posse_bola - desvio_padrao_posse_bola) + '%' +  ' - ' + str(media_posse_bola + desvio_padrao_posse_bola) + '%')  
        st.markdown('**PASSES CERTOS**')
        st.text('Média: ' +  str(media_passes_certos) + '%')
        st.text('Variação: ' + str(media_passes_certos - desvio_padrao_passes_certos) + '%' +  ' - ' + str(media_passes_certos + desvio_padrao_passes_certos) + '%')  


    def indicador_ofensividade(self):
        '''
        --> Mostra os indicadores de ofensividade
        :param dados: DataFrame com o números das rodadas da liga
        :param ultimos_jogos: Seleção do número de jogos anteriores para cálculo dos indicadores
        '''
        #Variáveis
        media_chutes_gol = round(self.dados['chutes_a_gol_%'][:self.ultimos_jogos].mean())
        desvio_padrao_chutes_gol = round(self.dados['chutes_a_gol_%'][:self.ultimos_jogos].std())
        media_chutes_por_gol = round(self.dados['chutes_por_gol'][:self.ultimos_jogos].mean())
        desvio_padrao_chutes_por_gol = round(self.dados['chutes_por_gol'][:self.ultimos_jogos].std())
        media_chutes = round(self.dados['total_chutes'][:self.ultimos_jogos].mean())
        desvio_padrao_chutes = round(self.dados['total_chutes'][:self.ultimos_jogos].std())
        
        #Visualização
        st.markdown('**TOTAL DE CHUTES**')
        st.text('Média: ' + str(media_chutes))
        st.text('Variação: ' + str(media_chutes - desvio_padrao_chutes) +  ' - ' + str(media_chutes + desvio_padrao_chutes))    
        st.markdown('**CHUTES NO GOL**')
        st.text('Média: ' +  str(media_chutes_gol) + '%')
        st.text('Variação: ' + str(media_chutes_gol - desvio_padrao_chutes_gol) + '%' +  ' - ' + str(media_chutes_gol + desvio_padrao_chutes_gol) + '%')    
        st.markdown('**NÚMERO DE CHUTES PARA CADA GOL**')
        st.text('Média: ' +  str(int(media_chutes_por_gol)))
        st.text('Variação: ' + str(media_chutes_por_gol - desvio_padrao_chutes_por_gol) +  ' - ' + str(media_chutes_por_gol + desvio_padrao_chutes_por_gol))    
    

    def indicador_defesa(self):
        '''
        --> Indicadores do sistema defensivo
        '''
        media_chutes_contra_gol = round(self.dados['chutes_contra_o_gol'][:self.ultimos_jogos].mean())
        desvio_padrao_chutes_contra_gol = round(self.dados['chutes_contra_o_gol'][:self.ultimos_jogos].std())
        media_defesas = round(self.dados['defesas_%'][:self.ultimos_jogos].mean())
        desvio_padrao_defesas = round(self.dados['defesas_%'][:self.ultimos_jogos].std())
        media_sem_vazamento = round(self.dados['sem_vazamento'][:self.ultimos_jogos].mean())
        desvio_padrao_sem_vazamento = round(self.dados['sem_vazamento'][:self.ultimos_jogos].std())
        
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
