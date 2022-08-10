#!./ascii-art/bin/python3
# a program to convert images into ASCII art

# usage notes: two command line arguments are required, the first is the path to the image, and the second is the threshold value which is optional

import image
import sys

def main ():
    myImage = image.Image()
    myImage.load(sys.argv[1])
    myImage.resize(200, 200)
    myImage.toGrayscale()
    myImage.toBinary(int(sys.argv[2]) if len(sys.argv) > 2 else 100)
    print(myImage.asBraille())

if (__name__ == "__main__"):
    main()
