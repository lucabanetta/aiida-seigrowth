"""
Calculations provided by aiida_seigrowth.

Register calculations via the "aiida.calculations" entry point in setup.json.
"""
from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import SinglefileData,Dict,Int


class PbeSeiCalculation(CalcJob):
    """
    AiiDA calculation plugin wrapping the python3.8 script executable pb.py.

    Simple AiiDA plugin wrapper to compute SEI growth by using population balance modeling
    """

    @classmethod
    def define(cls, spec):
    	super().define(spec)
    	spec.input("parameters", valid_type=SinglefileData, help="Parametri chimico/fisici per la crescita del SEI")
    	spec.input("nlayers", valid_type =Int, help = "numero di coordinate anodiche" )
    	spec.input("InitialSeiDistribution", valid_type=SinglefileData, help ="Distribuzione iniziale del SEI")
    	spec.input("PybammData", valid_type = SinglefileData, help = "FIle .pkl prodotto dalla simulazione pybamm")
    	# spec.inputs['metadata']['options']['parser_name'].default = 'seigrowth.pbe'
    	spec.inputs['metadata']['options']['resources'].default = {'num_machines': 1, 'num_mpiprocs_per_machine': 1}

    def prepare_for_submission(self, folder):
    
    # prepare the file distributions fildistr<ilayer>_0.dat from InitialSEIDistribution.dat in the folder Distributions
        for ilayer in range(self.inputs.nlayers.value):
            with open('InputData/InitialSEIDistribution.dat','r') as firstfile, open('Distributions/fildistr'+str(ilayer)+'_0.dat','w') as secondfile:
                for line in firstfile:
                    secondfile.write(line)
				
        codeinfo = datastructures.CodeInfo()
        codeinfo.code_uuid = self.inputs.code.uuid

        calcinfo = datastructures.CalcInfo()
        calcinfo.codes_info = [codeinfo]
        return calcinfo
