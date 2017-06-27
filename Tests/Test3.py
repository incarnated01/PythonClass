# Test 3
# Stephen Williamson

# Math notes: L = H/(sin * A), A = (Pi/180) * D

import math


def main():
    #input
    height = eval(input("What is the height of the house?"))
    degrees = eval(input("What is the degree of the ladder's angle?"))

    #process
    angle = (math.pi/180) * degrees
    length = height/(math.sin(angle))

    #output
    print("The length of the ladder is", round(length, 2))

main()



main()