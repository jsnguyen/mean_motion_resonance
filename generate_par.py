import os
import numpy as np

def generate_par(out_folder):

    parameters = {
                  'Setup':               'mmr',
                  'AspectRatio':         0.05,
                  'Sigma0':              '6.73e-7',
                  'SigmaSlope':          1.0,
                  'FlaringIndex':        0.25,
                  'DampingZone':         1.15,
                  'TauDamp':             0.3,
                  'PlanetConfig':        'planets/mmr.cfg',
                  'ThicknessSmoothing':  0.6,
                  'RocheSmoothing':      0.0,
                  'Eccentricity':        0.0,
                  'ExcludeHill':         'no',
                  'IndirectTerm':        'Yes',
                  'Nx':                  128,
                  'Ny':                  64,
                  'Xmin':                -3.14159265358979323844,
                  'Xmax':                3.14159265358979323844,
                  'Ymin':                0.7,
                  'Ymax':                2.7,
                  'OmegaFrame':          1.0,
                  'Frame':               'F',
                  'DT':                  2*np.pi/100,
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
    out_folder_path = '/home/jsn/landing/data/mmr_'+str(increment).zfill(4)

    while os.path.isdir(out_folder_path):
        increment+=1
        out_folder_path = '/home/jsn/landing/data/mmr_'+str(increment).zfill(4)

    generate_par(out_folder_path)

if __name__=='__main__':
    main()
