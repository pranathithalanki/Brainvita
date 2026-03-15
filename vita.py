def printing(l):
    for row in l:
        for el in row:
            if el==-1:
                print(".",end=" ")
            elif el==1:
                print("O",end=" ")
            else:
                print("0",end=" ")
        print()

def counting(l):
    c=0
    for row in l:
        for el in row:
            if el==1:
                c+=1
    return c
            
def moves(l):
    for i in range(7):
        for j in range(7):
            if l[i][j] == 1:
                if j <= 4 and l[i][j+1] == 1 and l[i][j+2] == 0:
                    return True
                if j >= 2 and l[i][j-1] == 1 and l[i][j-2] == 0:
                    return True
                if i <= 4 and l[i+1][j] == 1 and l[i+2][j] == 0:
                    return True
                if i >= 2 and l[i-1][j] == 1 and l[i-2][j] == 0:
                    return True
    return False

li = [[-1,-1,1,1,1,-1,-1],
      [-1,-1,1,1,1,-1,-1],
      [1,1,1,1,1,1,1],
      [1,1,1,0,1,1,1],
      [1,1,1,1,1,1,1],
      [-1,-1,1,1,1,-1,-1],
      [-1,-1,1,1,1,-1,-1]]

printing(li)
print("Rules of the Game:")
print("1. The '.' means there is no marble there or cannot move a marble there")
print("2. The 'O' means that a marble is present there")
print("3. The '0' represents an empty space")
print("4. To exit the game, type exit")

while True:
    userc=input("Enter your moves like this '3 R 1', which means move marble at 3rd row, 1st column to the right: ").upper().split()
    if userc==["EXIT"]:
        print("Successfully exited the game")
        print("Number of marbles left:", counting(li))
        break
    if len(userc)!=3:
        print("You have entered less than 3, please enter more")
        continue
    
    r,d,c=userc
    a=int(r)-1
    b=int(c)-1

    if d=="U":
        if a>=2 and li[a][b]==1 and li[a-1][b]==1 and li[a-2][b]==0:
            li[a][b]=0
            li[a-1][b]=0
            li[a-2][b]=1
        else:
            print("Move Invalid")

    elif d=="R":
        if b<=4 and li[a][b]==1 and li[a][b+1]==1 and li[a][b+2]==0:
            li[a][b]=0
            li[a][b+1]=0
            li[a][b+2]=1
        else:
            print("Move Invalid")

    elif d=="L":
        if b>=2 and li[a][b]==1 and li[a][b-1]==1 and li[a][b-2]==0:
            li[a][b]=0
            li[a][b-1]=0
            li[a][b-2]=1
        else:
            print("Move Invalid")

    elif d=="D":
        if a<=4 and li[a][b]==1 and li[a+1][b]==1 and li[a+2][b]==0:    
            li[a][b]=0
            li[a+1][b]=0
            li[a+2][b]=1
        else:
            print("Move Invalid")

    else:
        print("Invalid direction. Use U, D, L or R")
        continue

    printing(li)

    if not moves(li):
        print("No more moves left! Game over!")
        print("Number of marbles left:", counting(li))
        break