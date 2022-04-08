[![Build Status][ci-badge]][ci-link]
[![Coverage Status][cov-badge]][cov-link]
[![Docs status][docs-badge]][docs-link]
[![PyPI version][pypi-badge]][pypi-link]

# aiida-seigrowth

 A plugin to a python script which describes the growth of the Solid Electrolyte Interface on a graphitic electrode across a series of charges by coupling a Pseudo 2-Dimensional (P2D) model with a Population Balance Model (PBM).
 
The external code receives as inputs:
* ['Trajectory.pkl']: trajectory file obtained from p2d simulations conducted by using pybamm;
* ['Initial SEI Distribution']: an initial SEI thickness distribution for all the considered anodic coordinates;
* ['Parameters']: it contains the overall number of cycles and the kinetic features of the SEI growth.
 
 And it provides with two categories of results:
* ['Distributions']: it contains a series of files filedistr_j_k, which represent the SEI thickness distribution at the j-th location at time k
* ['Outputs']: it contains a series of files result_pb_k, which represent the average SEI thickness at every anodic location at time k.

## Repository contents
* [`ExternalCode/`](ExternalCode/): The main source code of the external application
  * [`pb.py`](ExternalCode/pb.py): external code to be plugged into Aiida via aiida-seigrowth
  * [`code.yml`](ExternalCode/code.yml): configuration code to be used to configure the code into Aiida  
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

```

 * Include the code by using
```
verdi code setup --config code.yml
```

 * Proceed to install the plugin 
```
pip install aiida-seigrowth==0.1.0
reentry scan
verdi plugin list aiida.calculations  
```
The user should now show see *seigrowth.pbe* under *aiida.calculations*
## Usage

Here goes a complete example of how to submit a test calculation using this plugin.

To submit a calculation:

* Activate the pybamm environment 
```
$ source /absoulte/path/to/PyBaMM/.tox/dev/bin/activate
```
* Prepare a Pybamm simulation
```shell
cd examples/Pybamm_Simulations
python Pybamm_Use_Example.py
```

* Entering the Examples folder in aiida-seigrowth, there is a subfolder named InputData with the necessary inputs and a script named launch.py

* Proceed to launch the example
```shell
cd examples
verdi run launch.py
verdi process list -a  # check record of calculation
check the retrieved folder data and save them to a new directory by using verdi node repo dump [NODES] /abs/path/to/new/Folder
```

## License

MIT
## Contact

luca.banetta@polito.it

[ci-badge]: https://github.com/lucabanetta/aiida-seigrowth/workflows/ci/badge.svg?branch=master
[ci-link]: https://github.com/lucabanetta/aiida-seigrowth/actions
[cov-badge]: https://coveralls.io/repos/github/lucabanetta/aiida-seigrowth/badge.svg?branch=master
[cov-link]: https://coveralls.io/github/lucabanetta/aiida-seigrowth?branch=master
[docs-badge]: https://readthedocs.org/projects/aiida-seigrowth/badge
[docs-link]: http://aiida-seigrowth.readthedocs.io/
[pypi-badge]: https://badge.fury.io/py/aiida-seigrowth.svg
[pypi-link]: https://badge.fury.io/py/aiida-seigrowth
