import os
import tvdbsimple as tvdb

#constants
baseName = "Kamen Rider"

def basicRenamer():
    '''
    Super lame and basic renamer that does not have any verification or checking whatsoever
    Checks files in the folder it is run in, if the files start with the baseName, it assumes it needs to be renamed
    Splits file name into 3 parts, the baseName, the stuff following base name (where we assume it the season and episode number)
    and then the file extension, then just re-orders them to play nicer with something like Plex
    '''
    for filename in os.listdir("."):
        if filename.startswith(baseName):
            filenameSuffix = filename[len(baseName)+1:len(filename)-4]
            filenameExt = filename[len(filename)-4:]
            newName = filenameSuffix+baseName+filenameExt
            os.rename(filename,newName)
            print("new file name is: ",newName)

def main():
    basicRenamer()

main()
