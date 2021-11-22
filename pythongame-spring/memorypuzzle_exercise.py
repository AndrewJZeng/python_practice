# nested loop

colors = ['red', 'green', 'blue']
shapes = ['donut', 'square', 'diamond', 'oval']

for c in colors:
    for s in shapes:
        print(c, s)

print()

for s in shapes:
    for c in colors:
        print(c, s)
print()

# list of lists
board = []
num_column = 3
num_row = 4
for i in range(num_column):
    column = []
    
    for j in range(num_row):
        column.append(j)
    
    board.append(column)
    
print(board)
print()

# random and copy
import random
A = [1,2,3,4,5]

random.shuffle(A)
print(A)

B = A[:3]
print(B)

C = B * 2
print(C)

random.shuffle(C)
print(C)