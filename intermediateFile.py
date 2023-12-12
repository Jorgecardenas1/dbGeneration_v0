import ScriptEnv
import sys
import os
sys.path.insert(0, './src/')
from dbuilder.modules import hfss 
oDesktop.RestoreWindow()
oDesktop.OpenProject("C:\\Users\\jorge\\Documents\\Projects Jorge C\\DRUIDA PROJECT\\POC\\dbGeneration_v0\\Models\\testing-multioutput\\meta-atom_box_01_datageneration.aedt")
oProject = oDesktop.SetActiveProject("meta-atom_box_01_datageneration")
hfss.setVariable(oProject,"parameters ","[3.1904937273524077, 3.8835954049098405, 0.5349188858804177, 1.3262243019997793]mm","HFSSDesign1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("OutputVariable")
oModule.CreateOutputVariable("ReflectanceTE","(mag(S(FloquetPort1:1,FloquetPort1:1)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule.CreateOutputVariable("ReflectanceTM","(mag(S(FloquetPort1:2,FloquetPort1:2)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule.CreateOutputVariable("TransmittanceTE","(mag(S(FloquetPort2:1,FloquetPort2:1)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule.CreateOutputVariable("TransmittanceTM","(mag(S(FloquetPort2:2,FloquetPort2:2)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule.CreateOutputVariable("AbsorbanceTE","1-((mag(S(FloquetPort1:1,FloquetPort1:1)))^2 +(mag(S(FloquetPort2:1,FloquetPort1:1)))^2)", "Setup1 : Sweep", "Modal Solution Data", [])
oModule.CreateOutputVariable("AbsorbanceTM","1-((mag(S(FloquetPort1:2,FloquetPort1:2)))^2 +(mag(S(FloquetPort2:2,FloquetPort1:2)))^2)", "Setup1 : Sweep", "Modal Solution Data", [])
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0-0","HFSSDesign1","0d9059e5-9940-11ee-9279-a4c3f0508c4a","ReflectanceTE")
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0-0","HFSSDesign1","0d9059e5-9940-11ee-9279-a4c3f0508c4a","ReflectanceTM")
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0-0","HFSSDesign1","0d9059e5-9940-11ee-9279-a4c3f0508c4a","TransmittanceTE")
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0-0","HFSSDesign1","0d9059e5-9940-11ee-9279-a4c3f0508c4a","TransmittanceTM")
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0-0","HFSSDesign1","0d9059e5-9940-11ee-9279-a4c3f0508c4a","AbsorbanceTE")
hfss.createResult(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Exports","_0-0","HFSSDesign1","0d9059e5-9940-11ee-9279-a4c3f0508c4a","AbsorbanceTM")
hfss.exportImage(oProject,"C:\Users\jorge\Documents\Projects Jorge C\DRUIDA PROJECT\POC\dbGeneration_v0\Images","HFSSDesign1_0d9059e5-9940-11ee-9279-a4c3f0508c4a_0-0")
