# Measure PSF
Measures PSFs from a 3D image using Fiji with MetroloJ and python script to calculate average lateral and axial resolution.

It can handle up to 4 different channels.

## How to use

### ImageJ
- Open a PSF stack image in Fiji.
- Process that image using the *while_metroloj.ijm* macro.

Output are PDF files with PSF measurements.

### Python
- *average_PSFs.py* and *wave_psf_objects.py* must be in the same directory.
- Create a directory called *pdfs_psf* in the same directory as the python scripts.
- Copy those PDF files into *pdfs_psf*.
- Run the *average_PSFs.py* script.

Output is a text file with average measurements.

## Dependencies
Python scripts use python3 syntax.
- [MetroloJ](https://imagejdocu.tudor.lu/plugin/analysis/metroloj/start)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

MetroloJ is installed in Fiji via the old-fashion way. By dragging the .jar file into the _Plugins_ folder of your Fiji installation. It also needs the iTextlibrary plugin installed in Fiji. Instructions on how to do so are present in the MetroloJ website.

To install PyPDF2, use pip. Run this on your terminal:
```
pip install PyPDF2
```

Please cite MetroloJ and this repo if you use it. Thanks :D
