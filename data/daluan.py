import pandas as pd 
import os
import random
import numpy as np

def luanxu(path):
    src_csv = pd.read_csv(path,sep='\t',header=0)

    ptid = src_csv['participant_id'].unique()
    print(ptid,type(ptid))

    index_ses = pd.DataFrame(ptid,columns=['participant_id'])

    ptid_luan = index_ses.sample(frac=1.0).reset_index(drop=True) #打乱操作
    
    dst_csv = pd.merge(ptid_luan,src_csv)
    return dst_csv



# train_csv = luanxu('train.tsv')
# ptid_train = train_csv[['participant_id','session_id']]
# train_csv.to_csv('adni_train.tsv',sep='\t',index=None)
# ptid_train.to_csv('ptid_train.tsv',sep='\t',index=None)

# test_csv = luanxu('test.tsv')
# ptid_test = test_csv[['participant_id','session_id']]
# test_csv.to_csv('adni_test.tsv',sep='\t',index=None)
# ptid_test.to_csv('ptid_test.tsv',sep='\t',index=None)

# val_csv = luanxu('val.tsv')
# ptid_val = val_csv[['participant_id','session_id']]
# val_csv.to_csv('adni_val.tsv',sep='\t',index=None)
# ptid_val.to_csv('ptid_val.tsv',sep='\t',index=None)



train_csv = pd.read_csv('adni_train.tsv',sep='\t',header=0)
ptid_train = train_csv[['participant_id','session_id']]
# train_csv.to_csv('adni_train.tsv',sep='\t',index=None)
ptid_train.to_csv('ptid_train.tsv',sep='\t',index=None)

test_csv = pd.read_csv('adni_test.tsv',sep='\t',header=0)
ptid_test = test_csv[['participant_id','session_id']]
# test_csv.to_csv('adni_test.tsv',sep='\t',index=None)
ptid_test.to_csv('ptid_test.tsv',sep='\t',index=None)

val_csv = pd.read_csv('adni_val.tsv',sep='\t',header=0)
ptid_val = val_csv[['participant_id','session_id']]
# val_csv.to_csv('adni_val.tsv',sep='\t',index=None)
ptid_val.to_csv('ptid_val.tsv',sep='\t',index=None)





