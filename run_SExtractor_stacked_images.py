"""run_SExtractor_stacked_images.py -- Input a year, month, field, color_type, image_type, thresh, mag_zpt, SExtractor will be run over all single extenstions for each exposure and the out putted catalogs will be saved in the follow directory /fred/oz100/NOAO_archive/arachive_NOAO_data/data_outputs/+year+/+month+/+field+/+band+/+iamge_type+/*/SE_cats/ 

Usage: run_SExtractor_stacked_images [-h] [-v]  [--debug] <year> <month> <field> <color_type> <image_type> <thresh> <mag_zpt>

Arguments:
	year (string)
		The year the data was taken. 
	month  (string)
		The month the data was taken.
	field  (string)
		The DWF field name. ENSURE spelling is exactly how it appears within the NOAO header files. 
	color_type (string)
		The band type, eg 'g_band' for single exposures of DWF data, or 'colors'. 
	image_type (string)
		The image type, default stacked.
	thresh (string)
		The detection threshold for SExtractor. Receommended 1.5.
	mag_zpt (string)
		The zeropoint of the images put into SExtractor. Recommended = 25
Options:
	-h, --help                              Show this screen
	-v, --verbose                           Show extra information [default: False]     
	--debug                                 Output more for debugging [default: False]
Example:
	python run_SExtractor_single_images.py -v 2015 01 4hr g_band single 1.5 25 
	python ####
"""

import docopt
import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from astropy import wcs
from astropy.wcs import WCS
from astropy.io import fits
import sys
import math
import os
import glob
import sys
from sortedcontainers import SortedDict
import datetime as dt
import imageio
import os
from PIL import Image
from matplotlib.colors import LogNorm
from astropy.nddata.utils import Cutout2D
from astropy import units as u
import datetime as dt 
import glob


def run_SExtractor_stacked_images(year, month, field, color_type, image_type, thresh, mag_zpt, verbose=False,debugmode=False):
	if image_type == 'single':
		path = '/fred/oz100/NOAO_archive/archive_NOAO_data/data_outputs/'+year+'/'+month+'/'+field+'/'+color_type+'/'+image_type+'/*/ccds/'
	elif image_type == 'stacked':
		path = '/fred/oz100/NOAO_archive/archive_NOAO_data/data_outputs/'+year+'/'+month+'/'+field+'/'+color_type+'/'+image_type+'/'
	print(path)
	#path_list = glob.glob(path)
	#print(year, month, field, color_type, image_type, thresh, mag_zpt)
	#break
	#for i in path_list: 
	for filename in os.listdir(path):
		if filename.endswith('.fits'):
			print(path + '/' + filename)
			hdulist = fits.open(path + '/' + filename)
			head = hdulist[0].header
			split = filename.split(".",2)[0:1]
			image_filenam = "".join(str(x) for x in split)
				
				
			cat_path = '/fred/oz100/NOAO_archive//archive_NOAO_data/data_outputs/' + year +'/'+month+'/'+field+'/'+color_type+'/'+image_type+'/'+str(image_filenam)+'/SE_cats'
			check_path = '/fred/oz100/NOAO_archive/archive_NOAO_data/data_outputs/' + year +'/'+month+'/'+field+'/'+color_type+'/'+image_type+'/'+str(image_filenam)+'/SE_check_fits'
			
			print(cat_path)
			print(check_path)
			if not os.path.exists(cat_path):
				os.makedirs(cat_path)
			else:
				pass 
			
			if not os.path.exists(check_path):
				os.makedirs(check_path)
			else:
				pass 
				 
			os.system('sex ' + str(path) + '/' + filename +' -c default_params.sex -CATALOG_NAME ' + cat_path + '/' + filename  + '_thresh_'+ str(thresh) +'_SE.cat -DETECT_THRESH ' + str(thresh) +' -MAG_ZEROPOINT ' + str(mag_zpt) + ' -CHECKIMAGE_NAME '  + check_path + '/' + filename + '_' + str(thresh) +'_CHECKIMAGE.fits')
	return print('DONE')

if __name__ == "__main__":
	arguments = docopt.docopt(__doc__)
	print(arguments)
	year = arguments['<year>']
	month = arguments['<month>']
	field = arguments['<field>']
	#color_type = arguments['<color_type>']
	#image_type = arguments['<image_type>']
	#thresh = arguments['<thresh>']
	#mag_zpt = arguments['<mag_zpt>']

	if arguments['<color_type>']:
		color_type = arguments['<color_type>']
	else: 
		color_type = 'g_band'
	
	if arguments['<image_type>']:
		image_type = arguments['<image_type>']
	else: 
		image_type = 'stacked'
	if arguments['<thresh>']:
		thresh = arguments['<thresh>']
		thresh = float(thresh)
	else: 
		thresh = 1.5 
	if arguments['<mag_zpt>']:
		mag_zpt = arguments['<mag_zpt>']
		mag_zpt = int(mag_zpt)
	else: 
		mag_zpt = 25 
	#verbose = arguments['--verbose']
	debugmode = arguments['--debug']
	print(arguments)
	if debugmode: 
		print(arguments)
	run_SExtractor_stacked_images(year, month, field, color_type, image_type, thresh, mag_zpt, verbose=False, debugmode=False)
