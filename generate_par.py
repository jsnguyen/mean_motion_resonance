import numpy as np

def main():

    parameters = {
                  'Setup':               'mmr',
                  'AspectRatio':         0.05,
                  'Sigma0':              '6.3661977237e-4',
                  'Nu':                  '1.0e-5',
                  'SigmaSlope':          0.0,
                  'FlaringIndex':        0.0,
                  'DampingZone':         1.15,
                  'TauDamp':             0.3,
                  'PlanetConfig':        'planets/mmr.cfg',
                  'ThicknessSmoothing':  0.6,
                  'RocheSmoothing':      0.0,
                  'Eccentricity':        0.0,
                  'ExcludeHill':         'no',
                  'IndirectTerm':        'Yes',
                  'Nx':                  384,
                  'Ny':                  128,
                  'Xmin':                -3.14159265358979323844 ,
                  'Xmax':                3.14159265358979323844,
                  'Ymin':                0.7,
                  'Ymax':                2.7,
                  'OmegaFrame':          1.0,
                  'Frame':               'F',
                  'DT':                  2*np.pi/100,
                  'Ninterm':             10,
                  'Ntot':                1000000,
                  'OutputDir':           '/Users/jsn/test'
                 }

    par_filename = './mmr/mmr.par'

    with open(par_filename, 'w') as f:
        for el in parameters.keys():
            f.write('{:32} {:64}'.format(el,str(parameters[el])).rstrip()+'\n')


if __name__=='__main__':
    main()
