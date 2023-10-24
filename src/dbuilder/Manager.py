import subprocess
import os

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
