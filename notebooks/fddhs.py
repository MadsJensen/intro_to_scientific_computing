"""Helper functions and support code for Foundations of data-driven health science
"""
##
import os
import numpy as np
from scipy.stats import norm
##

def decision_machine(systolic_blood_pressure, bmi,
                     hearing_threshold):
    """To operate or not to operate?!

    systolic_blood_pressure (mmHg)
    boody-mass index (kg/m^2)
    hearing_threshold (dB)
    
    """    
    if (systolic_blood_pressure > 180 or systolic_blood_pressure < 90 or
        (norm.cdf(systolic_blood_pressure, 130, 10) > 0.95 and
         (norm.cdf(bmi, 23, 4) > 0.95 or
          norm.cdf(hearing_threshold, 30, 8) > 0.95))):
        print('Prepare the patient for immediate surgery!')
    else:
        print('Send the patient home with some ibuprofen.')
        

def initialise_folder_structure(depth=5, touch_files=0):
    """Make nested folder structure and optional files
    
    level0/
    |- level1/
    |   |- level2a/
    |   |- file1
    |   |- file2
    """
    
    