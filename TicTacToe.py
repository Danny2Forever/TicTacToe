board=[[' ',' ',' '],
       [' ',' ',' '],
       [' ',' ',' ']]
win = False
turn = "X"

def checkwin():
    global running 
    winlst=[]
    for j in range(len(board)): # check for rows (3)
        for k in range(len(board)):
            winlst.append(board[j][k])
        result = winlst.count(winlst[0]) == len(winlst)
        if (result and ' ' not in winlst):
            print("You win !!!")
            running = False
        winlst=[]
    
    for l in range(len(board)):
        for m in range(len(board)): # check for diagonal (2)
            winlst.append(board[m][l])
        result = winlst.count(winlst[0]) == len(winlst)
        if (result and ' ' not in winlst):
            print("You win !!!")
            running = False
        winlst=[]

    z = 0
    for n in range(2):
        for o in range(3):
            winlst.append(board[z][z])
            if n == 0:
                z+=1
            else:
                z-=1
        result = winlst.count(winlst[0]) == len(winlst)
        if (result and ' ' not in winlst):
            print("You win !!!")
            running = False
        winlst=[]
        z=2

running = True
while running :
    for i in range(len(board)):
        print(board[i])
        
    x = int(input("Let's choose column : "))
    y = int(input("Let's choose row : "))

    if x < 1 or x > 3 :
        x = int(input("Let's choose column : "))
    if y < 1 or y > 3 :   
        y = int(input("Let's choose row : ")) 

    while board[y-1][x-1] == " " :
        if board[y-1][x-1] == " ":
            board[y-1][x-1] = turn
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
        else:
            x = int(input("Let's choose column : "))
            y = int(input("Let's choose row : "))
    
    checkwin()