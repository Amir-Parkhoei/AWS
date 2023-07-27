"""
      Created by:           
      __________
     /          \
    /            \
   |    TikTen    |
    \            /
     \          /
      \        /
       \      /
        \    /
         \  /
        \ \/ /
         \--/
          \/

      Powered by:
      __________
     /          \
    /            \
   |    Python    |
    \            /
     \          /
      \        /
       \      /
        \    /
         \  /
        \ \/ /
         \--/
          \/
        
     _______________________________________________
    |                                              /
    |My Github: HTTPS://GITHUB.COM/FARBODPARKHOOI /
    |My Email: farbod.p1390@gmail.com            /
    |___________________________________________/
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