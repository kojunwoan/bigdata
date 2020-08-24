players = "sys:print:12:[1,5]:1:1:sys:selectPlayer:[1,2]"
for idx,msg in enumerate(players.split("sys")):
    print(idx,msg)
    for submsg in msg.split(":"):
        print(submsg)