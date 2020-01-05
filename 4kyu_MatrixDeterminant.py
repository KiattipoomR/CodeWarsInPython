def determinant(matrix) :
    #your code here
    if len(matrix) == 1 :
        return matrix[0][0]
    if len(matrix) == 2 :
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    result = 0
    for i in range(len(matrix)):
        inner = []
        for block in matrix[1:] : 
            inner.append(block[0:i] + block[i+1:len(matrix)])
        result += matrix[0][i] * determinant(inner) * ((-1)**i)
    return result
