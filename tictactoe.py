turn = "X"

map = [" ", " | ", " ", " | ", " ", "\n",
             " ", " | ", " ", " | ", " ", "\n",
             " ", " | ", " ", " | ", " ", "\n"]
mapstr = ""
for i in map:
    mapstr += i
    
print(mapstr)

while True:
    hod = input(f"ход игрока {turn}: ").lower()
    
    #aaaaaaaaaaaaaaaaaaaaaa
    if hod == "a1":
        if map[0] == " ":
            map[0] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
        
    elif hod == "a2":
        if map[2] == " ":
            map[2] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
            
    elif hod == "a3":
        if map[4] == " ":
            map[4] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
    
    #bbbbbbbbbbbbbbbbbb
    elif hod == "b1":
        if map[6] == " ":
            map[6] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
        
    elif hod == "b2":
        if map[8] == " ":
            map[8] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
            
    elif hod == "b3":
        if map[10] == " ":
            map[10] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
    
    #cccccccccccccccccccc
    elif hod == "c1":
        if map[12] == " ":
            map[12] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
        
    elif hod == "c2":
        if map[14] == " ":
            map[14] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
            
    elif hod == "c3":
        if map[16] == " ":
            map[16] = turn
            mapstr = ""
            for i in map:
                mapstr += i
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print(mapstr)
        else:
            print("Эта ячейка уже занята, выбери другую.\n")
    #не найденна
    else:
        print("неверное место для хода. прочитайте rules.txt !\n")