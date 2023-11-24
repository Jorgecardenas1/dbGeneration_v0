
# -*- coding: utf-8 -*-

"""dataManagement.py
   Author: Jorge Cardenas

   1. Simulation data logging in CSV Files
   2. Simulation data Retrieval

   Future developments:
   1. Local or remote data storage
"""

import csv
import os
import pandas as pd
import os.path as path

import subprocess

class Builder:

    def __init__(self, ansysPath,modelName,projectName, designName, modelPath,exportPath):
        self.ansysPath = ansysPath
        self.modelName = modelName
        self.modelPath = modelPath
        self.exportPath = exportPath
        self.projectName = projectName
        self.designName = designName

    def create(self):
        pathString=self.modelPath + self.modelName+".py"
        subprocess.run([self.ansysPath,"-RunScriptandExit",pathString])

    def simulate(self, filepath):
        subprocess.run([self.ansysPath,"-RunScriptandExit",filepath])

    def sim_file(self, parameters, batch, iteration, filePath, **kwargs):
    
        reports=kwargs['reports']
        simulationID=kwargs['simulation_id']
        variableName=kwargs['variable_name']
        value=kwargs['value']
        units=kwargs['units']

        tag = "_"+str(batch)+"_"+str(iteration)

        os.chdir( os.path.normpath(filePath))
        drawing = '"' + self.modelPath + self.projectName + '.aedt"'
        print(drawing)

        isExist = os.path.exists(self.exportPath +"/output/"+str(simulationID)+"/files/")


        if not isExist:

            # Create a new directory because it does not exist
            os.makedirs(self.exportPath +"/output/"+str(simulationID)+"/files/")
            print("The new directory is created!")

        f = open("intermediateFile.py", "w")  

        #f.write("\n")

        f.write("import ScriptEnv\n")
        f.write("import sys\n")
        f.write("import os\n")
        f.write("sys.path.insert(0, './src/')\n")
        f.write("from dbuilder.modules import hfss \n")


        f.write("oDesktop.RestoreWindow()\n")
        f.write("oDesktop.OpenProject(" + drawing + ")\n")
        f.write("oProject = oDesktop.SetActiveProject(" + '"'+self.projectName+'"' + ")\n")
        f.write('hfss.setVariable(oProject,"' + variableName + ' ","' + value + units + '","' +self.designName +'")\n')
        
        f.write('oDesign = oProject.SetActiveDesign("' +self.designName  + '")\n')
        f.write("oDesign.AnalyzeAll()")
        f.write("\n")
        f.write('oModule = oDesign.GetModule("OutputVariable")\n')

        for key, val in reports.items():
            f.write('oModule.CreateOutputVariable("' + str(key) + '","'+str(val)+'", "Setup1 : Sweep", "Modal Solution Data", [])\n')

        
        for key, val in reports.items():

            f.write('hfss.createResult(oProject,"' + self.exportPath +'","'+ tag +'","'+ self.designName  +'","'+ simulationID  +'","'+str(key)+'")\n')
        

        f.close()




class DataExplorer:
    pass


   
class DBManager:

   file=None
   df = None
   def __init__(self, ansysPath,modelName,projectName, designName, modelPath,exportPath,dbName:str="output.csv" ):
        self.ansysPath = ansysPath
        self.modelName = modelName
        self.modelPath = modelPath
        self.exportPath = exportPath
        self.projectName = projectName
        self.designName = designName 
        self.dbName = dbName 

   def load_df(self):

      if path.exists(self.exportPath+self.dbName):
         self.df = pd.read_csv(self.exportPath+self.dbName, header=0)
      else:
            
         column_names = ["sim_id", "created_at", "iteration","modelName","designName","type","layers","params","paramValues","fMin","fMax","netric", "freq","value"]
         
         self.df = pd.DataFrame(columns = column_names)

         self.df['sim_id']=self.df['sim_id'].astype( 'object')
         self.df['created_at']=self.df['created_at'].astype( 'datetime64')
         self.df['sim_setup']=self.df['sim_setup'].astype( 'object')
         self.df['pbest']=self.df['pbest'].astype( 'float64')
         self.df['gbest']=self.df['gbest'].astype( 'float64')
         self.df['best_particle_id']=self.df['best_particle_id'].astype( 'int64')
         self.df['iteration']=self.df['iteration'].astype( 'int64')


   def save_data():
      pass
   
   def save_data_to_plot(self,data_to_plot,iteration,particle_id):
      
      df=pd.DataFrame.from_dict(data_to_plot,orient='index').transpose()
      df.to_csv('output/'+str(self.simulation_ID)+"/files/"+r"Derivative_"+str(iteration)+"_"+str(particle_id)+".csv", index=False,sep=',')


   def fill_df(self,data_struct):
      output = pd.DataFrame()
      output = output.append(data_struct, ignore_index=True)
      
      df = pd.concat([self.df, output])
      
      df.to_csv(self.exportPath+self.dbName, index=False,sep=',')
      
  
      
     


