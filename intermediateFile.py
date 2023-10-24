import ScriptEnv
import sys
import os
sys.path.insert(0, './src/')
from dbuilder.modules import hfss 
oDesktop.RestoreWindow()
oDesktop.OpenProject("C:/Users/jorge/Documents/Projects Jorge C/DRUIDA PROJECT/POC/dbGeneration_v0/Models/testing-multioutput/meta-atom_05_datageneration.aedt")
oProject = oDesktop.SetActiveProject("meta-atom_05_datageneration")
hfss.setVariable(oProject,"radio ","0.8mm","HFSSDesign1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("OutputVariable")
oModule.CreateOutputVariable("ReflectanceTE","(mag(S(FloquetPort1:1,FloquetPort1:1)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule.CreateOutputVariable("ReflectanceTM","(mag(S(FloquetPort1:2,FloquetPort1:2)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0_0","HFSSDesign1","anbshkd99384m","ReflectanceTE")
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0_0","HFSSDesign1","anbshkd99384m","ReflectanceTM")
