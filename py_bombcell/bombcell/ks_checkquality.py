import pandas as pd 
import numpy as np
import os

from loading_utils import load_ephys_data, load_bc_results


# # def doClassifications():
# #     '''
# #     Copy pasted from bombcell thing w my thresholds hard coded in here
# #     '''


# #def checkGoodTimes(bombcelldir):

# def classifyUnits(bombcelldir,minpctgood = 90, classifyparams):
#     paramfile = bombcelldir.parent/'params.py'
#     namespace = {}
#     exec(paramfile.read_text(), {}, namespace)
#     ##get things for bombcell from the phy params.py
#     n_channels_dat = int(namespace["n_channels_dat"])
#     sample_rate = float(namespace["sample_rate"])
#     chunkIDXes = np.load(bombcelldir/'chunkIDXs.npy')

#     allchunks = os.listdir(bombcelldir)


