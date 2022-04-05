###################### PBE_SEI_SETUP ###################################################################
# PBE_SEI_SETUP uses the python library pybamm to create the trajectory file used by the PBE model to describe the growth of SEI. 


import pybamm

model = pybamm.lithium_ion.DFN()
input_parameters = pybamm.ParameterValues("Marquis2019") #see Marquis et al. 

input_parameters["Initial concentration in negative electrode [mol.m-3]"] = 4500
input_parameters["Initial concentration in positive electrode [mol.m-3]"] = 48000

input_parameters["Initial inner SEI thickness [m]"] = 0.0
input_parameters["Initial outer SEI thickness [m]"] = 0.0
input_parameters["SEI kinetic rate constant [m.s-1]"] = 0.0
input_parameters["SEI reaction exchange current density [A.m-2]"] = 0.0

protocol = pybamm.Experiment(
    [
        ("Charge at C/2 until 4.1 V"),
    ]
)
setup = pybamm.Simulation(model, parameter_values = input_parameters, experiment = protocol)
setup.solve()
setup.save("Trajectory_C_2.pkl")
setup.plot()

