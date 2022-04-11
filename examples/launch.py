from aiida import orm
from aiida.engine import run
from aiida.common.exceptions import NotExistent

import os

# Setting up inputs
computer = orm.load_computer('testpbe')
code = load_code('seigrowthPBM@testpbe')
path = os.getcwd()
builder = code.get_builder()
builder.parameters = orm.SinglefileData(file = path + '/InputData/parameters.txt') 
builder.InitialSeiDistribution = orm.SinglefileData(file= path + '/InputData/InitialSEIDistribution.txt')
builder.PybammData = orm.SinglefileData(file= path +'/InputData/Trajectory.pkl')

builder.metadata.options.withmpi = False
builder.metadata.options.resources = {
    'num_machines': 1,
    'num_mpiprocs_per_machine': 1,
}

# Running the calculation & parsing results
run(builder)

print("Test completed.")
