import mvc.controller.painelController as PainelController
import webview

class Iniciar_webview:
    def __init__(self):
        
        webview.create_window('Time to Stop', 'mvc/view/painel_controle.html', js_api=PainelController.PainelController(), width=800, height=700)
        webview.start()

