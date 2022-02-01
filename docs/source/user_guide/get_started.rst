===============
Getting started
===============

This page should contain a short guide on what the plugin does and
a short example on how to use the plugin.

Installation
++++++++++++

Use the following commands to install the plugin::

    git clone https://github.com/lucabanetta/aiida-seigrowth .
    cd aiida-seigrowth
    pip install -e .  # also installs aiida, if missing (but not postgres)
    #pip install -e .[pre-commit,testing] # install extras for more features
    verdi quicksetup  # better to set up a new profile
    verdi calculation plugins  # should now show your calclulation plugins

Then use ``verdi code setup`` with the ``seigrowth`` input plugin
to set up an AiiDA code for aiida-seigrowth.

Usage
+++++

A quick demo of how to submit a calculation::

    verdi daemon start         # make sure the daemon is running
    cd examples
    verdi run test_submit.py        # submit test calculation
    verdi calculation list -a  # check status of calculation

If you have already set up your own aiida_seigrowth code using
``verdi code setup``, you may want to try the following command::

    seigrowth-submit  # uses aiida_seigrowth.cli

Available calculations
++++++++++++++++++++++

.. aiida-calcjob:: DiffCalculation
    :module: aiida_seigrowth.calculations
