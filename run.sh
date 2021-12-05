#!/bin/bash

PREPATH=$(eval echo ~$USER)
MMRDIR="${PREPATH}/code/mean_motion_resonance"
FARGODIR="${PREPATH}/programs/fargo3d"
MMRDIR="/Users/jsn/landing/code/mean_motion_resonance"
FARGODIR="/Users/jsn/landing/programs/fargo3d"
NCPU=4

cd ${MMRDIR}

python3 generate_par.py

echo "Copying to setups..."
cp -r mmr "${FARGODIR}/setups"

echo "Copying to planets..."
cp mmr.cfg "${FARGODIR}/planets"

cd ${FARGODIR}

make SETUP=mmr RESCALE=0 UNITS=0 PARALLEL=1
mpirun -np ${NCPU} ./fargo3d setups/mmr/mmr.par
