import os
import numpy as np
from pathlib import Path

def generate_par(out_folder):

    parameters = {
                  'Setup':               'mmr',
                  'AspectRatio':         0.05,
                  'Sigma0':              '2.0e-6',
                  'SigmaSlope':          0.8,
                  'FlaringIndex':        0.25,
                  'DampingZone':         1.15,
                  'TauDamp':             0.3,
                  'PlanetConfig':        'planets/mmr.cfg',
                  'ThicknessSmoothing':  0.6,
                  'RocheSmoothing':      0.0,
                  'Eccentricity':        0.0,
                  'ExcludeHill':         'no',
                  'IndirectTerm':        'Yes',
                  'AlphaIn':             '1.0e-5',
                  'AlphaOut':            '7.5e-3',
                  'Rmid':                27.0, # middle of disk units of AU
                  'Rc':                  60.0, # disk cutoff units of AU
                  'SigmaVisc':           1.0,
                  'Nx':                  64,
                  'Ny':                  32,
                  'Xmin':                -3.14159265358979323844,
                  'Xmax':                3.14159265358979323844,
                  'Ymin':                10.0,
                  'Ymax':                45.0,
                  'OmegaFrame':          1.0,
                  'Frame':               'F',
                  'DT':                  2*np.pi/10,
                  'Ninterm':             10,
                  'Ntot':                100000,
                  'OutputDir':           out_folder
                  }

    par_filename = './mmr/mmr.par'

    with open(par_filename, 'w') as f:
        for el in parameters.keys():
            f.write('{:32} {:64}'.format(el,str(parameters[el])).rstrip()+'\n')

def main():
    increment=0
    prepath = str(Path.home())
    print(prepath)
    out_folder_path = prepath+'/landing/data/mmr_'+str(increment).zfill(4)

    while os.path.isdir(out_folder_path):
        increment+=1
        out_folder_path = prepath+'/landing/data/mmr_'+str(increment).zfill(4)

    generate_par(out_folder_path)

if __name__=='__main__':
    main()
