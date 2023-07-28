with open("Lib-Info.txt", "r") as reader:
    reader = reader.readlines()
    reader = "".join(reader)
    if reader == "Com":
        from script import Check_Internet
        from script import Read_Internet_Info
        Check_Internet()
        