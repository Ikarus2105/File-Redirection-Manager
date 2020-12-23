from FileRedirection import FileRedirection
import json
import os

class DBZugriff:
    def __init__(self):
        self.json_Datei = "FileRedirection.json"
        if(os.stat(self.json_Datei).st_size == 0):
            with open(self.json_Datei, 'w') as f:
                f.write('{ "FileRedirections": []  }') 

    def __getJSONData(self):
        with open(self.json_Datei, 'r') as f:
            jsonFRData = json.load(f)
            return jsonFRData
    def __setJSONData(self, pData):
        print(pData)
        with open(self.json_Datei, 'w') as f:
            json.dump(pData, f, indent=4)

    def writeDB(self, pFileRedirection : FileRedirection):
        self.file_redirection = pFileRedirection
        dictFileRedirection = {
            "name": self.file_redirection.name,
            "source": self.file_redirection.path_source_folder,
            "target": self.file_redirection.path_target_folder,
            "datatype": self.file_redirection.data_type
        }
        jsonFileRedirection = json.dumps(dictFileRedirection)
        jsonFRList = self.__getJSONData()
        temp = jsonFRList["FileRedirections"]
        temp.append(jsonFileRedirection)
        self.__setJSONData(jsonFRList)
        
    def readDB(self):
        data = self.__getJSONData()
        return data