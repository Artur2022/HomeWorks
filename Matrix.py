matrix = []
age = int(input())


def matrixFun(matrix, age):
    for i in range(age):
        matrix.append([0]*age)

    for i in range(age):
        for j in range(age):
            if(i == j):
                matrix[i][j] = 'M'

    for i in matrix:
        print(i)
        # printi tex@ porcel em returnov kods chi ashxatum ayd depqum


print(matrixFun(matrix, age))
