import re
import PyPDF2
import glob

from PyPDF2 import pdf
from wave_psf_objects import wave_psf

# gets x, y and z values from pdf files 
def getPsfValues(text):
    x_fwhm = re.findall('resolution.*x(\d.\d*) .m', text)
    x_fwhm = float(x_fwhm[0])

    y_fwhm = re.findall('resolution.*y(\d.\d*) .m', text)
    y_fwhm = float(y_fwhm[0])

    z_fwhm = re.findall('resolution.*z(\d.\d*) .m', text)
    z_fwhm = float(z_fwhm[0])

    return x_fwhm, y_fwhm, z_fwhm


# get wavelengths. with user input
pdf_path_list = glob.glob("pdfs_psf/*.pdf")
n_waves = int(input("Number of channels: "))
waves_dict = dict()
for path in pdf_path_list[:n_waves]:
    wave_re = re.findall('wave.*(\d{3})', path)
    waves_dict[f'{wave_re[0]}'] = wave_psf(wave_re[0])


# retrieve FHWM values from PDF files
for path in pdf_path_list:
    pdf_object = open(path,'rb')

    #create a parsable PDF object
    pdfReader = PyPDF2.PdfFileReader(pdf_object)
    # get text in page 1
    pageObj = pdfReader.getPage(0)
    text_pdf = pageObj.extractText()

    # get microscope type
    try:
        mic_type
        #print('lols')
    except:
        mic_type = re.findall('Microscope: (.*)Wave', text_pdf)
        microscope = mic_type[0]
        #print(microscope)

    for wave in waves_dict:
        if wave in path:
            wave_obj = waves_dict[wave]
            wave_obj.addvalues(getPsfValues(text_pdf))
            
# calculate averages
for wave in waves_dict:
    wave_obj = waves_dict[wave]
    wave_obj.getmeans()

# get top dir 
full_path = pdf_path_list[0]
top_dir = full_path[0:full_path.find('\\') + 1]

# create and write file
re_name_file = re.findall('.*\W(.*)_bead', pdf_path_list[0])
name_file = re_name_file[0]
psf_info_file = open(top_dir + f'{microscope}_psf_info for {name_file}.txt', 'w')

for wave in waves_dict:
    current_wave = waves_dict[wave]
    psf_info_file.write(f'wavelength {wave}:\n - lateral resolution is {current_wave.lat_res} µm\n - axial resolution is {current_wave.axi_res} µm\n\n')

psf_info_file.write('Esta é a mega surpresa')
psf_info_file.close()
