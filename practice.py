maze=[[0 for i in range(10)]for j in range(10)]
for i in range(10):
    maze[i]=list(map(int,input().split()))

x,y=1

while True:
    if maze[x][y+1]==0:
        maze[x][y]=9
        y+=1
    elif maze[x+1][y]==0:
        maze[x][y]=9
        x+=1
    elif maze[x][y+1]==2:
        maze[x][y]=9
        maze[x][y+1]=9
        break
    elif maze[x+1][y]==2:
        maze[x][y]=9
        maze[x+1][y]=9
        break
    else:
        maze[x][y]=9
        break

for i in range(len(maze)):
    print(' '.join(map(str,maze[i])))