from common.storage.EdgeStorage import *

class EdgeStorageArray(EdgeStorage):
    def __init__(self):
        self.subgroups = []

    def create(self):
        self.subgroup = set()

    def add(self, pauliString):
        if pauliString in self.subgroup:
            print(f"dublicate *******{pauliString}**************")
        self.subgroup.add(pauliString)

    def store(self):
        self.subgroups.append(self.subgroup)

    def getStorage(self):
        return self.subgroups

    def printSubgroup(self):
        print(self.subgroup)

