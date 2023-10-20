import ScriptEnv
import os
sys.path.insert(0, './src/')
from dbuilder import modules as hfss
oDesktop.RestoreWindow()
oDesktop.OpenProject("C:/Users/jorge/Documents/Projects Jorge C/DRUIDA PROJECT/POC/dbGeneration_v0/Models/testing-multioutput/meta-atom_05_datageneration.aedt")
oProject = oDesktop.SetActiveProject("meta-atom_05_datageneration")
