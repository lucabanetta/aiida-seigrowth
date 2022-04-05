[![Build Status][ci-badge]][ci-link]
[![Coverage Status][cov-badge]][cov-link]
[![Docs status][docs-badge]][docs-link]
[![PyPI version][pypi-badge]][pypi-link]

# aiida-seigrowth

 A plugin to a python script which describes the growth of the Solid Electrolyte Interface o a polydisperse graphitic electrode by using population balance modeling.
 As input data, it receives:
* ['Trajectory.pkl']: trajectory file obtained from p2d simulations conducted by using pybamm;
* ['Initial SEI Distribution']: an initial SEI thickness distribution for all the anodid coordinates;
* ['Parameters']: crucial phyisicochemical parameters;
 
 It provides with two categories of results
* ['Distributions']: it contains a series of files filedistr_j_k, which represent the SEI thickness distribution at the j-th location at time k
* ['Outputs']: it contains a series of files result_pb_k, which represent the average SEI thickness at every anodic location at time k.

## Repository contents

* [`.github/`](.github/): [Github Actions](https://github.com/lucabanetta/aiida-seigrowth) configuration
  * [`ci.yml`](.github/workflows/ci.yml): runs tests, checks test coverage and builds documentation at every new commit
  * [`publish-on-pypi.yml`](.github/workflows/publish-on-pypi.yml): automatically deploy git tags to PyPI - just generate a [PyPI API token](https://pypi.org/help/#apitoken) for your PyPI account and add it to the `pypi_token` secret of your github repository
* [`aiida_seigrowth/`](aiida_seigrowth/): The main source code of the plugin package
  * [`calculations.py`](aiida_seigrowth/calculations.py): A new `PbeSeiCalculation` `CalcJob` class
* [`docs/`](docs/): A documentation template ready for publication on [Read the Docs](http://aiida-diff.readthedocs.io/en/latest/)
* [`examples/`](examples/): An example of how to submit a calculation using this plugin
* [`.gitignore`](.gitignore): Telling git which files to ignore
* [`.pre-commit-config.yaml`](.pre-commit-config.yaml): Configuration of [pre-commit hooks](https://pre-commit.com/) that sanitize coding style and check for syntax errors. Enable via `pip install -e .[pre-commit] && pre-commit install`
* [`.readthedocs.yml`](.readthedocs.yml): Configuration of documentation build for [Read the Docs](https://readthedocs.org/)
* [`LICENSE`](LICENSE): License for your plugin
* [`README.md`](README.md): This file
* [`conftest.py`](conftest.py): Configuration of fixtures for [pytest](https://docs.pytest.org/en/latest/)
* [`pyproject.toml`](setup.json): Python package metadata for registration on [PyPI](https://pypi.org/) and the [AiiDA plugin registry](https://aiidateam.github.io/aiida-registry/) (including entry points)

## Installation

 * Before proceeding with the installation make sure that you have the right version of Pybamm installed correctly using the developer version following the istructions at the following link:
```
https://pybamm.readthedocs.io/en/latest/install/install-from-source.html#
```
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
```shell
pip install aiida-seigrowth==0.1.0
reentry scan
verdi plugin list aiida.calculations  # should now show seigrowth.pbe under the list of aiida.calculations
```
## Usage

Here goes a complete example of how to submit a test calculation using this plugin.

A quick demo of how to submit a calculation:

* Activate the pybamm environment 
```
$ source /absoulte/path/to/PyBaMM/.tox/dev/bin/activate
```
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
