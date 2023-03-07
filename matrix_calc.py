def transpose(a):
    i_len = len(a)
    j_len = len(a[0])
    b=[[a[i][j] for i in range(i_len)]for j in range(j_len)]
    return b

# TODO check if it works
def add(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception("can't add 2 matrixes with different dimensions")
    
    
def mult(a,b):
    if type(b) == list and (type(a) == float or type(a) == int):
        temp = b
        b = a
        a = temp
        
    if type(a) == list and (type(b) == float or type(b) == int):
        return [[a[i][j] * b for j in range(len(a[0]))] for i in range(len(a))]
        
    if type(a) == float and type(b) == float:
        return a*b
        
    ai = len(a)
    aj = len(a[0])
    bi = len(b)
    bj = len(b[0])
    
    if aj != bi:
        raise Exception("cant mult with wrong dimentions")
        
    c = [[0 for _ in range(bj)] for _ in range(ai)]
    
    for i in range(ai):
        for j in range(bj):
            for k in range(aj):
                c[i][j] += a[i][k] * b[k][j]
    return c

    
def print_matrix(a):
    print('[')
    for i in range(len(a)):
        txt = ''
        for j in range(len(a[0])):
            txt += str(a[i][j]) + ', '
        print(txt[:-2])
    print(']')
    print()


def main():
    a = [[0,1,2,3],
        [85,33554,2,1]]

    b = [[1,85,8],
        [5,6,7],
        [3,2,9],
        [7,84,2]]
    
    print_matrix(mult(a,0))
    
    print_matrix(mult(5.5,b))
    print_matrix(mult(a,b))
    txt = input("enter matrix calculation\n")
    

if __name__ == '__main__':
    main()
    
