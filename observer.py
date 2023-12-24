from os import listdir
from os import system
from os.path import isfile, isdir, join, getmtime, basename
import time
from datetime import datetime



def gitPull():
    system("git pull origin main")


def gitPush(name):
    name = basename(name.replace("\\","/")).replace(".db","")
    system("git add .")
    system("git status")
    system("git commit -m \"Update "+ name +"\"")
    system("git push origin main")



activeWorld = 0

class TrackedFile:

    def __init__(self, path):
        self.path = path
        self.modDate = getmtime(self.path)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __ne__(self, other):
        return not __eq__(self, other)

    def __hash__(self):
        return hash(self.path)

    # observe if the world has been opened
    def update(self):
        currentModDate = getmtime(self.path)
        if(currentModDate != self.modDate):
            global activeWorld
            activeWorld = self
            print("world opened: " + self.path + " at " 
                + datetime.utcfromtimestamp(currentModDate)
                .strftime("%d/%m/%Y, %H:%M:%S"))
            time.sleep(10)      # cover inconsistent db access upon loading
        self.modDate = currentModDate

    # observe if the world was closed
    def checkClosed(self):
        currentModDate = getmtime(self.path)
        if(currentModDate == self.modDate):
            global activeWorld
            activeWorld = 0
            print("world closed: " + self.path + " at " 
                + datetime.utcfromtimestamp(currentModDate)
                .strftime("%d/%m/%Y, %H:%M:%S"))
            gitPush(self.path)
        self.modDate = currentModDate


def findTrackableFiles():
    filePaths = [f for f in listdir() if isfile(f)]
    for f in listdir():
        if isdir(f):
            filePaths += [join(f, g) for g in listdir(f) if isfile(join(f, g))]
    trackedFiles = [TrackedFile(f) for f in filePaths
                    if f.find("git_") != -1 and f.find(".db") != -1]
    return set(trackedFiles)


def loop():
    trackedFiles = set()

    while True:
        if activeWorld == 0:
            trackedFiles = trackedFiles.union(findTrackableFiles())
            
            print("worlds found:")
            for f in trackedFiles:
                print(f.path)
            print()
            
            for f in trackedFiles:
                f.update()
        else:
            activeWorld.checkClosed()
        time.sleep(2.0)


def main():

    gitPull()

    trackedFiles = findTrackableFiles()

    print("worlds found:")
    for f in trackedFiles:
        print(f.path)
    print()

    # launch Scrap Mechanic
    # system("steam steam://rungameid/387990")

    loop()


if __name__ == "__main__":
    main()
