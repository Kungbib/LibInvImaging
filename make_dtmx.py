# -*- coding: iso-8859-1 -*-
from pydmtx import DataMatrix
from PIL import Image, ImageDraw, ImageFont
import sys

# Generate a label image containing a DataMatrix code and shelf identifer text.
# Image files are output as PNG in the current directory.
#
# Usage: python make_dtmx.py <location> <bookshelf> <shelf>

margin = 0
fontsize = 120

dm = DataMatrix()
dm.options["shape"] = dm.DmtxSymbolRectAuto
dm.options["module_size"] = dm.DmtxSymbol8x32
dm.options["scheme"] = dm.DmtxSchemeAscii
dm.options["margin_size"] = margin
font = ImageFont.truetype("inconsolata.otf", fontsize)
dmtx_block_size = 25

# parameters - max length is 13 chars (including separators)
location = sys.argv[1]      # pysical location e.g. H12V
case = sys.argv[2]          # book case identifier e.g. 12
count = int(sys.argv[3])    # number of shelf identifier e.g. 4 will generate 4 images.


def makedmx(text, filename):
    # Set up Data Matrix
    dm.encode(text)
    dm.save(filename, "png")


def addtext(text, filename):
    # Add identifier text to image
    img = Image.open(filename)
    w, h = img.size
    mode = img.mode

    # create a new image with margin and space for text.
    newImage = Image.new(mode, (dmtx_block_size + (w*2), h + (2 * dmtx_block_size)), (255,255,255))
    newImage.paste(img, (dmtx_block_size, dmtx_block_size))

    # add text to the right
    draw = ImageDraw.Draw(newImage)
    draw.text((w + (3 * dmtx_block_size),dmtx_block_size),text ,(0,0,0), font=font)
    newImage.save(filename)


for shelf in range(count):
    identifier = "%s-%s-%s" % (location, case, shelf + 1)
    makedmx(identifier, identifier + ".png")
    addtext(identifier, identifier + ".png")
