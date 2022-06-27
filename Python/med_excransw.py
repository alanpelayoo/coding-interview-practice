
def main(arreglo):
    marked=set()
    river=[]
    for row in range(len(arreglo)):
        for col in range(len(arreglo[row])):
            if arreglo[row][col]==1 and (row,col) not in marked:
                cur_river_len=1
                marked.add((row,col))
                stack=[(row,col)]
                while stack:
                    current = stack.pop()
                    neighbors = get_neights(current,arreglo)
                    for n in neighbors:
                        y,x=n
                        if arreglo[y][x] ==1 and (y,x) not in marked:
                            marked.add((y,x))
                            cur_river_len +=1
                            stack.append((y,x))
            river.append(cur_river_len)
    return  river


def get_neights(pos,matrix):
    y,x=pos
    ns=[]
    if x >=1:
        ns.append((y,x-1))#left neigh

    if x< len(matrix[0])-1: #right
        ns.append((y,x+1))

    if y >=1:#top
        ns.append((y-1,x))#top

    if y < len(matrix)-1:#bot
        ns.append((y+1,x))
    return ns


arr = [
    [1,1,0,1,0],
    [1,0,1,0,0],
    [0,1,1,0,1],
    [0,0,1,0,1],
    [1,0,1,1,0]
]
out =main(arr)
print(out)
