import importAbbott as abb
import importBiotronik as bio
import importBsc as bsc
#import importMedtronic as med


class Data():
    def __init__(self, master=None, fileName=None):
        self.master = master
        self.fileName = fileName


    def data(self, fileName):
        global model, SerialNum, fileData, mode, dataDict

        if fileName.lower().endswith('.xml'):
            bio_class = bio.bioImport()
            fileData = bio_class.getBioDevData(fileName)
            
            dataDict = bio_class.mode() # importing in mode dict from bioimport.py
        elif fileName.lower().endswith('.bnk'):
            bsc_class = bsc.BscImport()
            #fileData = bs_class.getBscData(fileName)
            #print(fileData)
            dataDict = bsc_class.mode(fileName)
            #print(dataDict)
            #dvce_mode = fileData['mode']
            #model = fileData['type']
        elif fileName.lower().endswith('.log'):
            abb_class = abb.AbbotImport()
            #fileData = bs_class.getBscData(fileName)
            #print(fileData)
            dataDict = abb_class.mode(fileName)
        else:
            print('Try Again.')
        return dataDict

if __name__ == "__main__":
    fileName = "examples\\biotronik\\BIOIEEE_60952029.xml"
    #fileName = "02dc396a.bnk"
    #fileName = "abbot.log"
    dataclass = Data()
    datamethod = dataclass.data(fileName)
    #print(datamethod)
    def listData():
        for k, v in iter(datamethod.items()):
            print(k +" : "+ str(v))
    listData()