def det(A,n):
    if n==1:
        return A[0][0]
    elif n==2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    else:
        res=0
        for col in range(n):
            sub = sub_matrix(A,n,col,0)
            sign = 1 if col%2==0 else -1
            res+=sign*A[0][col]*det(sub,n-1)
        return res
    

def sub_matrix(A,n,col,row):
    sub = [[0]*(n-1) for _ in range(n-1)]
    row_ct = 0
    for i in range(0,n):
        col_ct = 0
        if row == i:
            continue
        for j in range(n):
            if j==col:
                continue
            sub[row_ct][col_ct] = A[i][j]
            col_ct+=1
        row_ct+=1
    return sub


def find_inverse(A,n):
    cofac = [[0]*(n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            cofac[i][j] = (-1)**(i+j)*det(sub_matrix(A,n,i,j),n-1)
    transpose(cofac,n)
    for i in range(n):
        for j in range(n):
            cofac[i][j]/=det(A,n)
    return cofac


def transpose(A,n):
    for i in range(n):
        for j in range(n):
            temp = A[i][j]
            A[i][j]=A[j][i]
            A[j][i]=temp


def print_matrix(A,n):
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]:0.2f}",end="  ")
        print()
    print()