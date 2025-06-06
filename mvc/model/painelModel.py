import pandas as pd
import os
import win32com.client
import sys

class PainelModel:
    
    def get_tempo():
        
        df = pd.read_csv('tempos.csv')
        
        for index, row in df.iterrows():
            tempo, texto = row['tempo'], row['texto']
            
            # Subistituir o texto pelo texto criado
            texto = PainelModel.criar_texto(tempo)
            df.loc[index, 'texto'] = texto
            
        df.to_csv('tempos.csv', index=False)
        
        lista_tempo = df['tempo'].tolist()
        lista_texto = df['texto'].tolist()
        
        return(lista_tempo, lista_texto)
                 
    def criar_texto(tempo):
        # Converte o tempo em segundos para horas, minutos e segundos
        if tempo // 60 > 0:
            horas = tempo // 3600
            minutos = (tempo % 3600) // 60
            segundos = tempo % 60
            
            texto = f"{int(horas)} hora(s) {int(minutos)} minuto(s) e {int(segundos)} segundo(s)"
            
            if horas == 0 and minutos == 0:
                texto = f"{int(segundos)} segundo(s)"
                return texto
            elif horas == 0 and segundos == 0:
                texto = f"{int(minutos)} minuto(s)"
                return texto
            elif minutos == 0 and segundos == 0:
                texto = f"{int(horas)} hora(s)"
                return texto            
            if segundos == 0:
                texto = f"{int(horas)} hora(s) e {int(minutos)} minuto(s)"
                return texto
            elif minutos == 0:
                texto = f"{int(horas)} hora(s) e {int(segundos)} segundo(s)"
                return texto
            elif horas == 0:
                texto = f"{int(minutos)} minuto(s) e {int(segundos)} segundo(s)"
                return texto
            else:
                return texto
        elif tempo < 60:
            texto = f"{int(tempo)} segundo(s)"
            return texto

    def deletar_tempo(id):
        df = pd.read_csv('tempos.csv')
        df.drop(id, inplace=True)
        df.to_csv('tempos.csv', index=False)
        return df
    
    def adicionar_tempo(tempo):
        df = pd.read_csv('tempos.csv')
        texto = PainelModel.criar_texto(tempo)
        
        linha_nova = {'tempo': tempo, 'texto': texto}
        
        df = pd.concat([df, pd.DataFrame([linha_nova])], ignore_index=True)
        df.to_csv('tempos.csv', index=False)             

    def resetar_padrao():
        df = pd.read_csv('tempos.csv')
        df.drop(df.index, inplace=True)
        
        tempos_padrao = [
            {'tempo': 10800, 'texto': '3 horas'},
            {'tempo': 7200, 'texto': '2 horas'},
            {'tempo': 3600, 'texto': '1 hora'},
            {'tempo': 1800, 'texto': '30 minutos'},
            {'tempo': 600, 'texto': '10 minutos'},
        ]
        
        df = pd.concat([df, pd.DataFrame(tempos_padrao)], ignore_index=True)
        
        df.to_csv('tempos.csv', index=False)
              
    def iniciar_com_sistema():
        startup_path = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        caminho_do_atalho = os.path.join(startup_path, "Time to stop.exe.lnk")
        if os.path.exists(caminho_do_atalho):
            return True        
        return False
    
    def criar_atalho_startup(check):
        caminho_do_programa = os.path.abspath(sys.executable)
        startup_path = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        caminho_do_atalho = os.path.join(startup_path, "Time to stop.exe.lnk")
        
        if check:
            shell = win32com.client.Dispatch("WScript.Shell")
            atalho = shell.CreateShortCut(caminho_do_atalho)
            atalho.Targetpath = caminho_do_programa
            atalho.Arguments = "--tray"
            atalho.WorkingDirectory = os.path.dirname(caminho_do_programa)
            atalho.IconLocation = caminho_do_programa
            atalho.save()
            print("Tray está ativado e está no startup")
                
        else:
            if os.path.exists(caminho_do_atalho):
                os.remove(caminho_do_atalho)
                print("Tray está desativado e foi removido do startup")
            else:
                print("Tray não está ativado e não está no startup")
                    
    def comando_desligar(texto):
        df = pd.read_csv('tempos.csv')     
        segundos = df[df['texto'] == str(texto)]['tempo'].values[0]
        os.system(f"shutdown -s -t {segundos}")
        print(f"Desligar em {segundos} segundos")
