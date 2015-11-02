# -*- coding: iso-8859-1 -*-
from pydmtx import DataMatrix
from PIL import Image, ImageDraw, ImageFont
import sys


margin = 40
fontsize = 90

dm = DataMatrix()
dm.options["shape"] = dm.DmtxSymbolRectAuto
dm.options["module_size"] = dm.DmtxSymbol8x32
dm.options["scheme"] = dm.DmtxSchemeAscii
dm.options["margin_size"] = margin
font = ImageFont.truetype("inconsolata.otf", fontsize)


def makedmx(text, filename):
    # Set up Data Matrix
    dm.encode(text)
    dm.save(filename, "png")


def addtext(text, filename):

    # Add identifier text to image
    img = Image.open(filename)
    w, h = img.size
    mode = img.mode

    newImage = Image.new(mode, (w*2, h), (255,255,255))
    newImage.paste(img, (0, 0))

    # add text to the right
    draw = ImageDraw.Draw(newImage)
    draw.text((w + 20,h/2),text ,(0,0,0), font=font)
    newImage.save(filename)


# Parameters
#location = "H2Ö"
#case = "98"
#shelf = "12"
#identifier = "%s-%s-%s" % (location, case, shelf)

location = sys.argv[1]
case = sys.argv[2]
count = int(sys.argv[3])


for shelf in range(count):
    identifier = "%s-%s-%s" % (location, case, shelf + 1)
    makedmx(identifier, identifier + ".png")
    addtext(identifier, identifier + ".png")
