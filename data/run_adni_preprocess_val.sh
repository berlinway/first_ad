#!/bin/bash
#SBATCH --job-name=adni_preprocess
#SBATCH --ntasks=24
#SBATCH --mem-per-cpu=16G
#SBATCH --time=12-24:00:00
#SBATCH --output=slurm_%j.out

module load anaconda3

module load matlab
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export MATLAB_HOME=/home/cv/app/matlab/r2017b
export PATH=${MATLAB_HOME}:${PATH}
export MATLABCMD=${MATLAB_HOME}/bin/matlab
conda activate yb
export FREESURFER_HOME=/home/cv/app/freesurfer
source $FREESURFER_HOME/SetUpFreeSurfer.sh
export SPM_HOME=/home/cv/app/matlab/r2017b/toolbox/spm12
# clinica run t1-volume-existing-template '/home/cv/data/adni/bids' '/home/cv/data/adni/processed1'  'TRAIN'  -tsv './ptid_val.tsv' -wd '/home/cv/data/adni/WD_train1' -np 50 

clinica run t1-volume-register-dartel '/home/cv/data/adni/bids' '/home/cv/data/adni/processed1'  'TRAIN'  -tsv './ptid_val.tsv' -wd '/home/cv/data/adni/WD_train1' -np 50 

clinica run t1-volume-dartel2mni  '/home/cv/data/adni/bids' '/home/cv/data/adni/processed1'  'TRAIN'  -tsv './ptid_val.tsv' -wd '/home/cv/data/adni/WD_train1' -np 50 

clinica run t1-volume-parcellation   '/home/cv/data/adni/processed1'  'TRAIN'  -tsv './ptid_val.tsv' -wd '/home/cv/data/adni/WD_train1' -np 50 


