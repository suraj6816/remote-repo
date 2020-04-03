#7 Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.

input_str = '4,5'     #raw_input()
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
print multilist

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print multilist

print('adding my second edit in the prog2 file')
