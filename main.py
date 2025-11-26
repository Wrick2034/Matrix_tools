from matrix import *

choice = int(input("Do you want to : \n 1- Calculate Inverse\n 2- Multiply 2 square matrices\n Choose : "))
if choice == 1:
    n = int(input("Enter the dimension of the Matrix : "))
    A=[]
    for i in range(n):
        A.append([])
        for j in range(n):
            print()
            num = int(input(f"Enter element {j+1} of row {i+1}: "))
            A[i]+=[num]
    print_matrix(A,n)
    # Cannot Calculate inverse if it has a determinant of 0
    if det(A,n)==0:
        raise ValueError("Invertible Matrix cannot have determinant 0")
    else:
        print("Your inverse Matrix is : ")
        print(find_inverse(A,n))


if choice == 2:
    n = int(input("Enter the dimension of the Matrix : "))
    A=[]
    for i in range(n):
        A.append([])
        for j in range(n):
            print()
            num = int(input(f"Enter element {j+1} of row {i+1}: "))
            A[i]+=[num]
    print_matrix(A,n)
    m = int(input("Enter the dimension of the Matrix : "))
    B=[]
    for i in range(m):
        B.append([])
        for j in range(m):
            print()
            num = int(input(f"Enter element {j+1} of row {i+1}: "))
            B[i]+=[num]
    print_matrix(B,n)
    print_matrix(multiply(A,B,n,m),n)
    
