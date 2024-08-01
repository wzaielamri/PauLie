from common.storage.EdgeStorage import *

class EdgeStorageArray(EdgeStorage):
    def __init__(self):
        self.subgroups = []
        self.route = []
        self.meetingRoute = []
        self.subroute = []

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

    def initRoute(self):
        self.route = []

    def addToRoute(self, pauliString):
        if pauliString in self.route:
            print(f"dublicate *******{pauliString}**************")
        self.route.append(pauliString)
    
    def printRoute(self):
        print(self.route)

    def initSubRoute(self):
        self.subroute = []

    def addToSubRoute(self, pauliString):
        if pauliString in self.subroute:
            print(f"*******{pauliString}**************")
        self.route.append(pauliString)
    
    def printSubRoute(self):
        print(self.route)

    def initMeetingRoute(self):
        self.meetingRoute = []

    def addToMeetingRoute(self, pauliString):
        self.meetingRoute.append(pauliString)

    def printMeetingRoute(self):
        print(self.meetingRoute)
