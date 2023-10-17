import subprocess


class Builder:

    def __init__(self, modelName, modelPath):
        self.modelName = modelName
        self.modelPath = modelPath

    def create():
        subprocess.run(["C:\\Program Files\\AnsysEM\\AnsysEM21.2\\Win64\\ansysedt.exe","-RunScript",r"C:/Users/jorge/Documents/Projects Jorge C/DRUIDA PROJECT/POC/dbGeneration_v0/Models/testing-multioutput/modelV2.py"])

    def simulate(self):
        subprocess.run(["C:\\Program Files\\AnsysEM\\AnsysEM21.2\\Win64\\ansysedt.exe","-RunScript",r"C:/Users/jorge/Documents/Projects Jorge C/DRUIDA PROJECT/POC/dbGeneration_v0/Models/testing-multioutput/modelV2.py"])
