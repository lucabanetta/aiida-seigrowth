#!/usr/bin/env python

from __future__ import absolute_import

import json

from setuptools import find_packages, setup

if __name__ == "__main__":

    setup(
        packages=find_packages(),
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        name = 'aiida-seigrowth',
        version = "0.1.0",
        description = "AiiDA plugin to model SEI growth by population balance modeling",
        author = "Luca Banetta",
        author_email = "luca.banetta@polito.it",
        license = 'MIT License',
        classifiers = [ "Programming Language :: Python :: 3.8", "Framework :: AiiDA"],
        python_requires = ">=3.8",
        install_requires = ["aiida-core>=1.4.0,<2.0.0",
    			"importlib_resources",
    			"jsonschema ~=3.0",
    			"numpy",
    			"packaging",
    			"python-dateutil~=2.8",
   			"pybamm == 21.12"],
        reentry_register = True,
        include_package_data = True,
        entry_points = { "aiida.calculations": ["seigrowth.pbe = aiida_seigrowth.calculations:PbeSeiCalculation"]},
        extras_require = { "code_style": ["pre-commit~=2.6"],"docs": ["myst-parser~=0.15.0","sphinx-external-toc","furo"]}      
    )
