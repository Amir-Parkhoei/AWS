"""
__________________________________________________________________________________
|                                                                                 |
|                    Created by:                                                  |
|                    __________                                                   |
|                   /          \                                                  |
|                  /            \                                                 |
|                 |    TikTen    |                                                |
|                  \            /                                                 |
|                   \          /                                                  |
|                    \        /                                                   |
|                     \      /                                                    |
|                      \    /                                                     |
|                       \  /                                                      |
|                      \ \/ /                                                     |
|                       \--/                                                      |
|                        \/                                                       |
|                                                                                 |
|                     Powered by:                                                 |
|                     __________                                                  |
|                    /          \                                                 |
|                   /            \                                                |
|                  |    Python    |                                               |
|                   \            /                                                |
|                    \          /                                                 |
|                     \        /                                                  |
|                      \      /                                                   |
|                       \    /                                                    |
|                        \  /                                                     |
|                       \ \/ /                                                    |
|                        \--/                                                     |
|                         \/                                                      |
|                                                                                 |
|    _______________________________________________                              |
|   |                                              /                              |
|   |My Github: HTTPS://GITHUB.COM/FARBODPARKHOOI /                               |
|   |My Email: farbod.p1390@gmail.com            /                                |
|   |___________________________________________/                                 |
|                                                                                 |
|                                                                                 |
|              ___________          ______            __________                  |
|              ||                  /      \          |          |                 | 
|              ||                 /        \         |          |                 |
|              ----------        /          \        |__________|                 |
|              ||               /            \       |          \                 |
|              ||              /              \      |           \                |
|              ||             /----------------\     |            \               |
|              ||            /                  \    |             \              |
|              ||           /                    \   |              \             |
|              ||          /     _____________    \  |               \            |
|               __________      /             \         _____                     |
|              |          |    /               \       |      \                   |
|              |          |   /                 \      |       \                  |
|              |-----------  |                   |     |        |                 |
|              |           |  \                 /      |       /                  |
|              |           |   \               /       |      /                   |
|              |___________|    \_____________/        |_____/                    |
|_________________________________________________________________________________|
"""
def Create_Speech(Text, Speed, Name):
    try:
        import pyttsx3 
        engine = pyttsx3.init()
        engine.setProperty('rate', int(Speed))
        engine.save_to_file(Text, f"Files\\Sounds\\{Name}.mp3")
        engine.runAndWait()
    except:
        try:
            from tkinter import messagebox as message
            message.showerror("Error!", "You can't use this part")
        except:
            try:
                from os import startfile
                startfile(r"Files\Codes\Error msg.vbs")
            except:
                try:
                    from time import sleep as sp
                    print("You can't use this part!")
                    sp(10)
                    quit()
                except:
                    print("You can't use this part!")
                    quit()
def Download_Library():
    from os import system as osy
    print("Download started!")
    osy("pip install tk")
    osy("pip install pyttsx")
    osy("pip install pyttsx3")
    osy("cls")
    print("Download ended!")
def Send_Internet_Info(TF): # TF: True - False
        with open("Internet Info.txt", "w") as writer:
            writer.write(TF)
def Check_Internet():
    import socket
    REMOTE_SERVER = "www.google.com"
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2) 
        Send_Internet_Info("True")
    except:
        Send_Internet_Info("False")
def Read_Internet_Info():
    with open("Internet Info.txt", "r") as reader:
        reader = reader.readlines()
        reader = "".join(reader)
        if reader == "True": return True
        elif reader == "False": return False
        else: return "Unk"