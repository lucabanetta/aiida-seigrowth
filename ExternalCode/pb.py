#!/usr/bin/env python3

###################### pbsei ###################################################################
# pbsei solves a population balance equation for the growth a solid electrolyte interphase (SEI) 
# on a population of spherical particles composing the anode of a Li-ion battery. ##############
 
import numpy as np
import pybamm
import os
import scipy

###################### Load solution data of a charging cycle from Pybamm ###################### 
solfil='/home/lbanetta/Desktop/BIGMAP/AiiDa/PBE_Plugin/V0.0.2_Test/InputData/Trajectory.pkl'
sim=pybamm.load(solfil)
eta_sei=sim.solution["SEI film overpotential [V]"].entries
neg_electrolyte_pot=sim.solution["Negative electrolyte potential [V]"].entries
neg_electrode_pot=sim.solution["Negative electrode potential [V]"].entries
inter_curr_dens=sim.solution["Negative electrode interfacial current density [A.m-2]"].entries
x_n=sim.solution["x_n [m]"].entries
nlayer = len(x_n)
time_P2D=sim.solution["Time [h]"].entries ; time = time_P2D*3600
				
###################Set input parameters from file parameters.dat ########################################
parameters = {}	
with open("/home/lbanetta/Desktop/BIGMAP/AiiDa/PBE_Plugin/V0.0.2_Test/InputData/parameters.dat") as inputParameters:
	for line in inputParameters:
		par, value = line.partition("=")[::2]
		parameters[par.strip()] = float(value)
            
################### Assign input parameters from dictionary ########################################
Usei    = parameters['Usei']
resist  = parameters['resist']
ksei    = parameters['ksei']
MW      = parameters['MW']
rho     = parameters['rho'] 
##################### Constants ################################################################
F       = parameters['F'] 
alpha   = parameters['alpha']  
R       = parameters['R'] 
T       = parameters['T']   
i0      = parameters['i0']  
ncycles = int(parameters['ncycles'])

nclass = -1 # remove the title from the evaluation of nclass
for ilayer in range(nlayer):
    with open('/home/lbanetta/Desktop/BIGMAP/AiiDa/PBE_Plugin/V0.0.2_Test/InputData/InitialSEIDistribution.dat','r') as firstfile, open('/home/lbanetta/Desktop/BIGMAP/AiiDa/PBE_Plugin/V0.0.2_Test/Distributions/fildistr'+str(ilayer)+'_0.dat','w') as secondfile:
        for line in firstfile:
            secondfile.write(line)
            if ilayer == 1:
            	nclass += 1       
            	   	
print(nclass)           

for a in range(1, ncycles):
#################### Initialize array to store sei thickness data ##############################
	sei=np.zeros(nlayer) #length=no of layer (internal coordinate: SEI thickness)
	sei_prev=np.zeros(nlayer)
################################################################################################

################### Create file for reporting results ##########################################
	resfile='/home/lbanetta/Desktop/BIGMAP/AiiDa/PBE_Plugin/V0.0.2_Test/Outputs/result_pb'+str(a)+'.dat'
	final_output = open(resfile, "w")
	final_output.write('x coord [m]   mean SEI prv[m]    mean SEI [m]\n')
################################################################################################

##### x is the internal variable of the population (i.e. SEI thickness) ########################
	my_dict_x = {}
#### y is the fraction of particle with a certain SEI thickness ################################
	my_dict_y = {}
	#### eta is the overpotential, different for each particle class ###############################
	my_dict_eta = {}
################################################################################################

################## Read initial (or temporary SEI distribution) ################################
	for ilayer in range(nlayer):  ##ilayer: counter referred to the location expressed as distance from anodic current collector
		infil='/home/lbanetta/Desktop/BIGMAP/AiiDa/PBE_Plugin/V0.0.2_Test/Distributions/fildistr'+str(ilayer)+'_'+str(a-1)+'.dat'
		SEI_thickness=np.zeros(nclass)
		thickness_number_fraction=np.zeros(nclass)
		overpot=np.zeros(shape=(nclass,len(time)))
		filedistr = open(infil, "r")
		header=filedistr.readline()
		for iclasse in range(nclass): #iclasse: counter referred to the size of the SEI
			line=filedistr.readline()
			floats = [float(x) for x in line.split()]
			SEI_thickness[iclasse]=floats[0]
			thickness_number_fraction[iclasse]=floats[1]
		################## define overpotential for each class for every time #################################
			overpot[iclasse,:] = neg_electrode_pot[ilayer,:]-neg_electrolyte_pot[ilayer,:]- parameters['Usei'] -(inter_curr_dens[ilayer,:]*SEI_thickness[iclasse]/parameters['resist'])
		varname='layer'+str(ilayer)
		my_dict_x[varname] = SEI_thickness
		my_dict_y[varname] = thickness_number_fraction
		my_dict_eta[varname] = overpot
		filedistr.close()
################################################################################################

##### Store SEI_thickness, thickness_number_fraction and sei overpotential data in two matrices and one array###############################

	x=np.matrix([my_dict_x['layer0'], my_dict_x['layer1'],my_dict_x['layer2']
	,my_dict_x['layer3'],my_dict_x['layer4'],my_dict_x['layer5']
	,my_dict_x['layer6'],my_dict_x['layer7'],my_dict_x['layer8']
	,my_dict_x['layer9'],my_dict_x['layer10'],my_dict_x['layer11']
	,my_dict_x['layer12'],my_dict_x['layer13'],my_dict_x['layer14']
	,my_dict_x['layer15'],my_dict_x['layer16'],my_dict_x['layer17']
	,my_dict_x['layer18'],my_dict_x['layer19']])


	y=np.matrix([my_dict_y['layer0'],my_dict_y['layer1'],my_dict_y['layer2']
	 ,my_dict_y['layer3'],my_dict_y['layer4'],my_dict_y['layer5']
	 ,my_dict_y['layer6'],my_dict_y['layer7'],my_dict_y['layer8']
	 ,my_dict_y['layer9'],my_dict_y['layer10'],my_dict_y['layer11']
	 ,my_dict_y['layer12'],my_dict_y['layer13'],my_dict_y['layer14']
	 ,my_dict_y['layer15'],my_dict_y['layer16'],my_dict_y['layer17']
	 ,my_dict_y['layer18'],my_dict_y['layer19']])


	eta_sei_single=np.array([my_dict_eta['layer0'],my_dict_eta['layer1'],my_dict_eta['layer2']
	 ,my_dict_eta['layer3'],my_dict_eta['layer4'],my_dict_eta['layer5']
	 ,my_dict_eta['layer6'],my_dict_eta['layer7'],my_dict_eta['layer8']
	 ,my_dict_eta['layer9'],my_dict_eta['layer10'],my_dict_eta['layer11']
	 ,my_dict_eta['layer12'],my_dict_eta['layer13'],my_dict_eta['layer14']
	 ,my_dict_eta['layer15'],my_dict_eta['layer16'],my_dict_eta['layer17']
	 ,my_dict_eta['layer18'],my_dict_eta['layer19']])

	x=np.transpose(x)
	y=np.transpose(y)
#######################################################################################################

	for ilayer in range(nlayer): 
	### initialize the rhs ########################################################################
		rate=np.zeros(nclass)
	### extract x and y nodes for each layer ######################################################
		x_layer=np.zeros(nclass)
		y_layer=np.zeros(nclass)


		for iclasse in range(0, nclass):
			x_layer[iclasse]=x[iclasse,ilayer]
			y_layer[iclasse]=y[iclasse,ilayer]


	 ####### define the rhs for each SEI thickness (iclasse) at every coordinate x[m] #######################################
		nfuncs = []
		for iclasse in range(0,int(nclass)):
			Jsei=- parameters['i0'] / parameters['F'] * np.exp(- parameters['F'] * eta_sei_single[ilayer,iclasse,:] * parameters['alpha'] / parameters['R']/parameters['T'])
			G=-Jsei*parameters['MW']/parameters['rho']  #growth for each layer and each particle size as a function of time
			nfunc = scipy.interpolate.interp1d(time,G,bounds_error=False, fill_value="extrapolate")
			nfuncs.append(nfunc) 

		def RHS(x_layer,time,nclass,nfuncs):
			for iclasse in range(0,int(nclass)):
				nfunc_single = nfuncs[iclasse]
				rate[iclasse] = nfunc_single(time)
			return rate

	########## Solve the set of ode's ##############################################################
		sol = scipy.integrate.odeint(RHS, x_layer, time,args=(nclass,nfuncs))
	################################################################################################
	##updates the SEI distribution at location X
		time_index=-1
		outfil='/home/lbanetta/Desktop/BIGMAP/AiiDa/PBE_Plugin/V0.0.2_Test/Distributions/fildistr'+str(ilayer)+'_'+str(a)+'.dat'
		file2 = open(outfil, "w")
		file2.write('SEI [m]   frc [-]   \n')
		for iclasse in range(nclass):
			file2.write(("%.5e   %.5e \n") %(sol[-1,iclasse],y_layer[iclasse]))
		file2.close()
	# initial and final average sei layer thickness
		sei_prev[ilayer]=np.dot(x_layer,y_layer)
		sei[ilayer]=np.dot(sol[time_index,:],y_layer)

	###write solution
		final_output.write(("%.5e   %.8e    %.8e\n") %(x_n[ilayer,-1], sei_prev[ilayer], sei[ilayer]))

	final_output.close()
	 ### report solution
