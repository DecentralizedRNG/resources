# Resources

This repository contain data and experiment of dRNG (Decetranlized Random Number Generator)

## Requirement

You need to prepare environment to execute expriment and/or simulator:

* *Python 2.7.x*
* *python-dev* or *python-devel*, this package are require to build *pysha3*
* Developer environment *(GCC/G++/Cmake...)* this is require for GNU/Linux
* *pip* Python package manager
* *matplotlib 2.0.1* is required to draw plots
* *pysha3 1.0.2* is required by Flexible Proof-of-Work

## Clean cache & execute experiment

Clearn cache

```bash
~$ rm -rf ./data/*.data && rm -rf ./plot/*.svg
```

Generate new data set

```bash
~$ python newSimulator.py
```
Result (it may take time to be done).
```data
Start experiment from e=44 to e=84
[DONE] Experiment e = 44 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 45 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 46 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 47 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 48 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 49 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 50 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 51 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 52 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 53 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 54 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 55 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 56 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 57 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 58 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 59 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 60 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 61 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 62 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 63 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 64 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 65 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 66 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 67 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 68 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 69 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 70 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 71 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 72 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 73 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 74 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 75 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 76 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 77 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 78 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 79 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 80 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 81 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 82 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 83 Era timeout = 1200 Samples = 1000 Solution= 1000  Threads = 24
Start experiment from e=44 to e=84
[DONE] Experiment e = 44 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 45 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 46 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 47 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 48 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 49 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 50 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 51 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 52 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 53 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 54 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 55 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 56 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 57 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 58 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 59 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 60 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 61 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 62 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 63 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 64 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 65 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 66 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 67 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 68 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 69 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 70 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 71 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 72 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 73 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 74 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 75 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 76 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 77 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 78 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 79 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 80 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 81 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 82 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
[DONE] Experiment e = 83 Era timeout = 600 Samples = 1000 Solution= 1000  Threads = 24
```
## Directories

```
├── data
├── experiment
│   └── data
│       ├── 3000100
│       ├── 3000200
│       └── 3000300
└── plot
```

**data** Cache data, remove all **.dat* if you want to generate new data set
**experiment** Old experiment result from previous
**plot** Vector plot base on conllected data

## License

This resouce distributed under [MIT License](https://github.com/DecentralizedRNG/resources/blob/master/LICENSE)