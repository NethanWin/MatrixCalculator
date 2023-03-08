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
    if is_matrix(b)and not is_matrix(a):
        temp = b
        b = a
        a = temp
        
    if is_matrix(a) and not is_matrix(b):
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


def pow(a, num):
    answear = a
    for i in range(num-1):
        answear = mult(answear, a)
    return answear
    
    
def print_matrix(a):
    print('[')
    for i in range(len(a)):
        txt = ''
        for j in range(len(a[0])):
            txt += str(a[i][j]) + ', '
        print(txt[:-2])
    print(']')
    print()


def is_matrix(a):
    return type(a) == list and type(a[0]) == list
    

def get_new_length(a, b):
    
    max_len = max
    
    
def add_zeroes(a, length):
    # returns 2^n length matrix (adds zeroes)
    c = [[0 for _ in length] for _ in length]
    
    for row in range(len(a)):
        for col in range(len(a[0])):
            c[row][col] = a[row][col]
                
    return c
    
    
def new_mult(a, b):
    length = get_new_length(a, b)
    a = add_zeroes(a, length)
    b = add_zeroes(b, length)
    print(b)
    
    
def recursive_mult(m1, m2):
    # gets 2^n 
    a = m1[0][0]
    b = m1[0][1]
    c = m1[1][0]
    d = m1[1][1]
    
    A = m2[0][0]
    C = m2[0][1]
    B = m2[1][0]
    D = m2[1][1]
    
    u = (c-a)(C-D)
    v = (c+d)(C-A)
    w = aA+(c+d-a)(A+D-C)
    
    
    
    
def calc(txt):
    #TODO condese string
    #todo recursive txt
    if txt[0] == 'a':
        arg1 = a
    
    if txt[1] == 'b':
        arg2 = b
        
    if txt[1] == '+':
        return add(arg1, arg2)
    return [[]]
    

def main():
    a = [[0,1,2,3],
        [85,33554,2,1]]

    b = [[1,85,8],
        [5,6,7],
        [3,2,9],
        ]
    
   #print_matrix(mult(a,0))
    
    #print_matrix(mult(5.5,b))
    #print_matrix(mult(a,b))
    print_matrix(pow(b,82))

if __name__ == '__main__':
    main()
    
