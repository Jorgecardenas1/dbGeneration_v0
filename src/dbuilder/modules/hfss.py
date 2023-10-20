# -*- coding: utf-8 -*-
"""
@author: Jorge Cardenas
"""



def agregaVariable(proj,nombre,valor):
        oDesign = proj.SetActiveDesign(nombre_diseno)
        oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:NewProps",
    				[
    					"NAME:" + nombre,
    					"PropType:="		, "VariableProp",
    					"UserDef:="		, True,
    					"Value:="		, valor
    				]
    			]
    		]
    	])
    

def modificaVariable(proj,nombre,valor):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:ChangedProps",
    				[
    					"NAME:"+ nombre ,
    					"Value:="		, valor
    				]
    			]
    		]
    	])

    
def agregaArreglo(proj,nombre,valor):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:NewProps",
    				[
    					"NAME:" + nombre,
    					"PropType:="		, "VariableProp",
    					"UserDef:="		, True,
    					"Value:="		, valor
    				]
    			]
    		]
    	])

# modifica un arreglo del proyecto proj
# nombre y valor son strings
    
def setVariable(proj,name,value, design):
    oDesign = proj.SetActiveDesign(design)
    oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:ChangedProps",
    				[
    					"NAME:"+ name,
    					"Value:="		, value
    				]
    			]
    		]
    	])

    
#UNDERNEATH THE COMMANDS TO GENERATE THE S PARAMETERS ARE PRESENTED.
    
#Creating the S11 data
def createResult(proj,path,name,design,simID, resultName):

    oDesign = proj.SetActiveDesign(design)
    oModule = oDesign.GetModule("ReportSetup")
    oModule.CreateReport(resultName, "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
    	[
    		"Domain:="		, "Sweep"
    	], 
    	[
    		"Freq:="		, ["All"],
    	], 
    	[
    		"X Component:="		, "Freq",
    		"Y Component:="		, [resultName]
    	], [])

    oModule.ExportToFile(resultName, path+"/output/"+str(simID)+"/files/"+str(resultName)+str(name)+".csv")

