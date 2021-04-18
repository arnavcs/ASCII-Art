# a program to convert images into ASCII art

import image

def main ():
  myImage = image.Image()

  myImage.loadText("word.txt")
  myImage.rescaleImage(size="large")
  myImage.toBraillePx(toFile=False, inverse=True)

if (__name__ == "__main__"):
  main()