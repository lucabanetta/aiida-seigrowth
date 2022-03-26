"""
Calculations provided by aiida_seigrowth.

Register calculations via the "aiida.calculations" entry point in setup.py.
"""
from aiida.common.datastructures import CalcInfo, CodeInfo
from aiida.engine import CalcJob
from aiida.orm import SinglefileData, Str, FolderData


class PbeSeiCalculation(CalcJob):
    """
    AiiDA calculation plugin wrapping the python3.8 script executable pb.py.

    Simple AiiDA plugin wrapper to compute SEI growth by using population balance modeling
    """

    @classmethod
    def define(cls, spec):
    	super().define(spec)
    	
    	spec.input("parameters", valid_type=SinglefileData, help="Parametri chimico/fisici per la crescita del SEI")
    	spec.input("InitialSeiDistribution", valid_type=SinglefileData, help ="Distribuzione iniziale del SEI")
    	spec.input("PybammData", valid_type = SinglefileData, help = "File .pkl prodotto dalla simulazione pybamm")
    	
    	spec.output("Distributions", valid_type = FolderData, help = 'Distribuzione del SEI ad ogni coordinata ')
    	spec.output("Outputs", valid_type = FolderData, help = "Valori medi del SEI ad ogni timestep e ad ogni coordinata anodica")
    	
    	spec.inputs['metadata']['options']['resources'].default = {'num_machines': 1, 'num_mpiprocs_per_machine': 1}

    def prepare_for_submission(self, folder) -> CalcInfo:
				
        codeinfo = CodeInfo()
        codeinfo.code_uuid = self.inputs.code.uuid
        
        calcinfo = CalcInfo()
        
        calcinfo.local_copy_list = [(self.inputs.parameters.uuid, self.inputs.parameters.filename, 'parameters.txt'),
                                    (self.inputs.InitialSeiDistribution.uuid, self.inputs.InitialSeiDistribution.filename, 'InitialSEIDistribution.txt'), 
                                    (self.inputs.PybammData.uuid, self.inputs.PybammData.filename, 'Trajectory.pkl')
                                   ]
        
        calcinfo.retrieve_list = ['Distributions',
                                  'Outputs'
                                 ]
                
        calcinfo.codes_info = [codeinfo]
        return calcinfo
