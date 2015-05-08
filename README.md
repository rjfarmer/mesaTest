# mesaTest
Downloads, builds and tests MESA (star)

Requires python (2.7 or 3)
No other packages are needed

Run:
chmod u+x /path/to/folder/main.py
/path/to/folder/main.py

Currently parameters are hardcoded in main.py
Set the following
## Test suite problems to run
cfg.test_names=['0.001M_tau1_atm','15M_dynamo']
## List of MESA versions to run (must be strings)
cfg.version_list=["7518","7525"]
## Ouput file to store results
cfg.log_file='/home/rob/Desktop/mesaTest.log'
## Somewhere to build MESA
cfg.temp_fold='/media/data/mesa/temp/'

## Set SDK path and omp_num_threads
cfg.mesasdk_root='/media/data/mesa/sdk/mesasdk-20141212'
cfg.omp_num_threads='8'
