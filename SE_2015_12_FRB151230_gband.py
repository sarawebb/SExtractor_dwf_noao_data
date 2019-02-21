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

################ MAKE SURE TO CHANGE THE INFO ###################################
path = '/mnt/dwf/archive_NOAO_data/data_outputs/2015/12/FRB151230/g_band/single/*/ccds'
color_type = 'g_band'
thresh = 1.5
field = 'FRB151230'
image_type = 'single'
year = '2015'
month = '12'
mag_zpt = '25'
path_list = glob.glob(path)
#print(path_list)

################ DID YOU CHANGE THE INFO????? ###################################

for i in path_list: 
	#print(i)
	for filename in os.listdir(i):
		if filename.endswith('.fits'):
			#print(filename)
			#print(i + '/' + filename)
			hdulist = fits.open(i + '/' + filename)
			head = hdulist[0].header
			#field = head['OBJECT']
			#im_type = head['PRODTYPE']
			
			#image_filenam = (str(os.path.splitext(filename)[0]))
			split = filename.split(".",2)[0:1]
			image_filenam = "".join(str(x) for x in split)
			print(image_filenam)
				
			cat_path = '/mnt/dwf/archive_NOAO_data/data_outputs/' + year +'/'+month+'/'+field+'/'+color_type+'/'+image_type+'/'+str(image_filenam)+'/SE_cats'
			#print(cat_path)
			check_path = '/mnt/dwf/archive_NOAO_data/data_outputs/' + year +'/'+month+'/'+field+'/'+color_type+'/'+image_type+'/'+str(image_filenam)+'/SE_check_fits'
			
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
			#for j in thresh: 
			os.system('sex ' + str(i) + '/' + filename +' -c default_params.sex -CATALOG_NAME ' + cat_path + '/' + filename  + '_thresh_'+ str(thresh) +'_SE.cat -DETECT_THRESH ' + str(thresh) +' -MAG_ZEROPOINT ' + str(mag_zpt)  )
			#-CHECKIMAGE_NAME ' + check_path + '/' + filename + '_' + str(thresh) +'_CHECKIMAGE.fits'
			
