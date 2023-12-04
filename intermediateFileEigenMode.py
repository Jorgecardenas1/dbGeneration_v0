import ScriptEnv
import sys
import os
sys.path.insert(0, './src/')
from dbuilder.modules import hfss 
oDesktop.RestoreWindow()
oDesktop.OpenProject("C:\\Users\\jorge\\Documents\\Projects Jorge C\\Glide_Symmetry\\Designs\\glideSymmetrySweep.aedt")
oProject = oDesktop.SetActiveProject("glideSymmetrySweep")
hfss.setVariable(oProject,"sep_factor ","1.0","GlideSymmetryV3")
oDesign = oProject.SetActiveDesign("GlideSymmetryV3")
oDesign.AnalyzeAll()
hfss.createEigenReport(oProject,"C:\Users\jorge\Documents\Projects Jorge C\Glide_Symmetry\Designs\Exports","_2_2","GlideSymmetryV3","78c1364a-9266-11ee-b749-a4c3f0508c4a","Eigen Modes Plot 1")
