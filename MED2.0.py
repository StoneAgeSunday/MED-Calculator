
import filler

def main():
    source = input("Please enter the source string: ")
    target = input("Please enter the target string: ")
    delcost = input("Please enter your chosen cost for a delete operation: ")
    inscost = input("Please enter your chosen cost for an insert operation: ")
    subcost = input("Please enter your chosen cost for a sub operation: ")

    delcost = int(delcost)
    inscost = int(inscost)
    subcost = int(subcost)

    matrix = filler.matrixBuild(source, target, delcost, inscost, subcost)

    #we have to state the MED. we'll get the final cell from the matix's size
    #then we'll want to call the presenter with the matrix and the strings

    #then we call the matrix builder with this info
    displayMatrix = input("Do you want to view the matrix? (Y/N)")
    if (displayMatrix == 'Y'):
        filler.presenter(matrix, source, target)

    end = input("press any key to exit ")

main()