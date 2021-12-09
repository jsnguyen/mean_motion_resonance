#!/bin/bash

PREPATH=$(eval echo ~$USER)
MMRDIR="${PREPATH}/landing/code/mean_motion_resonance"
FARGODIR="${PREPATH}/landing/programs/fargo3d"

cd ${MMRDIR}

echo "Copying \"visctensor_cyl.c\" to ${FARGODIR}/src/..."
cp visctensor_cyl.c "${FARGODIR}/src/"

echo "Generating par file..."
python3 generate_par.py

echo "Copying mmr/ to setups..."
cp -r mmr "${FARGODIR}/setups"

echo "Copying mmr.cfg to planets..."
cp mmr.cfg "${FARGODIR}/planets"

cd ${FARGODIR}

make clean

make SETUP=mmr RESCALE=0 UNITS=0 PARALLEL=1
