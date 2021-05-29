# Measure PSF
Measures PSFs from image using Fiji with MetroloJ and python script to calculate lateral and axial resolution averages.

It can handle up to 4 different channels.

## How to use

### ImageJ
- Open a PSF stack image in Fiji.
- Process that image using the *while_metroloj.ijm* macro.

Output are PDF files with PSF measurements.

### Python
- *average_PSFs.py* and *wave_psf_objects.py* need to be in the same directory.
- Create a directory called *pdfs_psf* in the same directory as the python scripts.
- Copy those PDF files into *pdfs_psf*.
- Run the *average_PSFs.py* script.

Output is a text file with average measurements.

## Dependencies
- [MetroloJ](https://imagejdocu.tudor.lu/plugin/analysis/metroloj/start)
- Python 3
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Please cite MetrojoJ and this repo if you use it. Thanks :D
