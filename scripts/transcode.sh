#!/usr/bin/env bash

# Where the ISOs live
SOURCE="/mnt/Big/Grandpa/Originals/iso"

# Where they'll be mounted
TARGET="/mnt/grandpa"

set -e

# Mount all of the isos
for i in 00 01 02 03 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39; do
  sudo mkdir -p ${TARGET}/${i}
  sudo mount ${SOURCE}/${i}.iso -o loop ${TARGET}/${i}/
done

# Run ffmpeg in parallel
./parallelise.py
