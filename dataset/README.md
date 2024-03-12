# UPDATE 20.12.2022

All PET and fMRI data have been reordered and written into a `*txt` file. 
The `*txt` file resides in the same directory as the original file, sharing the same file name (besides the different ending).
The new ordering is consistent with the ordering of the SCs



ORIGINAL
This directory contains the data necessary for Meysam and Abolfazl to run SBI and simulations with the patient specific ADNI data. 

##################################################################################################
## PET AV45 and AV1451
Currently only Schaefer2018_400Parcels_7Networks parcellation.
Including all subjects that were used for the PET GLM analysis.
Thus 219 and 147 patients for AV1451 and AV45, respectively.
There are 2 Nifti files for each PET modality.
"gtm.nii.gz"/ "nopvc.nii.gz" containing ROI PET values applying/ not applying partial volume correction 
They can be easily read in python using the nibabel package
E.g.
    import nibabel as nib
    img = nib.load("gtm.nii.gz")
    data = img.get_fdata() # data will be a numpy array

The ordering of the ROIs can be taken from pet_nii_ROI_order_Schaefer2018_400Parcels_7Networks.txt 
There are the ROIs of the cortical Schaefer parcellation, some subcortical ROIs and a few ROIs which are not of interest for us. 
Check the ROI ordering of the the structural connectivity to map the PET loads.

##################################################################################################
## Structural connectivity
Schaefer2018_400Parcels_7Networks parcellation and Schaefer2018_100Parcels_7Networks parcellation
Including all subjects that were used for the FBA GLM analysis. 
There are 2 subgroups. The larger group received a single shell diffusion scan including 48 directions with a voxel size of 2mm^3. 
The smaller group received a higher resolution multi-shell diffusion scan. 

Check 
good_subjects_w_sc_single_shell_48dir_2mm_voxsize.txt
and 
good_subjects_w_sc_multi_shell.txt
for the subjects of each group respectively.

If necessary, there would be a 3rd group of subjects, with single shell diffusion scans that are somewhere inbetween the first 2 groups. 
For the FBA analysis I wanted to keep data quality as similar as possible and thus excluded those subjects. 

For each subject there is a SC weights and lenghts matrix. 

Check the files in ./Schaefer_mrtrix_lut for the ROI ordering of the connectomes. 
Order is first left, second right hemisphere and third subcortical structures. 
NOTE: Thalamus and Thalamus-Proper are mapping to the same region. This is used by MRtrix to work with Freesurfer file format. 



## ROI fMRI timeseries
Schaefer2018_400Parcels_7Networks parcellation and Schaefer2018_100Parcels_7Networks parcellation
Including all subjects that were used for the Group ICA GLM analysis. 
Again there are 2 subgroups. There are 191 and 51 patients with lowres and hires data, respectively. 
Check 
gica_sublist_hires.txt
and
gica_sublist_hires.txt
for the subjects in each group, respectively.

For each subject there are 2 Files
rsfMRI_Atlas_hp2000_clean.Schaefer2018_100Parcels_7Networks_order.ptseries.FAKENII.nii.gz
and 
rsfMRI_Atlas_hp2000_clean.Schaefer2018_400Parcels_7Networks_order.ptseries.FAKENII.nii.gz

Those again are Nifti files, which can be read in python using the nibabel package. 

For the ROI ordering check files
fMRI_ROI_ordering_Schaefer2018_100Parcels_7Networks_order.txt
and
fMRI_ROI_ordering_Schaefer2018_400Parcels_7Networks_order.txt

There are a few areas that do not appear in the structural connectome. E.g. Brainstem and L/R - VentralDiencephalon.
Just ignore those.

##################################################################################################
##### General remarks
You will see that not every subject has every modality. 
This might be cause the modality was not acquired in the first place, the processing failed or I excluded because parameters of the data were to
different. 
But I can possible add more subjects if needed. 
E.g. the subjects that failed processing could be done with some manual editing which I didn't do for now because it takes a little bit of time.
