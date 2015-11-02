from pydmtx import DataMatrix
from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys
import logging

# Read jpegs in folder
folder = sys.argv[1]
output_folder = sys.argv[2]


def get_exif(i):
    ret = {}
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def parse_folder(folder, output_folder):

    # create output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # check images in folder
    for fn in os.listdir(folder):
        if fn.lower().endswith(".jpg") and not fn.lower().startswith("crop_"):
            print "Working on %s" % fn
            fnpath = os.path.join(folder, fn)

            # Read a Data Matrix barcode
            dm = DataMatrix()
            img = Image.open(fnpath)

            # Get datetime from image exif data
            exif = get_exif(img)
            datetime = exif["DateTime"].split(" ")[0].replace(":","")

            print datetime

            # only check bottom third column cell and sixth row
            w, h = img.size
            x_start = 3*(w/4)
            y_start = 4*(h/5)

            crop = img.crop((x_start, y_start, w, h))
            print "Crop: %s x %s" % (crop.size)

            #write crop for debugging purposes
            crop.save(os.path.join(folder, "crop_" + fn))

            # Detect
            identifier = dm.decode(crop.size[0], crop.size[1], buffer(crop.tobytes()))

            if identifier:
                print "Decoded: %s" % identifier

                #move and rename image
                os.rename(fnpath, os.path.join(output_folder, identifier + "_" + datetime + ".jpg"))
            else:
                print "No value"


parse_folder(folder, output_folder)
