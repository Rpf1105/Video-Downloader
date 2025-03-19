import os
from os import mkdir


def main():
    print("Bem vindo ao donwloader de video 8001")
    print("-"*40)
    folder = outputDir()
    cmd = f'yt-dlp -P {folder} -f {fileExt()} {videoUrl()}'
    os.system(cmd)
    os.startfile(folder)

def fileExt():
    print(
        "Qual tipo de arquivo voce deseja?:\n"
        "1-Video e audio\n"
        "2-Apenas audio"
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
            1: "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b",
            2: "ba[ext=m4a]"
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

main()