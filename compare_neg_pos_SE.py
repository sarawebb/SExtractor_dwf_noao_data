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
import shutil


path = '/mnt/dwf/archive_NOAO_data/testfolder/singlefits'
ext = np.arange(1, 2, 1)







for i in ext: 
    
    filenames_pos = []
    num_sources_pos  = []
    thresh_num_pos = []
    filenames_neg = []
    num_sources_neg  = []
    thresh_num_neg = []
    filenames_pos = glob.glob('/mnt/dwf/archive_NOAO_data/testfolder/singlefits/*_'+ str(i) + '*_pos_SE.cat ')
    filenames_neg = glob.glob('/mnt/dwf/archive_NOAO_data/testfolder/singlefits/*_'+ str(i) + '*_neg_SE.cat')
    print(filenames_pos)
    for j in filenames_pos:
        print(j)
        try:
            MAG_APP_OBS, MAGERR_APP_OBS, MAG_AUTO_OBS, MAGERR_AUTO_OBS, XPEAK_OBS, YPEAK_OBS, X_IMG_OBS, Y_IMG_OBS, RA_OBS, DEC_OBS = np.loadtxt(j, unpack = True)
            #print(MAG_APP_OBS)
        except: 
            MAG_APP_OBS = 0 
        
        print(MAG_APP_OBS)
        cat_filename = (str(os.path.splitext(j)[0]))
        filenames_pos.append(cat_filename)

    for k in filenames_neg:
        print(k)
        try:
            MAG_APP_OBS, MAGERR_APP_OBS, MAG_AUTO_OBS, MAGERR_AUTO_OBS, XPEAK_OBS, YPEAK_OBS, X_IMG_OBS, Y_IMG_OBS, RA_OBS, DEC_OBS = np.loadtxt(k, unpack = True)
            #print(MAG_APP_OBS)
        except: 
            MAG_APP_OBS = 0 
        
        #print(MAG_APP_OBS)
        cat_filename = (str(os.path.splitext(k)[0]))
        filenames_neg.append(cat_filename)
        
    print(filenames_pos, filenames_neg) 












'''     #   expect 
for filename in os.listdir(path):
    if filename.endswith('pos_SE.cat'):
    MAG_APP_OBS, MAGERR_APP_OBS, MAG_AUTO_OBS, MAGERR_AUTO_OBS, XPEAK_OBS, YPEAK_OBS, X_IMG_OBS, Y_IMG_OBS, RA_OBS, DEC_OBS = np.loadtxt(path + filename, unpack = True)
        cat_filename = (str(os.path.splitext(filename)[0]))
        thresh_pos = (str(os.path.splitext(filename)[1]))
        thresh_num_pos.append(thresh_pos)
        filenames_pos.append(cat_filename)
        cat_length = len(MAG_APP_OBS)
        num_sources_pos.append(cat_length)


filenames_neg = []
num_sources_neg  = []
thresh_num_neg =[]
for filename in os.listdir(path):
    if filename.endswith('neg_SE.cat'):
        try:
        MAG_APP_OBS, MAGERR_APP_OBS, MAG_AUTO_OBS, MAGERR_AUTO_OBS, XPEAK_OBS, YPEAK_OBS, X_IMG_OBS, Y_IMG_OBS, RA_OBS, DEC_OBS = np.loadtxt(path + filename, unpack = True)
        except: 
        MAG_APP_OBS = 0 
        print(MAG_APP_OBS)
        cat_filename = (str(os.path.splitext(filename)[0]))
        thresh_neg = (str(os.path.splitext(filename)[1]))
        thresh_num_neg.append(thresh_neg)
        filenames_neg.append(cat_filename)
        try: 
            cat_length = len(MAG_APP_OBS)
        except TypeError: 
                cat_length = 1
        num_sources_neg.append(cat_length)








        
print(filenames_pos, num_sources_pos)


plt.plot(filenames_pos, num_sources_pos, 'b.')
plt.title('Postive counts vs thresh ext' + str(ext))
plt.xticks(fontsize=4)
plt.xticks(rotation=90)
plt.show()

plt.plot(filenames_neg, num_sources_neg, 'b.')
plt.title('Negative counts vs thresh ext' + str(ext))
plt.xticks(fontsize=4)
plt.xticks(rotation=90)
plt.show()

plt.plot(num_sources_pos, num_sources_neg, 'x')
plt.xticks(fontsize=6)
plt.xticks(rotation=90)
plt.show()
'''
