import numpy as np
import nibabel as nib
import re
from pathlib import Path

def R2L_and_L2R(m):
    if m:
        if m.group() == "LEFT":
            return "Right-"
        elif m.group() == "RIGHT":
            return "Left-"
    return ''

def reorder_fmri(fMRI_fname,fMRI_ROI_names,SC_ROIs_names,SC_ROIs_idx):
    fmri_data = np.squeeze(nib.load(fMRI_fname).get_fdata())
    new_fmri_data = np.zeros((n_ROIs, fmri_data.shape[1]))
    new_fmri_data[:] = np.NaN
    for idx, name in enumerate(fMRI_ROI_names):
        # deal with cortical area names
        new_name = re.sub("L_7Net|R_7Net","7Net",name)

        # deal with subcortical area names
        m = re.search("LEFT|RIGHT",name)
        if m :
            new_name = re.sub("_LEFT|_RIGHT","",name)
            new_name = str(R2L_and_L2R(m)+new_name[0]+new_name[1:].lower())
            new_name = re.sub("Cerebellum","Cerebellum-Cortex",new_name)
            new_name = re.sub("Accumbens","Accumbens-area",new_name)

        new_idx = SC_ROIs_idx[np.where(SC_ROIs_names==new_name)[0]]-1
        # print(f"ROI : {new_name} - {idx} - {new_idx}")
        if not len(new_idx) == 0:
            new_fmri_data[new_idx,:] = fmri_data[idx,:]

    assert np.isnan(new_fmri_data).sum() == 0, "Not all ROIs were assigned with a timeseries. Check data or ROI naming."
    np.savetxt(fMRI_fname.strip("nii.gz")+".txt", new_fmri_data)
    print(f"Reordered {fMRI_fname}")

 
def reorder_PET(PET_fname,PET_ROI_names,SC_ROIs_names,SC_ROIs_idx):
    PET_data = np.squeeze(nib.load(PET_fname).get_fdata())
    new_PET_data = np.zeros((n_ROIs))
    new_PET_data[:] = np.NaN
    for idx, name in enumerate(PET_ROI_names):
        # deal with cortical regions
        new_name = re.sub('ctx-lh-|ctx-rh-',"",name)
        new_idx = SC_ROIs_idx[np.where(SC_ROIs_names==new_name)[0]]-1
        # print(f"ROI : {new_name} - {idx} - {new_idx}")
        if not len(new_idx) == 0:
            new_PET_data[new_idx] = PET_data[idx]

    assert np.isnan(new_PET_data).sum() == 0, "Not all ROIs were assigned with some data. Check data or ROI naming."
    np.savetxt(PET_fname.strip("nii.gz")+".txt", new_PET_data)
    print(f"Reordered {PET_fname}")
 

if __name__ == '__main__':
    import sys
    parcellation   = sys.argv[1]
    PET_ROI_names  = np.genfromtxt(f"PET_ROI_order_{parcellation}_order.txt", dtype=str)
    fMRI_ROI_names = np.genfromtxt(f"fMRI_ROI_ordering_{parcellation}_order.txt", dtype=str)
    SC_ROIs_names  = np.genfromtxt(f"Schaefer_mrtrix_lut/{parcellation}_order_LUT.txt", dtype=str, usecols=[1])
    SC_ROIs_idx    = np.genfromtxt(f"Schaefer_mrtrix_lut/{parcellation}_order_LUT.txt", dtype=int, usecols=[0])
    n_ROIs = SC_ROIs_idx.max()

    fname = sys.argv[3]
    if sys.argv[2] == "reorder_fmri":
        reorder_fmri(fname,fMRI_ROI_names,SC_ROIs_names,SC_ROIs_idx)
    elif sys.argv[2] == "reorder_PET":
        reorder_PET(fname,PET_ROI_names,SC_ROIs_names,SC_ROIs_idx)
    else : 
        print(f"The function {sys.argv[2]} is not known.")