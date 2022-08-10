# ASCII-Art

A project that takes images, and converts it into ASCII art using braille characters. It does this by first making the image grayscale, and then splitting the image into 3 by 2 chunks which are then represented with the braille ASCII characters.

## Running

Usage:
```
python3 main.py path-to-image [threshold-value]
```

Options:
```
path-to-image is the path to the image you would like to pass to the program
threshold-value is an integer between 0 and 255 that represents how dark or light the output should be
```

## Dependencies

* OpenCV
* Python 3.x.x
