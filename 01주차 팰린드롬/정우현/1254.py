str = str(input())
strarr = list(str)

def is_prdrop(strarr):
    w = len(strarr)//2
    for i in range(w):
        for j in range(len(strarr)-1,w,-1):
            if strarr[i] == strarr[j]:
                i += 1
            else:
                return False
    return True



def prdrop(strarr):
    if is_prdrop(strarr):
        print(strarr)
    else:
        

prdrop(strarr)
        
