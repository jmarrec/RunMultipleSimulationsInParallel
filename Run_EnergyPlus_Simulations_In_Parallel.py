#!/usr/bin/env python
# coding: utf-8

# Description: RunMultipleSimulationsInParallel
# Author: Julien Marrec of EffiBEM <contact@effibem.com>
# Website: www.effibem.com
# Github: https://github.com/jmarrec/RunMultipleSimulationsInParallel

import os
import multiprocessing
import shlex
import subprocess
import glob as gb
from itertools import product

# Optional: `pip install tqdm` => print a progress bar
import tqdm

ROOT_DIR = '.'
OUT_DIR = os.path.join(ROOT_DIR, 'Simulations')
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

def run_single_simulation(args):
    """
    Gets a tuple of arguments, eg: (file1.idf, weather.epw)
    """
    idf_path = os.path.relpath(args[0], ROOT_DIR)
    epw_path = os.path.relpath(args[1], ROOT_DIR)

    idf, idf_ext = os.path.splitext(idf_path)
    epw, epw_ext = os.path.splitext(epw_path)


    out_dir = os.path.join(OUT_DIR, "{}_-_{}".format(idf, epw))

    # Make a subdirectory
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)


    cmd = f"energyplus -w {epw_path} -d {out_dir} {idf_path}"
    res = subprocess.run(shlex.split(cmd), capture_output=True)
    if res.returncode != 0:
        print("Simulation failed for {idf_path} / {epw_path}")
        print(res.stdout.decode())
        print(res.stderr.decode())
        print("\n\n")


if __name__ == "__main__":

    idfs = gb.glob(os.path.join(ROOT_DIR, '*.idf'))

    epws = gb.glob(os.path.join(ROOT_DIR, '*.epw'))

    # Defaults to run on all threads
    N = multiprocessing.cpu_count()
    # You can override it to run only on a few threads
    # N = 4
    print(f"Running with {N} threads")

    all_cases = list(product(idfs, epws))

    print(f"There are {len(all_cases)} simulations to run.\n")

    with multiprocessing.Pool(processes=N) as pool:
        for _ in tqdm.tqdm(pool.imap_unordered(run_single_simulation,
                                               all_cases),
                           total=len(all_cases)):
            pass


    print("Finished!")

