try:
    from script import Create_Speech
    from script import Get_Text
    from script import Get_Name
    text = Get_Text()
    name = Get_Name()
    Create_Speech(Text=Def, Speed=125, Name="")
    try:
        from tkinter import *
    except:
        try:
            from os import startfile
            startfile(r"Files\Codes\Download.py")
            with open(r"Files\Codes\Lib-Info.txt", "w") as writer:
                writer.write("Com")
        except:
            try:
                from time import sleep as sp
                print("I can't start software.")
                sp(10)
                quit()
            except:
                print("I can't start software.")
                quit()
except:
    try:
        from tkinter import messagebox as message
        message.showerror("Error!", "I can't find a file!")
        quit()
    except:
        try:
            from os import startfile
            startfile(r"Files\Codes\Error msg2.vbs")
            quit()
        except:
            try:
                from time import sleep as sp
                print("I can't find a file!")
                sp(10)
                quit()
            except:
                print("I can't find a file!")
                quit()
