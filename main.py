from matrix import print_matrix,det,find_inverse

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
    print_matrix(find_inverse(A,n),n)
    
