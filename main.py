# a program to convert images into ASCII art

import image

def main ():
  myImage = image.Image()
  myImage.load("./cat.png")
  myImage.resize(200, 200)
  myImage.toGrayscale()
  myImage.toBinary(100)
  print(myImage.asBraille())
  myImage.show()

if (__name__ == "__main__"):
  main()
