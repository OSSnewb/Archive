d=[]
for i in range(10):
    b=list(map,(int,(input().split())))
    d.append(b)

x,y=1
while True:
    if(d[x][y]==0):
        d[x][y]=9
    elif(d[x][y]==2):
        d[x][y]==9
        break #영역 표시
    if (d[x][y+1]!=1):
        y=y+1
    elif(d[x+1][y]!=1):
        x=x+1
    if(d[x][y+1]==1 and d[x+1][y]==1):
        break

for i in range(10):
    for j in range(10):
        print(d[i][j],end=" ")
    print("")

    
