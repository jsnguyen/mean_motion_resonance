import argparse

import numpy as np
import matplotlib.pyplot as plt

def read_parameters_from_file(input_filename):
    parameters = {}
    with open(input_filename, 'r') as f:
        parameters['period_ratios'] = f.readline().strip().split()[1:]
        parameters['mass_ratios'] = f.readline().strip().split()[1:]
        parameters['n_samples'] = f.readline().strip().split()[1:]
        parameters['a_range'] = f.readline().strip().split()[1:]
        parameters['e_range'] = f.readline().strip().split()[1:]

    for key in parameters.keys():

        if key == 'period_ratios':
            parameters[key] = [int(el) for el in parameters[key]]
        elif key == 'n_samples':
            parameters[key] = int(parameters[key][0])
        else:
            parameters[key] = [float(el) for el in parameters[key]]

    return parameters

def plot_im_megno(im_megnos, parameters, run_name):

    fig = plt.figure(figsize=(7,5))
    ax = plt.subplot(111)

    extent = [parameters['a_range'][0],
              parameters['a_range'][1],
              parameters['e_range'][0],
              parameters['e_range'][1]]

    print(parameters)
    ax.set_xlim(extent[0],extent[1])
    ax.set_ylim(extent[2],extent[3])

    ax.set_xlabel('Semi-Major Axis, $a$ [AU]')
    ax.set_ylabel('Eccentricity, $e$')
    im = ax.imshow(im_megnos, interpolation='none', vmin=1.9, vmax=4, cmap='RdYlGn_r', origin='lower', aspect='auto', extent=extent)
    cb = plt.colorbar(im, ax=ax)
    cb.set_label('MEGNO')
    
    plt.savefig('megno_{}.pdf'.format(run_name), bbox_inches='tight')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('run_name', type=str)

    args = parser.parse_args()

    input_filename = 'mmr_megno_parameters_{}.txt'.format(args.run_name)
    input_im_megnos_filename = 'im_megnos_{}.npy'.format(args.run_name)

    parameters = read_parameters_from_file(input_filename)
    im_megnos = np.load(input_im_megnos_filename)

    plot_im_megno(im_megnos, parameters, args.run_name)

if __name__=='__main__':
    main()
