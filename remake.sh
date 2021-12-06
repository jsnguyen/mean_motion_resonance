#!/bin/bash

PREPATH=$(eval echo ~$USER)
FARGODIR="${PREPATH}/landing/programs/fargo3d"

cd ${FARGODIR}

make SETUP=mmr RESCALE=0 UNITS=0 PARALLEL=1
