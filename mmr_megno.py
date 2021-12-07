import numpy as np
import functools

import rebound
import multiprocessing
from multiprocessing import Pool
import tqdm

def mmr_megno(orbital_parameters, period_ratios, mass_ratios, star_mass=1, n_orbits=1e4, n_avg=10):

    megnos = []
    for _ in range(n_avg):
        np.random.seed()

        a,e = orbital_parameters

        sim = rebound.Simulation()
        sim.integrator = "whfast"
        sim.ri_whfast.safe_mode = 0
        sim.dt = 2*np.pi/10

        sim.add(m=star_mass)

        for period,mass in zip(period_ratios,mass_ratios):
            sim.add(m=mass, a=a*(period**(2/3)), e=e, omega=np.random.uniform(0,2*np.pi), f=np.random.uniform(0,2*np.pi))

        n_particles = sim.N_real

        sim.move_to_com()

        sim.init_megno()
        sim.exit_max_distance = a*10
        
        try:
            sim.integrate(n_orbits*2*np.pi, exact_finish_time=0)
            megno = sim.calculate_megno()
        
        except rebound.Escape:
            megno = 10

        megnos.append(megno)
        
    return np.mean(megnos)

def write_parameters_to_file(output_filename, period_ratios, mass_ratios, n_samples, a_range, e_range):
    with open(output_filename,'w') as f:
        f.write('PERIOD_RATIOS '+' '.join([str(el) for el in period_ratios]))
        f.write('\n')
        f.write('MASS_RATIOS '+' '.join([str(el) for el in mass_ratios]))
        f.write('\n')
        f.write('N_SAMPLES '+str(n_samples))
        f.write('\n')
        f.write('A_RANGE '+' '.join([str(el) for el in a_range]))
        f.write('\n')
        f.write('E_RANGE '+' '.join([str(el) for el in e_range]))
        f.write('\n')

def main():

    ms_to_mj = 1/1000 # solar mass to jupiter mass
    period_ratios  = [1,2]
    mass_ratios = [1*ms_to_mj,1*ms_to_mj]
    n_samples = 256
    a_range = (1,100)
    e_range = (0,1-1e-6)

    output_filename = 'mmr_megno_parameters_1_2.txt'
    output_im_megnos_filename = 'im_megnos_1_2.npy'

    write_parameters_to_file(output_filename, period_ratios, mass_ratios, n_samples, a_range, e_range)

    orbital_parameters = []
    for ee in np.linspace(*e_range,n_samples):
        for ss in np.linspace(*a_range,n_samples):
            orbital_parameters.append((ss,ee))

    megnos=[]

    partial_mmr_megno = functools.partial(mmr_megno, period_ratios=period_ratios, mass_ratios=mass_ratios)

    pool = Pool(processes=64)
    results = list(tqdm.tqdm(pool.imap(partial_mmr_megno,orbital_parameters), total=len(orbital_parameters)))

    im_megnos = np.array(results).reshape(n_samples,n_samples)
    np.save(output_im_megnos_filename, im_megnos)

if __name__=='__main__':
    main()
