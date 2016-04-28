# LibInvImaging
Library inventory imaging - pilot project

This repository contains code to generate and read DataMatrix shelf
codes. The idea is to support a faster inventory process by taking
pictures of shelves and automatically rename those pictures with the
correct shelf identifier. This enables image comparison over time.

The ´´´make_dtmx.py´´´ generates DataMatrix image files for a series of
shelves.

Example:

![Data Matrix code example](https://raw.githubusercontent.com/Kungbib/LibInvImaging/master/dmtxexamples/H2O-10-1.png)

´´´parse_folder.py´´´ looks at jpeg images in the input folder and assumes
a DataMatrix code is somewhere in the lower right corner of the image.
Images are renamed to the shelf identifier code and moved to a specified
target folder.

![Data Matrix image corner](https://raw.githubusercontent.com/Kungbib/LibInvImaging/master/docs/example.jpg)


## Install requirements

```
pip install -r requirements.txt
```


## Installing the libDMTX library

libDMTX and python wrapper is required for generating and detecting DataMatrix codes. See https://github.com/dmtx/libdmtx for instructions.


The [inconsolata font](https://en.wikipedia.org/wiki/Inconsolata) is distributed under the SIL Open Font License.
