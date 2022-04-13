import enum


def pasar_a_0(celdas):
    lista=[]

    for i in celdas:
        lista_aux=[]
        for char in i:   
            if char == '-':
                aux=0
            else:
                aux="B"
            lista_aux.append(aux)
        lista.append(lista_aux)
    return lista

def chequear_suma(tablero,i,j):
    pos=[(0,1),(1,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1)]
    for z in pos:
        x=i+z[0]
        y=j+z[1]
        if (type(tablero[i][j])!=int):
            if (x in [0,1,2,3]) and (y in [0,1,2,3,4]):
                if (type(tablero[x][y]) == int):
                    import pdb
                    pdb.set_trace()
                    tablero[x][y]+=1
                    print (tablero)
    

def sumar_bombas (tablero):
    for i,fila in enumerate(tablero):
        for j,columna in enumerate(fila):
            chequear_suma(tablero,i,j)

e=[
'-*-*-',
'--*--',
'----*',
'*----',
]
tablero=pasar_a_0(e)
sumar_bombas(tablero)
print (tablero)