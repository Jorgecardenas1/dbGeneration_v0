import ScriptEnv
import sys
import os
sys.path.insert(0, './src/')
from dbuilder.modules import hfss 
oDesktop.RestoreWindow()
oDesktop.OpenProject("C:/Users/jorge/Documents/Projects Jorge C/DRUIDA PROJECT/POC/dbGeneration_v0/Models/testing-multioutput/meta-atom_box_01_datageneration.aedt")
oProject = oDesktop.SetActiveProject("meta-atom_box_01_datageneration")
hfss.setVariable(oProject,"parameters ","[3.03119075514881, 1.4924253386343338, 0.3625252610464782, 1.0883294148982352]mm","HFSSDesign1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("OutputVariable")
oModule.CreateOutputVariable("ReflectanceTE","(mag(S(FloquetPort1:1,FloquetPort1:1)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule.CreateOutputVariable("ReflectanceTM","(mag(S(FloquetPort1:2,FloquetPort1:2)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0_0","HFSSDesign1","1f9a4069-7cbb-11ee-a648-a4c3f0508c4a","ReflectanceTE")
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0_0","HFSSDesign1","1f9a4069-7cbb-11ee-a648-a4c3f0508c4a","ReflectanceTM")
