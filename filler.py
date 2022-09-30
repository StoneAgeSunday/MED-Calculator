#matrix filler module

def matrixBuild(source, target, delcost, inscost, subcost):
    source = '#'+source
    target = '#'+target
    length = len(source)
    width = len(target)

    matrix = [[0 for x in range(width)] for y in range(length)]

    #we exclude 0 from the range because cell [0,0] must always contain 0
    for k in range(1, width):
        matrix[0][k] = matrix[0][k-1] + inscost

    for k in range(1, length):
        matrix[k][0] = matrix[k-1][0] + delcost

    for i in range(1,length):
        for j in range(1, width):
            matrix[i][j] = minOp(i, j, matrix, inscost, delcost, subcost, source, target)

    #time to view the current matrix
    #for i in range(width):
    #    print(repr(matrix[4][i]))

    #print("end")
    #for i in range (length):
    #    print(repr(matrix[i][4]))
    #end of viewing

    #outputting minimum distance
    print("")
    print("Minimum edit distance:")
    print(repr(matrix[length-1][width-1]))
    print("")
    #end

    return matrix

    #populate the leftmost column and top row.
    
    #now we have to build/fill the matrix. first let's test this.
    #for i in range(len(matrix[0])):
    #    print(repr(matrix[0][i]))
    #remember, the matrix in the book is filled upwards and rightwards.
    #transpose the matrix we build here to make it look like the one
    #that is shown in the book? I would use numpy but that requires the
    #elements to all be of the same type

    #l = len(source)-1
    #b = len(target)-1
    #for r in range(len(source)):
    #    matrix[l-r][0] = source[r]

    #for c in range(len(target)):
    #    matrix[l][b-c] = target[c]

    #Now I want to do another test, to check the current contents of the
    #matrix/table
    #this is to print target
    #for i in range(len(matrix[l])):
        #print(repr(matrix[l][i]))

    #this is to print source
    #for i in range(len(matrix)):
        #print(repr(matrix[i][0]))
    
    


    #we'll need to initialize the matrix and then pass that matrix to the
    #filler. when we pass it, we'll need to include the costs. This makes me
    #it would be a better idea to call matrixInit from inside matrixFiller. It
    #makes we think we have no need for matrixInit - that we should fill the
    #as we build it.
    #length is the length of the source, so it's the number of rows, i.e. the
    #number of sublists
    #reme

def minOp(sPos, tPos, matrix, inscost, delcost, subcost, source, target):
    costs = [0 for x in range(3)]
    costs[0] = matrix[sPos][tPos-1] + inscost #for the insert op
    costs[1] = matrix[sPos-1][tPos] + delcost #delete operation
    if source[sPos] == target[tPos]: #for sub operation
        costs[2] = matrix[sPos-1][tPos-1] + 0
    else:
        costs[2] = matrix[sPos-1][tPos-1] + subcost

    return min(costs)

def presenter(matrix, source, target):
    #we need to determine the longest number in each column.Store these numbers in a list Longest
    #Then we need to pad all entries in each column with the corresponding number in Longest.
    #We'll also need to convert the entries in the matrix to strings/chars
    #
    #How will we do the printing?
    target = '#'+target
    source = '#'+source
    width = len(target)+1
    length = len(source)+1
    #we need the plus ones so that there's space for the source and target strings
    #remember, everything in python is passed by reference
    table = [["" for x in range(width)] for y in range(length)]
    #now to fill the 1st column and row
    for k in range(1, length):
        table[k][0] = source[k-1]

    for k in range(1, width):
        table[0][k] = target[k-1]

    #we need to fill the table with string reprs of the values in matrix
    for k in range(1, length):
        for j in range(1, width):
            table[k][j] = repr(matrix[k-1][j-1])

    columnWidths = [0 for x in range(width)]
    columnWidths[0] = 1 #because the first column just contains the source string
    #we'll need a max variable. initialized to 1
    for k in range(width):
        max = 1
        for j in range(length):
            cand = len(table[j][k])
            if (cand > max): max = cand
        columnWidths[k] = max
     #now for the padding of the elements of table
    for k in range(width):
         for j in range(length):
             table[j][k] = table[j][k].rjust(columnWidths[k]+1)

    #now to print out the table
    line = "" #this is the string we'll use to hold the contents of each row. When it contains the whole row, we'll print it
    for k in range(length):
        for j in range(width):
            line = line + table[k][j]
        print(line)
        line = ""

    #python passes everything by reference so source and target should still be prepended with #
