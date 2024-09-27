def printMatrix(M):
    print("  y:   0      1      2      3      4      5      6      7")
    print("x-----------------------------------------------------------")
    a = 0
    for i in M:
        print(a, "| ", end="")
        for j in i:
            print(f"{j:.4f}", end=" ")
        a+=1
        print("")

from random import random

trials = 100000
n = 7 #number of weeks
p = 0.6 #play this week prob
q = 0.7 #winning prob

joint = [[0],
        [0, 0],
        [0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

for j in range(trials):
    y = 0 #number of wins
    x = 0 # number of plays
    for i in range(0,n): #trial start
        z = random() #will Joe play this week?
        if z < p:
            x+=1
            z = random() #will Joe win?
            if z < q:
                y+=1
    #print(x, y)
    joint[x][y]+=1#at end of week, increment (x,y)

#perform relative frequency calculation
for row, i in enumerate(joint):
    for col, j in enumerate(i):
        joint[row][col] = joint[row][col]/trials

print("Joint PMF of X and Y")
printMatrix(joint)

marginalx = [0, 0, 0, 0, 0, 0, 0, 0]
marginaly = [0, 0, 0, 0, 0, 0, 0, 0]
for row, i in enumerate(joint):
    marginalx[row] += sum(i)

for row, i in enumerate(joint):
    for col, j in enumerate(i):
        marginaly[col] += j 

"""
print("Marginal X:", marginalx)
print("Sum of Marginal X", sum(marginalx))
print("Marginal Y:", marginaly)
print("Sum of Marginal Y", sum(marginaly))
"""

#calculate Conditonal on x given y
xGivenY = [[0],
           [0, 0],
           [0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

for row, i in enumerate(joint):
    for col, j in enumerate(i):
        xGivenY[row][col] = joint[row][col]/marginaly[row]
print("")
print("Conditional PMF of X given Y")
printMatrix(xGivenY)

#calculate Conditional on y given x
yGivenX = [[0],
           [0, 0],
           [0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]]

for row, i in enumerate(joint):
    for col, j in enumerate(i):
        yGivenX[row][col] = joint[row][col]/marginalx[col]
print("")
print("Conditional PMF of Y given X")
printMatrix(yGivenX)
