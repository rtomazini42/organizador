import os

print("Bem vindo! É na pasta que você está rodando o script que você quer organizar?")
resposta = input("Responda 1 para sim: ")

if resposta != "1":
    print("bye")
    exit(0)

print("Rodando")
os.makedirs("Audio", exist_ok=True)
os.makedirs("Executavel", exist_ok=True)
os.makedirs("Textos", exist_ok=True)
os.makedirs("Imagens", exist_ok=True)
os.makedirs("Video", exist_ok=True)
os.makedirs("Torrent", exist_ok=True)
os.makedirs("Scripts", exist_ok=True)
os.makedirs("Zips", exist_ok=True)
os.makedirs("Outros", exist_ok=True)
os.makedirs("Organizador", exist_ok=True)

os.rename("organizador.py", "Organizador/organizador.py")
os.rename("readme.md", "Organizador/readme.md")

for file in os.listdir():
    if file.endswith((".mp3", ".ogg", ".flac", ".acc", ".wma", ".alac", ".aiff", ".pcm", ".wav")):
        os.rename(file, "Audio/" + file)
    elif file.endswith((".deb", ".app", ".iso", ".exe")):
        os.rename(file, "Executavel/" + file)
    elif file.endswith((".epub", ".txt", ".pdf")):
        os.rename(file, "Textos/" + file)
    elif file.endswith((".jpg", ".png", ".bmp", ".jpeg", ".svg", ".gif")):
        os.rename(file, "Imagens/" + file)
    elif file.endswith((".mp4", ".flv", ".mpeg", ".webm", ".mkv", ".vob", ".ogv", ".avi", ".MTS", ".mov", ".rm", ".rmvb", ".viv", ".amv", ".mpg", ".m4p", ".m4v", ".mpe", ".m2v", ".svi", ".3gp", ".3g2")):
        os.rename(file, "Video/" + file)
    elif file.endswith((".torrent", ".magnet")):
        os.rename(file, "Torrent/" + file)
    elif file.endswith((".py", ".sh", ".cpp", ".js", ".rs", "*rslib")):
        os.rename(file, "Scripts/" + file)
    elif file.endswith((".zip", ".rar")):
        os.rename(file, "Zips/" + file)
    elif os.path.isfile(file):
        os.rename(file, "Outros/" + file)

print("Deletar pastas e arquivos vazios?")
deletar = input("Responda 1 para sim: ")

if deletar == "1":
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            folder = os.path.join(root, name)
            if not os.listdir(folder):
                os.rmdir(folder)
    for file in os.listdir():
        if os.path.isfile(file):
            os.remove(file)

print("Feito")
print("Obrigado por usar!")
