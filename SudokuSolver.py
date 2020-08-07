import os
import glob

folder=r'C:\Users\Hp\Desktop\Project\Sudoku\\'

#Prepares the grid
def toGrid(path):
    grid=[]
    f=open(path,"r")
    for i in f.readlines():
        a=[]
        for j in i.split():
            a.append(int(j))
        grid.append(a)
    return grid

#Convert the grid to a string 
def toStr(grid):
    s=''
    for i in range(9):
        for j in range(9):
            s+=str(grid[i][j])
            s+=' '
        s+='\n'
    return s


grid=toGrid(folder+r'input.txt');

#check if n is possible in position grid[y][x]
def isPossible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range(0,9):
        if grid[i][x]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False
    return True

#Copy the grid to the Output file
i=1 #increment the output text filename
def toOutput(s):
    global i,folder
    path = folder+r'Outputs\\'
    f = open(path+str(i)+'.txt', 'w')
    f.write(s)
    f.close()
    i+=1
    return


#Solves the grid using recursion
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if isPossible(y,x,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    
    s=toStr(grid)
    toOutput(s)



files = glob.glob(folder+r'Outputs\*')
for f in files:
    os.remove(f)

solve()            