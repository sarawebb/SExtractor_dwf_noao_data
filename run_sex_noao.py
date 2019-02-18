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

path = '/mnt/dwf/archive_NOAO_data/testfolder/data_outputs/2017/02/4hr/g_band/single/*/ccds'

path_list = glob.glob(path)
print(path_list)

'''
for filename in os.listdir(path): 
    if filename.endswith('.fits'): 
        print(filename)
        hdulist = fits.open(path + '/'+ filename)
        head = hdulist[0].header
        field = head['OBJECT']
        date = dt.datetime.strptime(head['DATE-OBS'], '%Y-%m-%dT%H:%M:%S.%f')
        year = date.strftime('%Y')
        month = date.strftime('%m')
        im_type = head['PRODTYPE']
        
        if im_type == 'image1':
            image_type = 'stacked'
            
        if im_type == 'image':
                image_type = 'single'
        
        print(image_type)
        
        move_path_cat = '/mnt/dwf/archive_NOAO_data/data/'+year+'/' +month+ '/' +field+  '/'
        
       if not os.path.exists(move_path_year): 
             os.makedirs(move_path_year, 0o755)
        else: 
            pass 
            
        if not os.path.exists(move_path_month): 
             os.makedirs(move_path_month, 0o755)
        else: 
            pass 
              
            
        if not os.path.exists(move_path_cat): 
             os.makedirs(move_path_cat, 0o755)
        else: 
            pass 
        
        os.system('sex ' + path + '/' + filename +' -c default_params.sex -CATALOG_NAME ' + filename + '_SE.cat')
	#os.rename(path + '/'+ filename + '_SE.cat', move_path_cat + '/' + filename + '_SE.cat')
        
#hdulist= fits.open()
#hrd = hdulist[0].header
#field = hrd['OBJECT']
#date = dt.datetime.strptime(hrd['DATE'], '%Y-%m-%dT%H:%M:%S') 
#print(date) 
   '''  
