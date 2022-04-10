===============
Getting started
===============

This page contains a short guide on the installation procedures of the external code and the plugin, together with the necessary information to install PyBaMM. Finally, there is a short example on how to use the plugin.

Setup the external code *pb.py*
++++++++++++++++++++++++
    - Download the *ExternalCode* folder.

    - Load *pb.py* by modifying *code.yml*, inserting the absolute path to *pb.py* and the proper name of the computer:

        1) label: "seigrowthPBM"
	2) description:  "python script which models SEI growth by population balance modeling."
	3) input_plugin: "seigrowth.pbe"
	4) on_computer: true
	5) remote_abs_path: "/absolute/path/to/pb.py"
	6) computer: "<yourcomputer>"
	7) prepend_text: " "
	8) append_text: " "
    - Include the code: 
            .. code-block:: console 
	    verdi code setup --config code.yml
	
Setup PyBaMM
++++++++++++++++++++++++
	- Install PyBaMM in developer mode by following the instructions at `PyBaMM_Install <https://pybamm.readthedocs.io/en/latest/install/install-from-source.html>`_

Installation
++++++++++++
Quick installation guide for the plugin. Please use the following command lines:
    1) pip install aiida-seigrowth==0.1.0
    2) verdi quicksetup  # better to set up a new profile
    3) reentry scan
    4) verdi calculation plugins  # should now show your calclulation plugins

Usage
+++++
1) Activate the PyBaMM environment 
```
$ source /absoulte/path/to/PyBaMM/.tox/dev/bin/activate
```

2) To submit the demo:
   * Download examples folder
   * cd examples
   * verdi run launch.py  
   
3) Check the retrieved folder data and save them to a new directory
    * verdi process list -a  # check record of calculation
    * verdi node repo dump [RemoteDataFolderNode] /abs/path/to/new/Folder
Available calculations
++++++++++++++++++++++

.. aiida-calcjob:: PbeSeiCalculation
    :module: aiida_seigrowth.calculations
