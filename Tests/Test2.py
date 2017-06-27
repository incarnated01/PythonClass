# Chapter 2 Test
# Stephen Williamson

#named constants

FT_TO_INCHES = 12
INCHES_TO_CM = 2.54

def main():
    feet = eval(input("How many feet?"))
    for inches in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        height_in = feet * FT_TO_INCHES + inches
        height_cm = height_in * INCHES_TO_CM

        print(feet, "feet", inches, "inches ==", height_cm, "cm")

    feet = feet + 1
    for inches in [0]:
        height_in = feet * FT_TO_INCHES + inches
        height_cm = height_in * INCHES_TO_CM

        print(feet, "feet", inches, "inches ==", height_cm, "cm")

main()
