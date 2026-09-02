#Q4
'''Q4
 Write a function for matrix multiplication. It should support any
dimensions and print errors where multiplication is impossible.'''
def matrix_mul():
    m=int(input("Enter number of rows for matrix 1: "))
    n=int(input("Enter number of columns for matrix 1 :"))

    M1=list()
    M2=list()

    for i in range (m):
        row=[]
        for j in range (n):
            k=int(input("Enter element %d,%d : " %(i,j)))
            row.append(k)
        M1.append(row)



    a=int(input("Enter number of rows for matrix 2 : "))
    b=int(input("Enter number of columns for matrix 2 : "))   

    for i in range (a):
            row=[]
            for j in range (b):
                k=int(input("Enter element %d,%d : " %(i,j)))
                row.append(k)
            M2.append(row)

    print (M1)
    print(M2)

    if n != a:
        print("Matrix multiplication not possible.")
        return 0

    M3=list()
    
    for i in range(m):
        row=list()
        for j in range(b):
            s=0
            for k in range(a):
                s=s+M1[i][k]*M2[k][j]
            row.append(s)
        M3.append(row)


    print(M3)

matrix_mul()