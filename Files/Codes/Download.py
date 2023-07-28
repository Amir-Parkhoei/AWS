with open("Lib-Info.txt", "r") as reader:
    reader = reader.readlines()
    reader = "".join(reader)
    if reader == "Com":
        from script import Check_Internet
        from script import Read_Internet_Info
        from script import Download_Library
        Check_Internet()
        Def = Read_Internet_Info()
        if Def == True: Download_Library()
        else: print("Connect to internet and try again later."), quit()