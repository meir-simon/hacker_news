import pandas as pd

def throw_eggs(height, eggs):
    
    # Initiate the matrix to be full of zeros.
    matrix = []
    for h in range(height + 1):
        matrix.append([])
        for k in range(eggs + 1):
            matrix[h].append(0)

    # Initiate the start condition
    for k in range(1, eggs + 1):
        matrix[1][k] = 1

    # Initiate the start condition
    for h in range(1, height + 1):
        matrix[h][1] = h

    # Fill in the rest of the matrix
    for i in range(2, height + 1):
        for j in range(2, eggs + 1):
            list = []
            
            for x in range(1, i + 1):
                list.append(max(matrix[x - 1][j - 1] + 1, matrix[i - x][j] + 1))   
            matrix[i][j] = min(list)
            
            
            

    #return matrix # Return the relevant element in the matrix
    return matrix[height][eggs]
    
print(throw_eggs(100, 3))
# m = (throw_eggs(100, 3))
# print(pd.DataFrame(m))
    
