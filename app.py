from mvc.controller.painelController import PainelController
from mvc.controller.trayController import TrayController
from core.iniciar_webview import Iniciar_webview
import os, sys
import pandas as pd


if not os.path.exists('tempos.csv'):
    print('Arquivo não encontrado, criando...')
    df = pd.DataFrame(columns=['tempo', 'texto'])
    df.to_csv('tempos.csv', index=False)
    # Se os arquivos não existem, cria-os
    resetar = PainelController()
    resetar.resetar_padrao()


if __name__ == '__main__':
    
    PainelController()
    
    if '--tray' in os.sys.argv:
        TrayController()
        sys.exit()
    
    Iniciar_webview()
    
    TrayController()
