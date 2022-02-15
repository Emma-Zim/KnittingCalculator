import math

# this is the knitting calculator
# it has predefined patterns and the user inserts their desired final size
# and their swatch size to find out how many stitches to cast on and rows to knit


def menu():
    print("1. Rectangle calculator\n")
    menuChoice = int(input("Choose: "))
    if(menuChoice != 1):
        print("wrong")
        menu()
    return menuChoice

def rectangle():
    swatchRows = int(input("How many rows in the swatch: "))
    swatchSts = int(input("How many stitches in the swatch: "))

    # need to find out how many stitches per unit
    # going to round down by default
    stitchesPerUnit = math.floor(swatchSts/4)
    rowsPerUnit = math.floor(swatchRows/4)

    print("width\n-----\n|   | length\n-----")

    length = int(input("How long do you want it to be in inches? "))
    width = int(input("How wide do you want it to be in inches? "))

    print(str(stitchesPerUnit) + " stitches per 1 inch")
    print(str(rowsPerUnit) + " rows per 1 inch")

    # now to calculate- if we have how many stitches per inch and how many inches- then multiply them together
    finalStitches = stitchesPerUnit*width
    finalRows = rowsPerUnit*length

    print(str(finalStitches) + " stitches to cast on")
    print(str(finalRows) + " rows to knit")

def main():
    menuChoice = menu()
    if(menuChoice == 1):
        print("Rectangles are the most versatile shape and can be used for blankets, scarves, and the basis for sweaters. If you are just starting out, this is the place for you.")
        print("This is suitable for any weight yarn.")
        print("If you want a scarf, make the length much longer than the width. if you want a blanket, make it more square.")
        print("Knit a swatch that is 4x4 inches in the yarn and needle size you are wanting to use. Measure out how many stitches and rows are in the swatch. Block it if you want before measuring.")
        rectangle()
        exit()


main()

# this is assuming swatch size is 4x4 inches
