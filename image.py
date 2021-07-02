# this is the image class

import cv2
import math

class Image:
  def __init__ (self) -> None:
    self.image = None

  def load (self, path: str) -> None:
    '''
    This function loads the image at the desired path
    '''
    self.image = cv2.imread(path, cv2.IMREAD_COLOR)

  def resize (self, height, width) -> None:
    '''
    This function resizes the image to the given dimensions
    '''
    self.image = cv2.resize(self.image, (width, height), interpolation = cv2.INTER_AREA)

  def toGrayscale (self) -> None:
    '''
    This function makes the image a grayscale image
    '''
    self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    
  def toBinary (self, threshold : int) -> None:
    '''
    This function binarizes the image
    '''
    _, self.image = cv2.threshold(self.image, threshold, 255, cv2.THRESH_BINARY)
  
  def show (self) -> None:
    '''
    This function displays the image and waits for user input
    '''
    cv2.imshow("Loaded Image", self.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

  def brValue (self, row : int, col : int) -> int:
    '''
    For each braille block, this function calculates the ASCII value
    '''
    retValue = 0
    img_dims = list(self.image.shape)
    coeff = 1

    for i in range(2 * col, 2 * col + 2):
      for j in range(4 * row, 4 * row + 4):
        if (not (j >= img_dims[0] or i >= img_dims[1])) and (self.image[j, i] > 0):
          retValue += coeff
        coeff *= 2

    return retValue

  def asBraille (self) -> None:
    '''
    This function returns a string that represents the braille ASCII art
    '''
    img_dims = list(self.image.shape)
    ret = ""

    for row in range(math.ceil(img_dims[0] / 4)):
      for col in range(math.ceil(img_dims[1] / 2)):
        ret += chr(10240 + self.brValue(row, col))
      ret += '\n'

    return ret
