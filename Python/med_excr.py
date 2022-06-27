
def get_neigs(pos):
    fila = pos[0]
    col = pos[1]
    neigs=[]
    if fila>0: #arriba
        neigs.append((fila-1,col))
    if fila<4: #arriba
        neigs.append((fila+1,col))
    if col>0:
        neigs.append((fila,col-1))
    if col<4:
        neigs.append((fila,col+1))
    return neigs



def evalute_neigh(positions_l):
    marked = set()
    rivers=[]
    for pos_t in positions_l:
        if pos_t not in marked:
            river=[]
            stack=[pos_t]
            while stack:
                current = stack.pop()
                if current not in marked:
                    river.append(current)
                    marked.add(current)
                    neigbors=get_neigs(current)
                    for n in neigbors:
                        if n in positions_l:
                            stack.append(n)
            rivers.append(river)

    return rivers

def main(arreglo):
    fila_n=0
    item_n=0
    pos =[]
    for fila in arreglo:
        for item in fila:
            if item ==1:
                pos.append((fila_n,item_n))
            item_n=item_n+1
        item_n = 0
        fila_n=fila_n+1
    return pos



arr = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]
]
returnn=main(arr) #nos regresa pos [fila,col]

sols= evalute_neigh(returnn)
print(len(sols))
for sol in sols:
    print(len(sol))


#solution generete list of lists 