import os
import shutil
import glob
from tqdm import tqdm

Raw_DIR= r'C:\Users\HP\Desktop\SGP\Driver Drowsiness System\mrlEyes_2018_01'
for dirpath, dirname, filenames in os.walk(Raw_DIR):
    for i in tqdm([f for f in filenames if f.endswith('.png')]):
        if i.split('_')[4]=='0':
            shutil.copy(src=dirpath+'/'+i, dst=r'C:\Users\HP\Desktop\SGP\Driver Drowsiness System\train\Closed eyes')
        
        elif i.split('_')[4]=='1':
            shutil.copy(src=dirpath+'/'+i, dst=r'C:\Users\HP\Desktop\SGP\Driver Drowsiness System\train\Open eyes')