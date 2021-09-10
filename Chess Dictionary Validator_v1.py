firstboard={'a8':'wrook','b8':'wknight','c8':'wbishop','d8':'wqueen','e8':'wking','f8':'wbishop','g8':'wknight','h8':'wrook',
            'a7':'wpawns','b7':'wpawns','c7':'wpawns','d7':'wpawns','e7':'wpawns','f7':'wpawns','g7':'wpawns','h7':'wpawns',
            'a1':'brook','b1':'bknight','c1':'bbishop','d1':'bqueen','e1':'bking','f1':'bbishop','g1':'bknight','h1':'brook',
            'a2':'bpawns','b2':'bpawns','c2':'bpawns','d2':'bpawns','e2':'bpawns','f2':'bpawns','g2':'bpawns','h2':'bpawns',}
def boardtest(position,pieces):
    wr=0
    wkt=0
    wb=0
    wq=0
    wk=0
    wp=0
    w = ['wrook', 'wknight', 'wbishop','wqueen', 'wking', 'wpawns']
    b = ['brook', 'bknight', 'bbishop', 'bqueen', 'bking', 'bpawns']
    p=['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
    for i in pieces:
        if i==w[0]:
            wr+=1
        elif i == w[1]:
            wkt += 1
        elif i == w[2]:
            wb += 1
        elif i == w[3]:
            wq += 1
        elif i == w[4]:
            wk += 1
        elif i == w[5]:
            wp += 1
    if ((wkt==2)and(wr==2)and(wb==2)and(wk==1)and(wq==1)and(wp==8)):
        for i in pieces:
            if i == b[0]:
                wr += 1
            elif i == b[1]:
                wkt += 1
            elif i == b[2]:
                wb += 1
            elif i == b[3]:
                wq += 1
            elif i == b[4]:
                wk += 1
            elif i == b[5]:
                wp += 1
        if ((wkt==4)and(wr==4)and(wb==4)and(wk==2)and(wq==2)and(wp==16)):
            for l in position:
                if l not in p:
                    return False
                else:
                    ''
        else:
            return False
    else:
        return False
    return True
key=firstboard.keys()
value=firstboard.values()
print(boardtest(key,value))

