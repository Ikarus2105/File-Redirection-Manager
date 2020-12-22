from FileRedirection import FileRedirection
from DBZugriff import DBZugriff


class Verwaltung:
    def __init__(self):
        print("Verwaltung")
        self.dbManager = DBZugriff()

    def getFileRedirections(self):
        return self.dbManager.readDB()

    def setFileRedirections(self, pFile_Redirection : FileRedirection):
        self.dbManager.writeDB(pFile_Redirection)