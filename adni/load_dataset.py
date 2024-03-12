import os
import adni
import numpy as np
import pandas as pd
from os.path import join
import matplotlib.pyplot as plt
from scipy.stats import zscore as zscore_scipy


class Adni(object):

    def __init__(self) -> None:

        self.data_path = self.get_dataset_path()
        self.diagnosis = pd.read_csv(join(self.data_path, "subjects_diagnosis.csv"))
        self.groups = self.diagnosis["Diagnosis"].unique()

    def __str__(self) -> str:
        return "ADNI dataset loader."

    # define a method to give some text output when instance is called
    def __call__(self):
        return "ADNI dataset loader."

    def get_dataset_path(self):

        # find the root address of adni package
        path = adni.__path__[0]
        path = join(path, "..", "dataset")
        return path

    def get_region_labels(self, size=100):
        filename = join(
            self.data_path,
            # f"Schaefer_mrtrix_lut/Schaefer2018_{size}Parcels_7Networks_order_LUT.txt",
            f"Schaefer_mrtrix_lut/ADNI_region_labels_{size}Parcels.txt",
        )
        # load text file including string and numbers, seperated by space
        lines = np.loadtxt(filename, dtype=str)
        return lines

    def get_limbic(self, size=100):

        roi_names = self.get_region_labels(size=size).tolist()

        # lim_region = [
        #     "Hippocampus",
        #     "ParaHippocampal",
        #     "Cingulum",
        #     "Amygdala",
        #     "Temporal_Pole_Sup",
        #     "Temporal_Mid",
        # ]
        regions = [
            "Limbic",
            "Amygdala",
            "Vis_1",
        ]

        vec = []
        idxs = []

        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))

        df = pd.DataFrame({"limbic": vec, "idx": idxs})
        return df

    def get_parietal(self, size=100):
        #!TODO
        roi_names = self.get_region_labels(size=size).tolist()
        # regions = [
        #     "Parietal",
        #     "Postcentral",
        #     "SupraMarginal",
        #     "Angular",
        #     "Precuneus",
        # ]
        
        vec = []
        idxs = []

        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))

        df = pd.DataFrame({"parietal": vec, "idx": idxs})
        return df


    def get_occipital(self, size=100): #!TODO
        roi_names = self.get_region_labels(size=size).tolist()
        regions = [
        ] #!TODO
        
        vec = []
        idxs = []

        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))

        df = pd.DataFrame({"occipital": vec, "idx": idxs})
        return df


    def get_central(self, size=100): #!TODO
        '''get label and indices of central structures regions'''
        roi_names = self.get_region_labels(size=size).tolist()
        regions = [
        ] #!TODO
        
        vec = []
        idxs = []

        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))

        df = pd.DataFrame({"central": vec, "idx": idxs})
        return df


    def frontal(self, size=100):
        '''get label and indices of frontal structures regions'''
        roi_names = self.get_region_labels(size=size).tolist()
        regions = [
        ] #!TODO
        
        vec = []
        idxs = []
        
        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))
                    
        df = pd.DataFrame({"frontal": vec, "idx": idxs})
        return df

    def get_temporal(self, size=100): #!TODO
        '''get label and indices of temporal structures regions'''
        roi_names = self.get_region_labels(size=size).tolist()
        regions = [
        ] #!TODO
        
        vec = []
        idxs = []
        
        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))
                    
        df = pd.DataFrame({"temporal": vec, "idx": idxs})
        return df        

    def get_insulacingulate(self, size=100): #!TODO
        '''get label and indices of insula and cingulate structures regions'''
        roi_names = self.get_region_labels(size=size).tolist()
        regions = [
        ] #!TODO
        
        vec = []
        idxs = []
        
        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))
                    
        df = pd.DataFrame({"insulacingulate": vec, "idx": idxs})
        return df
    
    def get_DMN(self, size=100): #!TODO
        '''get label and indices of default mode network structures regions'''
        roi_names = self.get_region_labels(size=size).tolist()
        regions = [
        ] #!TODO
        
        vec = []
        idxs = []
        
        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))
                    
        df = pd.DataFrame({"DMN": vec, "idx": idxs})
        return df
    
    def get_cingulate(self, size=100): #!TODO
        '''get label and indices of cingulate structures regions'''
        roi_names = self.get_region_labels(size=size).tolist()
        regions = [
        ] #!TODO
        
        vec = []
        idxs = []
        
        for i in roi_names:
            for j in regions:
                if i.find(j) != -1:
                    vec.append(i)
                    idxs.append(roi_names.index(i))
                    
        df = pd.DataFrame({"cingulate": vec, "idx": idxs})
        return df
    
    def find_dirs(self, path, exclude_pattern=None):
        """
        find directories in a given path excluding hidden directories and given list of pattern
        """
        directories = [
            f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))
        ]
        directories = [f for f in directories if not f.startswith(".")]
        if exclude_pattern is not None:
            directories = [
                f for f in directories if not f.startswith(tuple(exclude_pattern))
            ]
        directories.sort()

        return directories

    def check_subdir(self, path, subdir):
        """
        check if there are given subdirectories in each directory
        """
        return all([os.path.isdir(os.path.join(path, sub)) for sub in subdir])

    def check_file_exist(self, path, files):
        """
        check if there are given files in each directory
        """
        # check if there is "___" if files, replace with the name of the directory
        subs = path.split("/")[-1]
        files = [f.replace("___", subs) for f in files]

        return all([os.path.isfile(os.path.join(path, sub)) for sub in files])

    def find_complete_subjects(self, size=100, modality="AV45", verbose=False):
        """
        find complete subjects with given size and modality

        Parameters
        ----------
        path: str
            path to the root directory
        size: int
            size of the atlas, 100 or 400
        modality: str
            modality of the data, "AV45" or "AV1451"
        verbose: bool
            print out the incomplete subjects

        Returns
        -------
        complete_files: list

        """
        path = self.get_dataset_path()

        all_dir = self.find_dirs(path, exclude_pattern=["Schaefer", "output"])
        all_dir.sort()
        subdir = ["dwi", "MNINonLinear", "T1w"]
        complete_folders = []
        for directory in all_dir:
            if self.check_subdir(join(path, directory), subdir):
                complete_folders.append(directory)
        if verbose:
            print(f"Total number of subjects: {len(complete_folders)}")

        if size == 100:
            subdirs = [
                "dwi/weights_Schaefer2018_100Parcels_7Networks.txt",
                "MNINonLinear/Results/rsfMRI/rsfMRI_Atlas_hp2000_clean.Schaefer2018_100Parcels_7Networks_order.ptseries.FAKENII.txt",
                f"T1w/___/{modality}.Schaefer2018_100Parcels_7Networks.output/gtm.txt",
            ]
        else:
            subdirs = [
                "dwi/weights_Schaefer2018_400Parcels_7Networks.txt",
                "MNINonLinear/Results/rsfMRI/rsfMRI_Atlas_hp2000_clean.Schaefer2018_400Parcels_7Networks_order.ptseries.FAKENII.txt",
                f"T1w/___/{modality}.Schaefer2018_400Parcels_7Networks.output/gtm.txt",
            ]
        complete_files = []

        for directory in complete_folders:
            if self.check_file_exist(join(path, directory), subdirs):
                complete_files.append(directory)
            else:
                if verbose:
                    print(directory, end=", ")

        return complete_files

    def get_diagnosis(self, subject: str):
        """Looks up the diagnosis of a given subject."""
        # check if the subject is in the dataset
        if subject not in self.diagnosis["Subject"].values:
            raise ValueError(f"Subject {subject} is not in the dataset.")
        return self.diagnosis[self.diagnosis["Subject"] == subject]["Diagnosis"].values[
            0
        ]

    def get_pet_mask(self, subject: str, size: int = 100, modality="AV45"):
        """Load PET mask for a given subject and size

        Parameters
        ----------
        subject: int
            subject id
        size: int
            size of the atlas, 100 or 400
        modality: str
            modality of the data, "AV45" or "AV1451"
        Returns
        -------
        mask: np.array

        """
        path = Adni().get_dataset_path()
        filename = join(
            path,
            f"{subject}/T1w/{subject}/{modality}.Schaefer2018_{size}Parcels_7Networks.output/gtm.txt",
        )
        mask = np.loadtxt(filename)
        return np.array([float(m) for m in mask])

    def get_weights(self, subject: str, size: int = 100, normalize: bool = True):
        """
        Load connectome for a given subject and size

        Parameters
        ----------
        subject: int
            subject id
        size: int
            size of the atlas, 100 or 400
        normalize: bool
            normalize the connectome matrix

        Returns
        -------
        SC: np.array
            connectome matrix

        """
        path = Adni().get_dataset_path()
        filename = join(
            path, f"{subject}/dwi/weights_Schaefer2018_{size}Parcels_7Networks.txt"
        )
        SC = np.loadtxt(filename)
        if normalize:
            np.fill_diagonal(SC, 0.0)
            SC = SC / np.max(SC)
        return SC

    def get_fmri(self, subject: str, size: int = 100, zscore: bool = False):
        """
        get fMRI data for a given subject and size

        Parameters
        ----------
        subject: int
            subject id
        size: int
            size of the atlas, 100 or 400
        zscore: bool
            zscore the fMRI data

        Returns
        -------
        fmri: np.array [n_regions, n_timepoints]
            fMRI data
        """
        path = Adni().get_dataset_path()
        filename = join(
            path,
            f"{subject}/MNINonLinear/Results/rsfMRI/rsfMRI_Atlas_hp2000_clean.Schaefer2018_{size}Parcels_7Networks_order.ptseries.FAKENII.txt",
        )
        fmri = np.loadtxt(filename)
        if zscore:
            fmri = zscore_scipy(fmri, axis=1)
        return fmri
