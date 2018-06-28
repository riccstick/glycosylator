import glycosylator as GL
from prody import *
import matplotlib.pyplot as plt
import numpy as np
#Reads a NAG and adds all missing atoms

#Load a Man9 molecule
myGlycosylator = GL.Glycosylator('./support/toppar_charmm/carbohydrates.rtf', './support/toppar_charmm/carbohydrates.prm')
myGlycosylator.builder.Topology.read_topology('./support/topology/DUMMY.top')
myGlycosylator.read_connectivity_topology('./support/topology/mannose.top')

myGlycosylator.load_glycoprotein('./env_4tvp.pdb')
myGlycosylator.build_glycan_topology()
writePDB('88.pdb', myGlycosylator.glycanMolecules[',G,88,'].atom_group)
#Detect clashes
dihe_parameters = myGlycosylator.builder.Parameters.parameters['DIHEDRALS']
vwd_parameters = myGlycosylator.builder.Parameters.parameters['NONBONDED']

mySampler = GL.Sampler(myGlycosylator.glycanMolecules.values(), myGlycosylator.protein, dihe_parameters, vwd_parameters)
mySampler.remove_clashes(temp =  305, n = 100)
myGlycosylator.write_glycoprotein('HIV_test.pdb')

