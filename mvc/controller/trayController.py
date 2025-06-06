from mvc.model.painelModel import PainelModel
from core.iniciar_webview import Iniciar_webview
from pystray import Icon, Menu, MenuItem
from PIL import Image
import os, sys



class TrayController:
    def __init__(self):
        self.iniciar_tray()
    
        
    def iniciar_tray(self):
        """
        Inicia o ícone na system tray com opções baseadas nos tempos.
        """
        lista_tempo, lista_texto = PainelModel.get_tempo()
             
        dicionario = {lista_tempo[i]: lista_texto[i] for i in range(len(lista_tempo))}
        dicionario = dict(sorted(dicionario.items(), reverse=True))
        valores = list(dicionario.values())

        image = Image.open(self.recurso_caminho('mvc/view/img/icon_tray.png'))
        icone = Icon('Time to Stop', image)
        
        menu_itens = []
        menu_itens.append(MenuItem("Abrir painel", lambda icon, item: Iniciar_webview()))
        
        for i in range(len(dicionario)):
            menu_itens.append(MenuItem(valores[i], lambda icon, item: PainelModel.comando_desligar(item)))
            
        menu_itens.append(MenuItem("Cancelar", lambda icon, item: os.system("shutdown -a")))
        menu_itens.append(MenuItem("Sair", lambda icon, item: os._exit(0)))

        icone.menu = Menu(*menu_itens)

        icone.run()
        
    def recurso_caminho(self, rel_path):
        """Resolve o caminho de arquivos tanto no modo normal quanto empacotado"""
        if getattr(sys, 'frozen', False):  # executável gerado pelo pyinstaller
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, rel_path)
