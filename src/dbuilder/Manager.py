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
    
        simulationID=kwargs['simulation_id']
        variableName=kwargs['variable_name']
        value=kwargs['value']
        units=kwargs['units']

        tag = "_"+str(batch)+"_"+str(iteration)     #esta linea genera el string _i_j

        os.chdir( os.path.normpath(filePath))
        drawing = '"' + self.modelPath + self.projectName + '.aedt"'


        f = open("intermediateFile.py", "w")   #abre un archivo para escribir


        #f.write("\n")



        f.write("import ScriptEnv\n")
        f.write("import os\n")
        f.write("sys.path.insert(0, './src/')\n")
        f.write("from dbuilder import modules as hfss\n")


        f.write("oDesktop.RestoreWindow()\n")
        f.write("oDesktop.OpenProject(" + drawing + ")\n")
        f.write("oProject = oDesktop.SetActiveProject(" + '"'+self.projectName+'"' + ")\n")
        #f.write('hfss.setVariable(oProject,"' + variableName + ' ","' + value + units + '","' +self.designName +'")\n')
        
        #f.write('oDesign = oProject.SetActiveDesign("' +self.designName  + '")\n')
        #f.write("oDesign.AnalyzeAll()")
        #f.write("\n")
        #f.write('oModule = oDesign.GetModule("OutputVariable")\n')
        #f.write('oModule.CreateOutputVariable("ReflectanceTE", "(mag(S(FloquetPort1:1,FloquetPort1:1)))^2", "Setup1 : Sweep", "Modal Solution Data", [])\n')
        #f.write('oModule.CreateOutputVariable("ReflectanceTM", "(mag(S(FloquetPort1:2,FloquetPort1:2)))^2", "Setup1 : Sweep", "Modal Solution Data", [])\n')

        #f.write("hfss.createResult(oProject,'" + self.exportPath +"','"+ tag +"','"+ self.modelName  +"','"+ simulationID  +"')\n")
        f.close()




class DataExplorer:
    pass
