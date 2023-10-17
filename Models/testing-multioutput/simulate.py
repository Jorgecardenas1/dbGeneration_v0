# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2021.2.0
# 7:57:01  Oct 17, 2023
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("meta-atom_02_datageneration")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.AnalyzeAll()
oModule = oDesign.GetModule("OutputVariable")
oModule.CreateOutputVariable("transmittance", "(mag(S(FloquetPort2:1,FloquetPort1:1)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Output Variables Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"Xsize:="		, ["Nominal"],
		"Ysize:="		, ["Nominal"],
		"H:="			, ["Nominal"],
		"margin:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["transmittance"]
	])
oModule = oDesign.GetModule("OutputVariable")
oModule.CreateOutputVariable("transmittanceTM", "(mag(S(FloquetPort2:2,FloquetPort1:2)))^2", "Setup1 : Sweep", "Modal Solution Data", [])
oModule = oDesign.GetModule("ReportSetup")
oModule.AddTraces("Output Variables Plot 1", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"Xsize:="		, ["Nominal"],
		"Ysize:="		, ["Nominal"],
		"H:="			, ["Nominal"],
		"margin:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["transmittanceTM"]
	])
oModule.CreateReport("S Parameter Plot 1", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"Xsize:="		, ["Nominal"],
		"Ysize:="		, ["Nominal"],
		"H:="			, ["Nominal"],
		"margin:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(FloquetPort1:2,FloquetPort1:1))","dB(S(FloquetPort2:2,FloquetPort1:1))"]
	])
oModule.UpdateTraces("S Parameter Plot 1", ["dB(S(FloquetPort1:2,FloquetPort1:1))"], "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"Xsize:="		, ["Nominal"],
		"Ysize:="		, ["Nominal"],
		"H:="			, ["Nominal"],
		"margin:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(FloquetPort1:1,FloquetPort1:1))"]
	])
oModule.AddTraces("S Parameter Plot 1", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"Xsize:="		, ["Nominal"],
		"Ysize:="		, ["Nominal"],
		"H:="			, ["Nominal"],
		"margin:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(FloquetPort2:1,FloquetPort1:1))"]
	])
oModule.DeleteTraces(
	[
		"S Parameter Plot 1:="	, ["dB(S(FloquetPort2:2,FloquetPort1:1))"]
	])
oModule.CreateReport("S Parameter Plot 2", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"Xsize:="		, ["Nominal"],
		"Ysize:="		, ["Nominal"],
		"H:="			, ["Nominal"],
		"margin:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["dB(S(FloquetPort1:2,FloquetPort1:2))","dB(S(FloquetPort2:2,FloquetPort1:2))"]
	])
oModule.RenameReport("S Parameter Plot 2", "TM")
oModule.RenameReport("S Parameter Plot 1", "TE")
oModule.RenameReport("Output Variables Plot 1", "Transmittance")
oModule.ExportToFile("TE", "C:/Users/jorge/Documents/Projects Jorge C/Octubre 2023/testing-multioutput/exports/TE.csv", False)
oModule.ExportToFile("TM", "C:/Users/jorge/Documents/Projects Jorge C/Octubre 2023/testing-multioutput/exports/TM.csv", False)
oModule.ExportToFile("Transmittance", "C:/Users/jorge/Documents/Projects Jorge C/Octubre 2023/testing-multioutput/exports/Transmittance.csv", False)
oProject.Save()
oDesktop.CloseProject("meta-atom_02_datageneration")
