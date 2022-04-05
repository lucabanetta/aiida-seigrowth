===============
Getting started
===============

This page should contain a short guide on what the plugin does and
a short example on how to use the plugin.

Setup the external code *pb.py*
++++++++++++++++++++++++
Follow the instructions:
    Download the *ExternalCode* folder
    Load *pb.py* by modifying the provided *code.yml*:
        ```
        label: "seigrowthPBM" \\
        description:  "python script which models SEI growth by population balance modeling."
        input_plugin: "seigrowth.pbe"
        on_computer: true
        remote_abs_path: "/absolute/path/to/pb.py"
        computer: "<yourcomputer>"
        prepend_text: " "
        append_text: " "
        ```
    Include the code by using
    ```
    verdi code setup --config code.yml
    ```

Installation
++++++++++++

Use the following commands to install the plugin:

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
