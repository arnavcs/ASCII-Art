import PIL.Image


def lt_stringWidth (message: str) -> int:
  """
  Returns the number of characters wide that a string is
  """
  maxWidth = 0
  runningWidth = 0

  for character in message:
    if (character == '\n'):
      maxWidth = max(maxWidth, runningWidth)
      runningWidth = 0
    else:
      runningWidth += 1
  
  maxWidth = max(maxWidth, runningWidth)
  return maxWidth


def lt_stringHeight (message: str) -> int:
  """
  Returns the height of a string in chracters
  """
  counter = 1

  for character in message:
    if (character == '\n'):
      counter += 1
  
  return counter


def b_toColour (image: PIL.Image, threshhold: int, coordinates: tuple, inverse: bool) -> int:
  """
  This function returns 1 if a pixel should be coloured black
  """
  col = image.getpixel(coordinates)
  val = sum(col) / len(col)
  if ((val > threshhold and not inverse) or (val < threshhold and inverse)):
    return 1
  else:
    return 0


def b_blockValue (image: PIL.Image, x: int, y: int, threshold: int, inverse: bool) -> int:
  """
  This function returns the value of the braille block in row y and column x
  """
  width, height = image.size
  val = 0
  exp = 0

  for i in range(2):
    for j in range(3):
      if (2*x + i >= width or 4*y + j >= height):
        exp += 1
        continue
      val += (2 ** exp) * b_toColour(image, threshold, (2*x + i, 4*y + j), inverse)
      exp += 1

  return val


def s_shadeValue (image: PIL.Image, coordinates: tuple, numIntervals:int) -> int:
  width, height = image.size
  if (coordinates[0] >= width):
    return 0
  elif (coordinates[1] >= height):
    return 0

  for i in range(numIntervals):
    col = image.getpixel(coordinates)
    val = sum(col) / len(col)
    if (255 * (i/numIntervals) < val):
      return i
  
  return numIntervals - 1


def s_blockValue (image: PIL.Image, x: int, y: int, numIntervals: int) -> int:
  """
  Returns the index (in the value list) that a certain block should have
  """
  width, height = image.size

  valueTop = s_shadeValue(image, (x, 2 * y), numIntervals)
  valueBot = s_shadeValue(image, (x, 2 * y + 1), numIntervals)
  
  return (valueTop + valueBot) // 2

# TODO: write this function
def toGrayscale (colours: tuple):
  """
  Converts a colour to grayscale using an averaging algorithm
  """
  pass