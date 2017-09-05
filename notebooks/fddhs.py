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
    if (systolic_blood_pressure > 180 or systolic_blood_pressure < 90 or
        (norm.cdf(systolic_blood_pressure, 130, 10) > 0.95 and
         (norm.cdf(weight, 70, 20) > 0.95 or
          norm.cdf(hearing_threshold, 30, 10) > 0.95))):
        print('You must operate!')
    else:
        print('Send the patient home with some ibuprofen.')