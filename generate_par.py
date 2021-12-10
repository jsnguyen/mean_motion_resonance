import os
import argparse

import numpy as np
from pathlib import Path

def generate_par(out_folder, run_name):
    
    print('Making run_name parameter file:',run_name)

    parameters = {
                  'Setup':               'mmr',
                  'AspectRatio':         0.05,
                  'Sigma0':              '2.0e-6',
                  'SigmaSlope':          0.8,
                  'FlaringIndex':        0.25,
                  'DampingZone':         1.15,
                  'TauDamp':             0.3,
                  'ThicknessSmoothing':  0.6,
                  'RocheSmoothing':      0.0,
                  'Eccentricity':        0.0,
                  'ExcludeHill':         'no',
                  'IndirectTerm':        'Yes',
                  'AlphaIn':             '1.0e-5',
                  'AlphaOut':            '7.5e-3',
                  'SigmaVisc':           1.0,
                  'Nx':                  32*3,
                  'Ny':                  32,
                  'Xmin':                -3.14159265358979323844,
                  'Xmax':                3.14159265358979323844,
                  'OmegaFrame':          0.0, # sqrt(1/r1)
                  'Frame':               'F',
                  'DT':                  2*np.pi/10,
                  'Ninterm':             100,
                  'Ntot':                1000000,
                  'OutputDir':           out_folder
                  }


    if run_name == '1_2':
        # 1:2
        parameters['PlanetConfig'] = 'planets/mmr_1_2.cfg'
        parameters['Epsilon'] = 15.0 # units dimensionless parameter, multiplies R0 factor so R0 can be zero if scale free
        parameters['Rmid'] = 18.0 # middle of disk units of AU
        parameters['Rc'] = 30.0 # disk cutoff units of AU
        parameters['Ymin'] = 10.0
        parameters['Ymax'] = 25.0

    elif run_name == '1_2_4':
        # 1:2:4
        parameters['PlanetConfig'] = 'planets/mmr_1_2_4.cfg'
        parameters['Epsilon'] = 50.0 # units dimensionless parameter, multiplies R0 factor so R0 can be zero if scale free
        parameters['Rmid'] = 43.0 # middle of disk units of AU
        parameters['Rc'] = 135.0 # disk cutoff units of AU
        parameters['Ymin'] = 45.0
        parameters['Ymax'] = 130.0

    elif run_name == '1_2_4_8':
        # 1:2:4:8
        parameters['Eccentricity'] = 0.0125
        parameters['PlanetConfig'] = 'planets/mmr_1_2_4_8.cfg'
        parameters['Epsilon'] = 75.0 # units dimensionless parameter, multiplies R0 factor so R0 can be zero if scale free
        parameters['Rmid'] = 130.0 # middle of disk units of AU
        parameters['Rc'] = 330.0 # disk cutoff units of AU
        parameters['Ymin'] = 75.0
        parameters['Ymax'] = 325.0

    par_filename = './mmr/mmr.par'

    with open(par_filename, 'w') as f:
        for el in parameters.keys():
            f.write('{:32} {:64}'.format(el,str(parameters[el])).rstrip()+'\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('run_name', type=str)

    args = parser.parse_args()

    increment=0
    prepath = str(Path.home())
    print(prepath)
    out_folder_path = prepath+'/landing/data/mmr_'+str(increment).zfill(4)

    while os.path.isdir(out_folder_path):
        increment+=1
        out_folder_path = prepath+'/landing/data/mmr_'+str(increment).zfill(4)

    generate_par(out_folder_path, args.run_name)

if __name__=='__main__':
    main()
