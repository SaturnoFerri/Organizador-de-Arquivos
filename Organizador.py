import os
import shutil

#O caminho da pasta que você quer organiza
camin = "C:/Users/Seu_Usuario/test"

arquivos_cami = []
fotos = []
vídeo = []
documento = []
documentos_programação_banco_de_dados = []
documentos_programação_web = []
documentos_programação_scripts_e_altomaçõs = []

#As extensões, são adicionadas aqui:
extensão_fotos = ".jpg", ".png", ".jpeg", ".JPG", ".PNG", ".JPEG"
extensão_documentos = ".docx", ".doc", ".rtf", ".pdf", ".xlsx", ".xls", ".ods", ".pptx", ".ppt", ".txt"
extensão_vídeos = ".mp4", ".mov", ".avi", ".mkv", ".wmv", ".webm", ".flv"
#extensão_documentos_programação = ".html", ".php", ".py", ".js", ".json",
extensão_documentos_programação_banco_de_dados = ".sql", ".pls", ".plsql", ".json"
extensão_documentos_programação_web = ".html", ".htm", ".css", ".js", ".jsx", ".ts", ".tsx", ".php", ".rb", ".cs", ".cshtml"
extensão_documentos_programação_scripts_e_altomaçõs = ".py", ".sh", ".bash", ".ps1", ".pl", ".groovy"

#Esse loop, passa por toda pasta e subpasta, na região que você definiu
for root, dirs, arquivo in os.walk(camin):
    for arquivos in arquivo:
        caminho = os.path.join(root, arquivos)
        caminho_ce = os.path.normpath(caminho)
        arquivos_cami.append(caminho_ce.lower())
        
        #todos os arquivos que encontra ele vai adicionar nas lista, respectiva do arquivo(ele faz essa analize pela extensão do arquivo)
        if caminho_ce.endswith(extensão_fotos):
            fotos.append(caminho_ce)
        elif caminho_ce.endswith(extensão_documentos):
            documento.append(caminho_ce)
        elif caminho_ce.endswith(extensão_vídeos):
            vídeo.append(caminho_ce)
        elif caminho_ce.endswith(extensão_documentos_programação_banco_de_dados):
            documentos_programação_banco_de_dados.append(caminho_ce)
        elif caminho_ce.endswith(extensão_documentos_programação_scripts_e_altomaçõs):
            documentos_programação_scripts_e_altomaçõs.append(caminho_ce)
        elif caminho_ce.endswith(extensão_documentos_programação_web):
            documentos_programação_web.append(caminho_ce)

#Esses loops são o que vão organizar os arquivos:
for foto in fotos:
    pasta1 = f"{camin}/fotos"
    destino1 = os.path.join(pasta1, os.path.basename(foto))
    
    #verifica se exite alguma pasta chamada fotos
    if os.path.isdir(pasta1):
        
        #Verifica se tem algum arquivo com o mesmo nome na pasta que vai ser adicionada 
        if not os.path.exists(destino1):
            #move o arquivo para pasta criada
            shutil.move(foto, pasta1)
        
        #Se já exite o arquivo ele passa, para o proximo
        else:
            continue

    #Se não tiver nehuma pasta chamada fotos ele cria e depois move todos os arquivos fotos para essa pasta
    else:
        os.mkdir(f"{camin}/fotos")
        shutil.move(rf"{foto}", pasta1)

#O mesmo processo, só que o nome da pasta diferente e agora com vídeos
for vídeos in vídeo:
    pasta2 = f"{camin}/vídeos"
    destino2 = os.path.join(pasta2, os.path.basename(vídeos))
    if os.path.isdir(pasta2):
        if not os.path.exists(destino2):
            shutil.move(vídeos, pasta2)
        
        else:
            continue
    else:
        os.mkdir(f"{camin}/vídeos")
        shutil.move(vídeos, pasta2)

for documentos in documento:
    pasta3 = f"{camin}/documentos"
    destino3 = os.path.join(pasta3, os.path.basename(documentos))
    if os.path.isdir(pasta3):
        if not os.path.exists(destino3):
            shutil.move(documentos, pasta3)
        else:
            continue
    else:
        os.mkdir(f"{camin}/documentos")
        shutil.move(documentos, pasta3)

for documento_programação_banco_dados in documentos_programação_banco_de_dados:
    pasta4 = f"{camin}/programação_banco_de_dados"
    destino4 = os.path.join(pasta4, os.path.basename(documento_programação_banco_dados))
    
    if os.path.isdir(pasta4):
        if not os.path.exists(destino4):
            shutil.move(documento_programação_banco_dados, pasta4)
        else:
            continue

    else:
        os.mkdir(pasta4)
        shutil.move(documento_programação_banco_dados, pasta4)
    
for documento_programação_web in documentos_programação_web:
    pasta5 = f"{camin}/programação_web"
    destino5 = os.path.join(pasta5, os.path.basename(documento_programação_web))
    
    if os.path.isdir(f"{camin}/programação_web"):
        if not os.path.exists(destino5):
            shutil.move(documento_programação_web, pasta5)
        else:
            continue
    else:
        os.mkdir(f"{camin}/programação_web")
        shutil.move(documento_programação_web, pasta5)

for documento_programação_scripts_e_altomações in documentos_programação_scripts_e_altomaçõs:
    pasta6 = f"{camin}/programação_scripts_e_altomações"
    destino6 = os.path.join(pasta6, os.path.basename(documento_programação_scripts_e_altomações))
    
    if os.path.isdir(pasta6):
        if not os.path.exists(destino6):
            shutil.move(documento_programação_scripts_e_altomações, pasta6)
        else:
            continue   
    else:
        os.mkdir(f"{camin}/programação_scripts_e_altomações")
        shutil.move(documento_programação_scripts_e_altomações, pasta6)
