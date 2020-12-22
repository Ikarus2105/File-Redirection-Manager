from FileRedirection import FileRedirection
import json

class DBZugriff:
    def __init__(self):
        self.json_Datei = "FileRedirection.json"
        with open(self.json_Datei, 'w') as f:
            f.write('{ "FileRedirections": []  }')

    def __getJSONData(self):
        with open(self.json_Datei, 'r') as f:
            jsonFRData = json.load(f)
            return jsonFRData
    def __setJSONData(self, pData):
        with open(self.json_Datei, 'w') as f:
            json.dump(pData, f, indent=4)

    def writeDB(self, pFileRedirection : FileRedirection):
        self.file_redirection = pFileRedirection
        dictFileRedirection = {
            "Name": self.file_redirection.name,
            "Source": self.file_redirection.path_source_folder,
            "Target": self.file_redirection.path_target_folder,
            "Datatype": self.file_redirection.data_type
        }
        jsonFileRedirection = json.dumps(dictFileRedirection)
        jsonFRList = self.__getJSONData()
        temp = jsonFRList["FileRedirections"]
        temp.append(jsonFileRedirection)
        self.__setJSONData(jsonFRList)
        
    def readDB(self):
        data = self.__getJSONData()
        return data