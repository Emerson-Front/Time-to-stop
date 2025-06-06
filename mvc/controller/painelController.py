from mvc.model.painelModel import PainelModel

class PainelController:
    def __init__(self):
        self.get_tempo()
    
    def get_tempo(self):
        lista_tempo, lista_texto = PainelModel.get_tempo()
        
        lista_tempo_texto = []
        for tempo, texto in zip(lista_tempo, lista_texto):
            lista_tempo_texto.append([tempo, texto])
            
        return lista_tempo_texto
    
    def deletar_tempo(self, id):
        print('Deletando o tempo com id:', id)
        PainelModel.deletar_tempo(id)
    
    def adicionar_tempo(self, tempo):
        print('Adicionando o tempo:', tempo)
        PainelModel.adicionar_tempo(tempo)
        
    def resetar_padrao(self):
        print('Resetando o padrão')
        PainelModel.resetar_padrao()
        
    def iniciar_com_sistema(self):
        return PainelModel.iniciar_com_sistema()
    
    def criar_atalho_startup(self, parametro):
        print('Criando atalho no startup')
        PainelModel.criar_atalho_startup(parametro)