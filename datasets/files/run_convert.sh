#!/bin/bash
#SBATCH --job-name=adni_conv
#SBATCH --ntasks=4
#SBATCH --mem-per-cpu=16G
#SBATCH --time=12-24:00:00
#SBATCH --output=slurm_%j.out
module load anaconda3
conda activate clinicaEnv
export FREESURFER_HOME=/home/cv/app/freesurfer
source $FREESURFER_HOME/SetUpFreeSurfer.sh
export PATH="/home/cv/app/mricron:$PATH"
export PATH="/home/cv/app/mricrogl:$PATH"
# clinica -v convert adni-to-bids './ADNI' 'Dir/To/Downloaded/Data' './ADNI_converted' -m T1
# clinica -v  convert adni-to-bids '/home/cv/data/ADNI_full/adni_screen_1075/adni_1075/ADNI' \
        # '/home/cv/data/adni/clinical_data' '/home/cv/yb/code/python/cnn_design_for_ad/data/adni_converted' -m T1
# clinica -v convert adni-to-bids './ADNI' '/home/cv/data/adni/clinical_data' '/home/cv/data/ADNI_full/adni_screen_1075/adni_1075_converted'  -m T1
clinica -v convert adni-to-bids '/home/cv/data/ADNI/MRI_PRE_AD_3T_1889/ADNI' '/home/cv/data/adni/clinical_data' '/home/cv/data/ADNI/bids'  -m T1

