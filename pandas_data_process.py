import pandas as pd 
import re

# sub_data = pd.read_csv('./sub_list.txt',header=0)
# adni_data = pd.read_csv('./ADNIMERGE.csv',header=0)

# merge_data = pd.merge(adni_data,sub_data,how='inner',on=['PTID'])

# merge_data.to_csv('./adnimerge.csv',sep=',')

t1_path = pd.read_csv('./t1_paths.tsv',sep='\t',header=0)
t2 = t1_path.dropna()
# t2['sub-id'] = t2.apply(lumbar x: self.bug_rule(x,"Subject_ID",axis=1))

# for subj in t2:
#     subj.sub-id = 'sub-ADNI' +replace_sequence_chars(subj.Subject_ID)
def session(x):
    if x== "bl":
        return "ses-M00"

t2['participant_id']= t2["Subject_ID"].apply(lambda x : ('sub-ADNI' + re.sub('[ /_*()<>:]', '', x)))
t2['session_id']= t2["VISCODE"].apply(lambda x : session(x) )

t3 = t2[['participant_id','session_id']].reset_index(drop=True) #去除不连续的索引

# def bug_rule(self,frame,type):

# t1_path[]


# t3.to_csv('all_adni_1075.tsv',sep='\t')


##########划分数据集#########
t3 = t3.sample(frac=1.0).reset_index(drop=True)  #全部打乱
train_idx = int(round(0.7*t3.shape[0]))
test_idx = int(round(0.85*t3.shape[0]))

print(t3.shape[0],train_idx,test_idx)

t3_train = t3.iloc[:train_idx]
t3_test = t3.iloc[train_idx:test_idx]
t3_val = t3.iloc[test_idx:]

t3_train.to_csv('train_adni_806.tsv',sep='\t',index=None)
t3_test.to_csv('test_adni_806.tsv',sep='\t',index=None)
t3_val.to_csv('val_adni_806.tsv',sep='\t',index=None)
