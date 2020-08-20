import pandas as pd 
import  os
from os import walk

# csv_path = '/home/cv/yb/code/python/cnn_design_for_ad/datasets/files/ADNI_converted/conversion_info/t1_paths.tsv'
# t1_col_df = ['Subject_ID', 'VISCODE', 'Visit', 'Sequence', 'Scan_Date',
#                  'Study_ID', 'Field_Strength', 'Series_ID', 'Image_ID', 'Original','Is_Dicom','Path']
# image = pd.read_csv(csv_path,sep='\t')

# print(image.shape)

adni_sl_dir = './datasets/files/ADNI'
f = open('sub_list.txt',"a")

for i in os.listdir(adni_sl_dir):
    f.write("{}\n".format(i))
f.close()








