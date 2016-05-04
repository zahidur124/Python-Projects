##
## ***************************************************
## Zahidur Abedin (20549852)
## CS 116 Winter 2015
## Assignment 05, Problem 2
## ***************************************************
##

import check
#new_line(n) consumes  n, an Integer, and prints a pattern consisting of
# '#', and produces none.
#new_line: Int -> None

def new_line(n):
    x = ""
    while n>0:
        if n%2 ==0:
            x= x + "#"
            n = n -1
        else:
            x = x + " "
            n = n - 1
    return x

#new_line(n) consumes  n, an Integer, and prints a pattern consisting of
# '#', and produces none.
#alternate_line: Int -> None
    
def alternate_line(n):
    y =""
    val = new_line(n)
    for x in val:
        if x.isspace() == True:
            y = y + "#"
            n = n - 1
        else:
            y = y + " "
            n = n - 1
    return y


#print_checkerboard(rows,cols) consumes rows, an Integer, and cols, and Integer,
# produces None, and prints a pattern on the screen with rows rows and 
# cols columns.
#print_checkerboard: Int Int -> None
# requires: rows >= 1
#           cols >= 1
#Example:
#        print_chekerboard(5,3) => None is produced and the function prints
#        a checkerboard on the screen with 5 rows and 3 columns
#        print_chekerboard(1,2) => None is produced and the function prints
#        a checkerboard on the screen with 1 rows and 2 columns

def print_checkerboard(rows,cols):
    first_line = new_line(cols)
    second_line = alternate_line(cols)
    dashes = "-" * cols
    boundary = "+"+dashes+"+"
    print(boundary)
    while rows > 0:
        if rows%2 ==0:
            print("|"+second_line+"|")
            rows = rows - 1
        else:
            print("|"+first_line+"|")
            rows = rows - 1
    print(boundary)

#Tests:
check.set_screen("+--+\n|# |\n+--+")
check.expect("Q2T1", print_checkerboard(1,2), None)
check.set_screen("+---+\n| # |\n|# #|\n| # |\n+---+")
check.expect("Q2T2", print_checkerboard(3,3), None)
check.set_screen("+-+\n| |\n|#|\n| |\n|#|\n| |\n+-+")
check.expect("Q2T3", print_checkerboard(5,1), None)

check.set_screen("+----+\n|# # |\n| # #|\n|# # |\n+----+")
check.expect("Q2T3", print_checkerboard(3,4), None)

                 

    
    