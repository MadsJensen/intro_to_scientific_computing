"""Helper functions and support code for Foundations of data-driven health science
"""
##
import numpy as np
from scipy.stats import norm
##

def decision_machine(systolic_blood_pressure, weight,
                     hearing_threshold):
    """To operate or not to operate?!

    systolic_blood_pressure (mmHg)
    weight (kg)
    hearing_threshold (dB)
    
    """    
    if (norm.cdf(systolic_blood_pressure, 140, 15) > 0.99 and
        norm.cdf(weight, 70, 10) > 0.99 and
        norm.cdf(hearing_threshold, 30, 5) > 0.99):
        print('You must operate!')
    else:
        print('Send the patient home with some ibuprofen.')