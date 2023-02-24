#!/usr/bin/env python3

from PIL import Image, ImageEnhance
from tkinter import filedialog as fd, simpledialog

wPixels, contrast, characterScale = 200, 1.0, " .,-:=+*#%@"
# ░▒▓█
def main():

    global wPixels, contrast, characterScale
    filename = fd.askopenfilename()
    originalImage = Image.open(filename)
    wPercent = (wPixels/float(originalImage.size[0]))
    hPixels = int((float(originalImage.size[1])*float(wPercent))*.35)
    grayImage = originalImage.resize((wPixels,hPixels), Image.Resampling.LANCZOS).convert('L')
    contrastedImage = ImageEnhance.Contrast(grayImage).enhance(contrast)
    #grayImage.save('mypic.png')
    #contrastedImage.save('mypic2.png')
    pixelValues = list(contrastedImage.getdata())
    numChars = len(characterScale)-1
    pixelValuesNormalized = [round(numChars-(i/255*numChars)) for i in pixelValues]
    #print(pixelValuesNormalized)
    x=0
    for i in pixelValuesNormalized:
        print(characterScale[i], end="")
        x += 1
        if x % wPixels == 0:
            print("\n", end="")

main()
