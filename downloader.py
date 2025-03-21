import os
from os import mkdir
#pyinstaller command: pyinstaller downloader.py --add-binary C:\Users\Pichau\AppData\Local\Programs\Python\Python313\Scripts\yt-dlp.exe:.
def main():
    print("Bem vindo ao donwloader de video 8001")
    print("-"*40)
    folder = outputDir()
    cmd = f'_internal\\yt-dlp.exe -P {folder} -f {fileExt()} {videoUrl()}'
    os.system(cmd)
    anotherOne()
    os.startfile(folder)

def fileExt():
    print(
        "Qual tipo de arquivo voce deseja?:\n"
        "1-Video e audio\n"
        "2-Apenas audio (m4a)\n"
        "3-Apenas audio (mp3)\n"
    )
    try:
        op = input()
        output = validInput(op)
    except ValueError as e:
        msgError(e)
        return fileExt()
    return output

def validInput(num):
    try:
        int(num)
    except ValueError:
        raise ValueError("Não foi digitado um numero")
    try:
        formats = {
            1: "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/b",
            2: "ba[ext=m4a]",
            3: "ba[ext=mp3]"
        }
        return formats[int(num)]
    except KeyError:
        raise ValueError("O numero digitado não é uma opção")

def outputDir():
    mypath = os.path.join(os.path.expanduser('~'), 'Videos', 'Downloader')
    if not os.path.exists(mypath):
        mkdir(mypath)
    return mypath

def videoUrl():
    url = input("Digite o link:\n")
    return url

def msgError(e):
    print("-"*40)
    print(f"Error: {e}")
    print("-"*40)

def anotherOne():
    again = ""
    again = input(
        "-"*40+
        "\nVoce deseja baixar outro video?\n"
        "Se sim digite s, se não digite qualquer outro valor\n"
        +"-"*40
    )
    if again.lower() == "s":
        return main()
main()