Run these lines on the command line and activate the correct conda environment before. 
These lines will reorder PET and fMRI data and write them into a *txt file, such that the order corresponds to the ROI ordering in the connectome. 
#conda activate jlabdask

#find "$(pwd -P)" -name "*100Parcels_7Networks_order*FAKENII.nii.gz" | xargs -I % python reorder_ROIs_for_all_modalities.py Schaefer2018_100Parcels_7Networks reorder_fmri %
#find "$(pwd -P)" -name "*400Parcels_7Networks_order*FAKENII.nii.gz" | xargs -I % python reorder_ROIs_for_all_modalities.py Schaefer2018_400Parcels_7Networks reorder_fmri %
#find "$(pwd -P)" -wholename "*T1w/*/AV*Schaefer2018_100Parcels_7Networks*/*nii.gz" | xargs -I % python reorder_ROIs_for_all_modalities.py Schaefer2018_100Parcels_7Networks reorder_PET %
#find "$(pwd -P)" -wholename "*T1w/*/AV*Schaefer2018_400Parcels_7Networks*/*nii.gz" | xargs -I % python reorder_ROIs_for_all_modalities.py Schaefer2018_400Parcels_7Networks reorder_PET %
