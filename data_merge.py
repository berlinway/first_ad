import pandas  as pd 

import os 
import random
import numpy as np

def div_data(convert_subj,index,per1,per2):
    k = index[int(len(index)*per1):int(len(index)*per2)]
    div_subj = []
    for i in k:
        div_subj.append(convert_subj[i])
    return div_subj


def age_round_func(x):

    # if x is nan:
    #     return x

    print(x)
    i = x- int(x)
    # res = x
    

    if i>0.0 and i<0.5:
        x = 0.5+ int(x)
    if i>0.5 and i<1.0:
        x = 1.0+int(x)
    return x


#去除标签中病例为nan的值
def diagnosis_drop_nan(tsv_data_raw):
    nan_index = tsv_data_raw[np.isnan(tsv_data_raw['diagnosis'])].index
    tsv_data_raw = tsv_data_raw.drop(nan_index,inplcae=True)
    return tsv_data_raw


def concat_csv(obj_csv,path,drop_nan=False):
    data_frame = ['participant_id','session_id','diagnosis','MMSE','cdr_global','cdr_sb','age','examination_date','age_round']
    # data_frame1 = ['participant_id','session_id','diagnosis','MMSE','cdr_global','cdr_sb','age','examination_date','age_round']
    dst = pd.DataFrame(columns=data_frame)
    for subj in obj_csv:
        if 'sub-ADNI' not in subj:
            continue
        ses_subj = list(os.listdir(os.path.join(path,subj)))
        ses_folder = []
        tsv_file = []

        #ses 和tsv文件分开
        for i in ses_subj:
            if 'ses-' in i:
                ses_folder.append(i)
            elif subj in i:
                    tsv_file.append(i)
            else:
                continue
        tsv_data = pd.read_csv(os.path.join(path,subj,tsv_file[0]),sep='\t',header=0)
        if drop_nan:    
            tsv_data = diagnosis_drop_nan(tsv_data)

        tsv_data['participant_id'] = subj
        # tsv_data = tsv_data[data_frame1].dropna().reset_index(drop=True)

        #nan值用0填充
        tsv_data =  tsv_data.fillna(0)
        tsv_data['age_round'] =  tsv_data['age'].apply(lambda x: age_round_func(float(x)))

        
        dst_csv = tsv_data[data_frame].dropna().reset_index(drop=True)
        # index_ses = []
        # ses_col = dst_csv['session_id']
        # for i in ses_folder:
        #     index_ses.append(ses_col.index(i))
        index_ses = pd.DataFrame(['ses-M00','ses-M06','ses-M12'],columns=['session_id'])
        dst_csv = pd.merge(dst_csv,index_ses)
        # dst_csv = dst_csv.iloc[index_ses]
        print(dst_csv)
        dst = pd.concat([dst,dst_csv],axis=0)

    print(dst)
    return dst

if __name__ == "__main__":

    path = '/home/cv/data/ADNI/MCI/bids'
    convert_subj = list(os.listdir(path))


    index = [i for i in range(len(convert_subj))]
    random.shuffle(index)

    ##划分数据集，按照0.7 ： 0.15 ：0.15的比例划分
    # k = index[:int(len(index)*0.7)]
    train_subj= div_data(convert_subj,index,0,1.0)
    # test_subj= div_data(convert_subj,index,0.7,0.85)
    # val_subj= div_data(convert_subj,index,0.85,1)


    # train_subj = convert_subj[index[:int(len(index)*0.7)]]
    # test_subj = convert_subj[index[int(len(index)*0.7):int(len(index)*0.85)]]
    # val_subj = convert_subj[index[int(len(index)*0.85):]]


    train_csv = concat_csv(train_subj,path)
    # test_csv = concat_csv(test_subj,path)
    # val_csv = concat_csv(val_subj,path)

    # train_csv.to_csv('mri_pre_ad.tsv',sep='\t',index=None)
    # train_csv.to_csv('mri_pre_cn.tsv',sep='\t',index=None)
    train_csv.to_csv('mri_pre_mci_01.tsv',sep='\t',index=None)











    


