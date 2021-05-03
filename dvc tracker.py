# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:52:32 2021

@author: Avinash Jha
"""

# NOTE: For windows user-
# This file must be created in the root of the project 
# where Training and Prediction batch file as are present

import os
from glob import glob


data_dirs = ["Training_Batch_Files","Prediction_Batch_files"]

for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        # print(f"dvc add {filePath}")
        os.system(f"dvc add {filePath}")

print("\n #### all files added to dvc ####")