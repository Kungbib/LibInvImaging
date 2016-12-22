# LibInvImaging
Library inventory imaging - pilot project

This repository contains code to generate and read DataMatrix shelf
codes. The idea is to support a faster inventory process by taking
pictures of shelves and automatically rename those pictures with the
correct shelf identifier. Images are to be collected in a database to 
enable comparison of shelf content over time.

The project also explored various options for quick image capture. 

 * _make_dtmx.py_ generates DataMatrix image files for a series of shelves. Example: ![Data Matrix code example](/dmtxexamples/H2O-10-1.png?raw=true)

 * _parse_folder.py_ looks at jpeg images in the input folder and assumes
a DataMatrix code is somewhere in the lower right corner of the image.
Images are renamed to the shelf identifier code and moved to a specified
target folder.

![Data Matrix image corner](/docs/example.jpg?raw=true)


## Install requirements

```
pip install -r requirements.txt
```


## Installing the libDMTX library

libDMTX is required for generating and detecting DataMatrix codes.

* Get source

```
git clone git://libdmtx.git.sourceforge.net/gitroot/libdmtx/libdmtx
git clone git://libdmtx.git.sourceforge.net/gitroot/libdmtx/dmtx-wrappers
git clone git://libdmtx.git.sourceforge.net/gitroot/libdmtx/dmtx-utils
```

* Build core library

```
cd libdmtx
git checkout v0.7.4
./autogen.sh
./configure
make
make install
```

* Build Python library

```
cd ../dmtx-wrappers/
./autogen.sh
./configure
make
```

* Install Python library

```
cd python
python setup.py install
```

* Test your installation

```
python -c "import pydmtx; print(pydmtx)"
```


The [inconsolata font](https://en.wikipedia.org/wiki/Inconsolata) is distributed under the SIL Open Font License.
