# RunMultipleSimulationsInParallel

A simple way to run several IDFs against several EPWs via Python

Uses only standard python library, except [tqdm](https://github.com/tqdm/tqdm) (`pip install tqdm`) but easy to not use it. tqdm is great to make a progress bar, which is nice.

Written with `f-strings`, so Python >= 3.6


Sawn together very quickly to answer this [UnmetHours](https://unmethours.com/question/49584/how-to-run-models-with-many-different-weather-files-and-set-output-excel-name-accordingly/) question, so take it or leave it.

There is a jupyter notebook and the exact same code as a regular .py file.

Place your IDF / EPW into the root folder. It will run the simulations of each IDF against each EPW in parallel, and output to the `Simulations/{idf_name}_-_{epw_name}` folder.
You should customize the number of simulations to be run in parallel, it defaults to `multiprocessing.cpu_count()`. You probably DO want to set it to the number of physical cores, not threads.

example usage:

```shell
$ python Run_EnergyPlus_Simulations_In_Parallel.py

Running with 16 threads
There are 6 simulations to run.

100%|█████████████████████████████████████████████| 6/6 [00:01<00:00,  3.65it/s]
Finished!


$ ls Simulations/
1ZoneUncontrolled3SurfaceZone_-_USA_CA_San.Francisco.Intl.AP.724940_TMY3
1ZoneUncontrolled3SurfaceZone_-_USA_CO_Golden-NREL.724666_TMY3
1ZoneUncontrolled3SurfaceZone_-_USA_IL_Chicago-OHare.Intl.AP.725300_TMY3
1ZoneUncontrolled_-_USA_CA_San.Francisco.Intl.AP.724940_TMY3
1ZoneUncontrolled_-_USA_CO_Golden-NREL.724666_TMY3
1ZoneUncontrolled_-_USA_IL_Chicago-OHare.Intl.AP.725300_TMY3
```

------------

Author: Julien Marrec of [EffiBEM](www.effibem.com)
