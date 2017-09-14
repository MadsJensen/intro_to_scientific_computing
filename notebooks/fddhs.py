"""Helper functions and support code for Foundations of data-driven health science
"""
##
import os
import re
import glob
import random
import string
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

        
def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


def random_filename(fname_len=8, sufflist=None):
    
    fname = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + '-_',
                                   k=fname_len))

    if sufflist is None:
        suffix = ''.join(random.choices(string.ascii_lowercase, k=3))
    elif isinstance(sufflist, list):
        suffix = random.choices(sufflist, k=1)[0]
        
    return(fname + '.' + suffix)


def create_nested_dirstruct(root, fromlevel, tolevel=4, sublevels=4, fake=False,
                            files_per_level=10, fname_len=8, sufflist=None):
    '''Create up to `tolevel` nested directories with `sublevels` each
    '''
    
    this_nest = []
    
    subnames = list(string.ascii_uppercase[:sublevels])
    
    if not os.path.exists(root):
        os.makedirs(root)

    for sn in subnames:
        if fromlevel <= tolevel:
            newdir = os.path.join(root, 'level%d' % fromlevel + sn)
            if fake:
                print('os.makedirs({})'.format(newdir))
            else:
                os.makedirs(newdir, exist_ok=True)
                for _ in range(files_per_level):
                    fname = os.path.join(newdir,
                                         random_filename(fname_len=fname_len,
                                                         sufflist=sufflist))
                    touch(fname)
                    this_nest += [fname]

            this_nest += create_nested_dirstruct(newdir, fromlevel + 1,
                                                 tolevel=tolevel, sublevels=sublevels,
                                                 fake=fake, sufflist=sufflist,
                                                 files_per_level=files_per_level,
                                                 fname_len=fname_len)
        
    return(this_nest)


def explode_text_to_files(file_list, text='dickens.txt'):
    '''Take a list of files and a file with rows of text,
    spread the rows into the files, adding line numbers.'''

    inject_to = list(range(len(file_list)))
    random.shuffle(inject_to)
    with open(text, 'rt') as fp:
        lines = fp.readlines()
        lines = [l for l in lines if not l.startswith('#')]
        lines[-1] += '\n' if not lines[-1].endswith('\n') else ''
        del inject_to[len(lines):]
    
    for lno, (fileno, line) in enumerate(zip(inject_to, lines)):
        with open(file_list[fileno], 'wt') as fp:
            fp.write('{:02d}: {:s}'.format(lno, line))

    return(inject_to)


def grep(filename, string):
    for line in open(filename):
        if re.search(string, line):
            return(line.rstrip())

    raise RuntimeError('No matches for {} in {}'.format(string, filename))


def find(directory, wildcard):
    return(glob.glob(os.path.join(directory, wildcard)))


def mean(values):
    '''Return the mean of a list of numbers'''
    return(sum(values)/len(values))


def median(values):
    '''Return the median of a list of numbers
    NB: Should be corrected for the case of even number of values!
    '''
    return(sorted(values)[len(values) // 2])


def read_log_file(logfile_name, field_sep='\t'):
    '''Read a single log file
    
    The field-separator is assumed to be the tab-character (\t)
    
    Return the mean and median RT, and the accuracy, separately for
    the frequent and rare categories. This is done as a list (tuple) of
    6 return values, in the order:
    (mean_rt_freq, median_rt_freq, accuracy_freq,
     mean_rt_rare, median_rt_rare, accuracy_rare)
    '''

    rt_freq = []
    rt_rare = []
    n_corr_freq = 0
    n_corr_rare = 0

    # open file and read it
    fp = open(logfile_name, 'r')
    all_lines = fp.readlines()
    fp.close()

    # hard-code the index of the stimulus/response type/number
    idx = 5
    
    # loop over lines from 6th onwards
    for line in all_lines[5:]:
        split_line = line.split(field_sep)

        if split_line[2].startswith('STIM'):
            stim_time = split_line[0]
            cur_stim = split_line[2][idx]
        else:
            split_line = line.split(field_sep)

            resp_time = split_line[0]
            cur_resp = split_line[2][idx]

            # calculate RT
            RT = int(resp_time) - int(stim_time)

            if cur_stim in string.ascii_lowercase:
                rt_freq.append(RT)
                if cur_resp == '1':
                    n_corr_freq += 1
            elif cur_stim in string.digits:
                rt_rare.append(RT)            
                if cur_resp == '2':
                    n_corr_rare += 1    

    # calculate return values
    # freq
    mean_rt_freq = mean(rt_freq) * 100e-3
    median_rt_freq = median(rt_freq) * 100e-3
    accuracy_freq = 100 * n_corr_freq / len(rt_freq)

    # rare
    mean_rt_rare = mean(rt_rare) * 100e-3
    median_rt_rare = median(rt_rare) * 100e-3
    accuracy_rare = 100 * n_corr_rare / len(rt_rare)                    
                    
    return(mean_rt_freq, median_rt_freq, accuracy_freq,
           mean_rt_rare, median_rt_rare, accuracy_rare)


if __name__ == '__main__':
    # everyone's special :)
    # import socket
    # random.seed(socket.gethostname())
    # but for the sake of teaching...
    random.seed('hathor')

    initloc = os.path.dirname(__file__)
    print('Initialising to: {:s} ...'.format(initloc))
    nest = create_nested_dirstruct('exercises/level0', 1, 4, sublevels=4,
                                   sufflist=['txt', 'log', 'bat', 'dat',
                                             'htm', 'html', 'yaml'])
    inject = explode_text_to_files(nest)


