import os

class FileRedirection:
    def __init__(self, pName, pPath_Source_Folder, pPath_Target_Folder, pDataType=None):
        self.name = pName
        self.data_type = pDataType
        self.path_source_folder = pPath_Source_Folder
        self.path_target_folder = pPath_Target_Folder
    def activateFileRedirection(self):
        print("Activate")
        print(self.path_source_folder)

    def deactivateFileRedirection(self):
        print("Deactivate")
        print(self.path_target_folder)