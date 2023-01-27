"""
Return a list of elements from a matrix by doing a zig-zag traversal over the
diagonal.

Part of a 45-m interview.

Runs in Python3

input = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]

output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

def test(matr):
    row = 0
    col = 0
    output = []

    down = True
    while (len(output) < (len(matr) * len(matr[0]))):
        print("%s, %s" % (row, col))
        output.append(matr[row][col])
        if (col == 0 or row == len(matr) -1) and down: #left wall
            # Skip down, go up and to the right
            print("Bounce right")
            row += 1
            down = False

            # Trim if this is OOB
            if (row == len(matr)):
                row -= 1
                col += 1

        elif (row == 0 or col == len(matr[row]) -1) and not down:
            #top wall
            # Skip right, go down and to the left
            print("Bounce down")
            col += 1
            down = True

            # Trim if this is OOB
            if (col == len(matr[0])):
                col -= 1
                row += 1

        else:
            # Travel along diag
            row += 1 if down else -1
            col += -1 if down else 1
        print(output)
        

input = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
] 

input2 = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
] 

input3 = [
  [1, 3],
  [2, 5],
  [6, 8],
  [7, 13]
]


"""
CoderPad REPL Log:

>>> test(input)
0, 0
Bounce right
[1]
1, 0
[1, 2]
0, 1
Bounce down
[1, 2, 3]
0, 2
[1, 2, 3, 4]
1, 1
[1, 2, 3, 4, 5]
2, 0
Bounce right
[1, 2, 3, 4, 5, 6]
3, 0
[1, 2, 3, 4, 5, 6, 7]
2, 1
[1, 2, 3, 4, 5, 6, 7, 8]
1, 2
[1, 2, 3, 4, 5, 6, 7, 8, 9]
0, 3
Bounce down
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
1, 3
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
2, 2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
3, 1
Bounce right
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
3, 2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
2, 3
Bounce down
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
3, 3
Bounce right
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

>>> test(input2)
0, 0
Bounce right
[1]
1, 0
[1, 2]
0, 1
Bounce down
[1, 2, 3]
0, 2
[1, 2, 3, 4]
1, 1
Bounce right
[1, 2, 3, 4, 5]
1, 2
[1, 2, 3, 4, 5, 9]
0, 3
Bounce down
[1, 2, 3, 4, 5, 9, 10]
1, 3
Bounce right
[1, 2, 3, 4, 5, 9, 10, 11]

>>> test(input3)
0, 0
Bounce right
[1]
1, 0
[1, 2]
0, 1
Bounce down
[1, 2, 3]
1, 1
[1, 2, 3, 5]
2, 0
Bounce right
[1, 2, 3, 5, 6]
3, 0
[1, 2, 3, 5, 6, 7]
2, 1
Bounce down
[1, 2, 3, 5, 6, 7, 8]
3, 1
Bounce right
[1, 2, 3, 5, 6, 7, 8, 13]

"""
