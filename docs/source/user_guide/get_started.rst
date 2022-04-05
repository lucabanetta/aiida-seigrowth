===============
Getting started
===============

This page should contain a short guide on what the plugin does and
a short example on how to use the plugin.

Setup the external code *pb.py*
++++++++++++++++++++++++
	- Download the *ExternalCode* folder.

	- Load *pb.py* by modifying the entries of the provided *code.yml* by inserting the absolute path to *pb.py* and the name of the computer platform:

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

Installation
++++++++++++

Use the following commands to install the plugin:
	.. code-block:: console
	
 	$ Database engine: postgresql_psycopg2
   	$ Database host: localhost
   	$ Database port: 5432
   	$ AiiDA Database name: aiidadb
   	$ AiiDA Database user: aiida
  	$ AiiDA Database password: <password>
	pip install aiida-seigrowth==0.1.0
    	verdi quicksetup  # better to set up a new profile
    	reentry scan
	verdi calculation plugins  # should now show your calclulation plugins

Usage
+++++

A quick demo of how to submit a calculation:

    cd examples
    verdi run launch.py        # submit test calculation
    verdi calculation list -a  # check status of calculation

Available calculations
++++++++++++++++++++++

.. aiida-calcjob:: PbeSeiCalculation
    :module: aiida_seigrowth.calculations
