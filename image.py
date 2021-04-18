# the image class

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

import helperFunctions as hf

class Image:

  def __init__ (self) -> None:
    """
    a function that initializes the image to None
    """
    self.img = None
    return


  # TODO: write this function
  def loadText (self, path: str) -> None:
    """
    loads the text file at the path to self.img
    """
    f = open(path, "r")
    message = f.read()

    self.img = PIL.Image.new('RGB', (6 * hf.lt_stringWidth(message), 15 * hf.lt_stringHeight(message)), (255, 255, 255))

    draw = PIL.ImageDraw.Draw(self.img)
    draw.text((0, 0), message, (0, 0, 0)) 
    return


  def loadImage (self, path: str) -> None:
    """
    loads the image at the path to self.img
    """
    self.img = PIL.Image.open(path)
    return


  def getDimensions (self) -> tuple:
    """
    returns the current dimensions of the Image
    """
    width, height = self.img.size
    return (width, height)


  def rescaleImage (self, dimensions = (0, 0), size = "None") -> None:
    """
    resizes the image to the new dimensions
    """
    # if the dimensions are given, size it according to that
    if (dimensions != (0, 0)):
      self.img = self.img.resize(dimensions)
    
    # if relative sizing is given, make the image "small", "medium", or "large"
    elif (size != "None"):
      relDim = 0
      if (size == "small"):
        relDim = 50
      elif (size == "medium"):
        relDim = 100
      elif (size == "large"):
        relDim = 150
      else:
        return
      
      currDim = self.getDimensions()
      if (currDim[0] > currDim[1]):
        self.img = self.img.resize((relDim, int((relDim / currDim[0]) * currDim[1])))
      else:
        self.img = self.img.resize((int((relDim / currDim[1]) * currDim[0]), relDim))

    return


  def toBraillePx (self, threshold = 128, toFile = False, inverse = False) -> None:
    """
    prints the image out in the braille pixel format
    a pixel displayed if the value is more than the threshhold
    note: ascii values start from 10240 and go to 10303
    """
    dim = self.getDimensions()
    w = (dim[0] + 1) // 2
    h = (dim[1] + 1) // 4

    # if it should be written to a file, writes to file
    if (toFile):
      f = open("out.txt", "w")

      for i in range(h):
        for j in range(w):
          f.write(chr(10240 + hf.b_blockValue(self.img, j, i, threshold, inverse)))
        f.write('\n')
    
    # outputs to console otherwise
    else:
      for i in range(h):
        for j in range(w):
          print(chr(10240 + hf.b_blockValue(self.img, j, i, threshold, inverse)), end='')
        print()
        
    return


  def toShade (self, characters=[32, 9617, 9618, 9619, 9608], toFile=False, inverse=False) -> None:
    """
    prints the image out in shaded format
    replaces each pixel with a shade based on value
    note: ascii values are 32, 9617, 9618, 9619, 9608
    """
    dim = self.getDimensions()
    w = dim[0]
    h = (dim[1] + 1) // 2

    # if it is to be written to a file, write it to a file
    if (toFile):
      f = open("out.txt", "w")

      for i in range(h):
        for j in range(w):
          f.write(chr(characters[hf.s_blockValue(self.img, j, i, len(characters))]))
        f.write('\n')

    # outputs to console otherwise
    else:
      for i in range(h):
        for j in range(w):
          print(chr(characters[hf.s_blockValue(self.img, j, i, len(characters))]), end='')
        print()

    return