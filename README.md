[![Build Status][ci-badge]][ci-link]
[![Coverage Status][cov-badge]][cov-link]
[![Docs status][docs-badge]][docs-link]
[![PyPI version][pypi-badge]][pypi-link]

# aiida-seigrowth

 A plugin to an external code which models the growth of the Solid Electrolyte Interface (SEI) across a graphitic anode over a series of charge cycles by coupling a Pseudo 2-Dimensional (P2D) Doyle-Fuller-Newman Li-ion battery modemodel with a Population Balance Model (PBM).
 
The external code receives as inputs:
* ['Trajectory.pkl']: pickle format file obtained from Li-ion battery charge simulations by using the P2D Doyle-Fuller-Newman Model implemented in the open source python library PyBaMM;
* ['Initial SEI Distribution.txt']: an initial SEI thickness distribution for all the considered anodic coordinates;
* ['Parameters.txt']: the overall number of cycles and the kinetic parameters related to the SEI growth,
 
and provides with two categories of results:
* ['Distributions']: a series of filedistr_j_k.dat text files, which represent the SEI thickness distribution at the j-th location at time k
* ['Outputs']:  a series of files result_pb_k text files, which represent the average SEI thickness at every anodic location at time k.

## Repository contents
* [`ExternalCode/`](ExternalCode/): The main source code which solves the Population Balance Model
  * [`pb.py`](ExternalCode/pb.py): external code to be plugged into Aiida via aiida-seigrowth
  * [`code.yml`](ExternalCode/code.yml): to be used to configure the code into the computer Aiida is working at. 
* [`aiida_seigrowth/`](aiida_seigrowth/): The main source code of the plugin package
  * [`calculations.py`](aiida_seigrowth/calculations.py): A new `PbeSeiCalculation` `CalcJob` class
* [`docs/`](docs/): Initial documentation including a user fuide
* [`examples/`](examples/): An example of how to submit a calculation using this plugin
* [`LICENSE`](LICENSE): License for your plugin
* [`README.md`](README.md): This file
* [`pyproject.toml`](pyproject.toml): Minimum requirements for the build system to execute
* [`setup.py`](setup.py): Configuration to install the package aiida-seigrowth

## Installation
 * Before proceeding with the installation make sure that you have the right version of Pybamm installed correctly using the developer version following the istructions at the following [link](https://pybamm.readthedocs.io/en/latest/install/install-from-source.html):

 * Download the External Code folder and include the python script pb.py by modifying the script code.yml by inserting the absolute path to the script pb.py:
```
---
label: "seigrowthPBM"
description:  "python script which models SEI growth by population balance modeling."
input_plugin: "seigrowth.pbe"
on_computer: true
remote_abs_path: "/absolute/path/to/pb.py"
computer: "<yourcomputer>"
prepend_text: " "
append_text: " "
---
```

 * Include the code:
```
verdi code setup --config code.yml
```

 * Proceed to install via pip: 
```
pip install aiida-seigrowth==0.1.0
reentry scan
verdi plugin list aiida.calculations  
```
The user should now show see *seigrowth.pbe* under *aiida.calculations*
## Usage

To submit a calculation:

* Activate the PyBaMM environment 
```
$ source /absoulte/path/to/PyBaMM/.tox/dev/bin/activate
```
* Prepare a P2D simulation via PyBaMM
```shell
cd examples/Pybamm_Simulations
python Pybamm_Use_Example.py
```

* Download the examples folder, with a subfolder named InputData with the aforementioned input data and a script named launch.py

* Proceed to run launch.py for the first demo:
```
cd examples
verdi run launch.py

```
* Check the retrieved folder data and save them to a new directory
  ```
  verdi process list -a  # check record of calculation
  verdi node repo dump [RemoteDataFolderNode] /abs/path/to/new/Folder
## License

MIT
## Contact

luca.banetta@polito.it

## Acknowledgements
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 957189. The project is part of BATTERY 2030+, the large-scale European research initiative for inventing the sustainable batteries of the future.

[ci-badge]: https://github.com/lucabanetta/aiida-seigrowth/workflows/ci/badge.svg?branch=master
[ci-link]: https://github.com/lucabanetta/aiida-seigrowth/actions
[cov-badge]: https://coveralls.io/repos/github/lucabanetta/aiida-seigrowth/badge.svg?branch=master
[cov-link]: https://coveralls.io/github/lucabanetta/aiida-seigrowth?branch=master
[docs-badge]: https://readthedocs.org/projects/aiida-seigrowth/badge
[docs-link]: http://aiida-seigrowth.readthedocs.io/
[pypi-badge]: https://badge.fury.io/py/aiida-seigrowth.svg
[pypi-link]: https://badge.fury.io/py/aiida-seigrowth

