import pandas as pd 
import os
import random
import numpy as np

src_csv = pd.read_csv('adni_full.tsv',sep='\t',header=0)


index_ses = pd.DataFrame(['ses-M00','ses-M06','ses-M12'],columns=['session_id'])


mci_csv = src_csv[src_csv['diagnosis'] == 'MCI']
ad_csv = src_csv[src_csv['diagnosis'] == 'AD']
cn_csv = src_csv[src_csv['diagnosis'] == 'CN']

mci_csv = pd.merge(mci_csv,index_ses)
ad_csv = pd.merge(ad_csv,index_ses)
cn_csv = pd.merge(cn_csv,index_ses)
print(mci_csv,"\n",type(mci_csv))

mci_csv_1 = mci_csv.sort_values(by='participant_id',axis=0, ascending=True)

print(mci_csv_1,"\n",type(mci_csv_1))
ad_csv_1 =  ad_csv.sort_values(by='participant_id',axis=0, ascending=True)
cn_csv_1 = cn_csv.sort_values(by='participant_id',axis=0, ascending=True)

# print(mci_csv,"\n",type(mci_csv))




mci_csv_1.to_csv('mci_1y.tsv',sep='\t',index=None)
ad_csv_1.to_csv('ad_1y.tsv',sep='\t',index=None)
cn_csv_1.to_csv('cn_1y.tsv',sep='\t',index=None)
