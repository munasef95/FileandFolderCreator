import os
import csv

# folderNames = ['entry1','entry2','entry3','entry4']
# fileName = folderNames
# parentDir = 'C:/Users/munas/Documents/pythonBeginnerToAdvaned/CreateFiles/'
#
# for i in range(0,len(folderNames)):
#
#     txtFileFolder = parentDir + folderNames[i] + '/' + fileName[i] + '.txt'
#     os.mkdir(parentDir + folderNames[i])
#     print (parentDir + folderNames[i])
#
#     varFile = open(txtFileFolder, 'w+')
#     varFile.close()
#
#     print (txtFileFolder)
#
#
# # varFile = open('demo.txt','w+')
# # varFile.close()
#

#below is a class i created to create folders with empty text files in them with the same ename as the foldder above code is mom's spaghetti, below code is done with classes
#arguement 1 is a string of parent directory where the tree will be created
#arg 2 is an array of names that will be assigned to created folders and text file. files and folders will have the same name

class CreateFolderWithTxtFile:
    def __init__(
            self, parentfolderPath, folderarraylist):
        self.Folders = folderarraylist
        self.parentfolder = parentfolderPath + '/'

    def maketree (self):
            for i in range(0, len(self.Folders)):
                os.mkdir(self.parentfolder + self.Folders[i])
                FilePath = self.parentfolder + self.Folders[i] +'/' + self.Folders[i] + '.txt'
                varFile = open(FilePath, 'w+')
                varFile.close()

Tree1 = CreateFolderWithTxtFile(
    'C:/Users/munas/Documents/pythonBeginnerToAdvaned/CreateFiles', ['entry1', 'entry2', 'entry3', 'entry4'])


print (Tree1.parentfolder)
print(len(Tree1.Folders))
