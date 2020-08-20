#!/bin/bash
#SBATCH --job-name=adni_preprocess
#SBATCH --ntasks=24
#SBATCH --mem-per-cpu=16G
#SBATCH --time=12-24:00:00
#SBATCH --output=slurm_%j.out

conda  activate clinicaEnv
module load anaconda3

module load matlab
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export MATLAB_HOME=/home/cv/app/matlab/r2017b
export PATH=${MATLAB_HOME}:${PATH}
export MATLABCMD=${MATLAB_HOME}/bin/matlab
conda activate clinicaEnv
export FREESURFER_HOME=/home/cv/app/freesurfer
source $FREESURFER_HOME/SetUpFreeSurfer.sh
export SPM_HOME=/home/cv/app/matlab/r2017b/toolbox/spm12
# clinica run t1-volume '/home/cv/data/ADNI_full/adni_screen_1075/adni_1075_converted' '/home/cv/data/ADNI_full/adni_screen_1075/adni_1075_processed' 'TRAIN' -tsv \
#         'train_adni_806.tsv' -wd '/home/cv/data/ADNI_full/adni_screen_1075/WD_train' -np 24

clinica run t1-volume '/home/cv/data/ADNI_full/adni_screen_1075/adni_1075_converted' './adni_1075_processed' 'TRAIN' -tsv \
        'test.tsv' -wd './WD_train' -np 24



