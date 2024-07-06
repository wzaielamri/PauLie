from common.pauli import *

class Symmetries:
      def __init__(self):
          self.pauliStrings = {}
          self.subgroups = {}
          self.lastName = 0
      
      def find(self, edge):
          for pauliString in edge:
              if pauliString in self.pauliStrings.keys():
                  return self.pauliStrings[pauliString]
          return -1

      def getInnerSubgroups(self):
          return self.subgroups

      def add(self, edges):

          for edge in edges:
              index = self.find(edge)
              if index == -1:
                  self.subgroups[self.lastName] = set()
                  for pauliString in edge: 
                      self.pauliStrings[pauliString] = self.lastName
                      if self.subgroups[self.lastName] is None:
                          self.subgroups[self.lastName] = set()
                      self.subgroups[self.lastName].add(pauliString)
                  self.lastName += 1
              else:
                  for pauliString in edge:
                      oldindex = -1
                      if pauliString in self.pauliStrings.keys():
                          oldindex = self.pauliStrings[pauliString]
                      self.pauliStrings[pauliString] = index
                      self.subgroups[index].add(pauliString)
                     
                      if oldindex in self.subgroups.keys() and oldindex != index and oldindex != -1:
                          for item in self.subgroups[oldindex]:
                              self.pauliStrings[item] = index
                              self.subgroups[index].add(item)

                          del self.subgroups[oldindex]


      def getNotLinearSubgroups(self):
          subgroups = []
          for subgroup in self.subgroups.values():
              subgroups.append(subgroup)
          return subgroups

      def getSubgroups(self):
          return self.getLinearSubgroups() + self.getNotLinearSubgroups()

      def getLinearSubgroups(self):
          linear = []
          isFinish = False
          n = self.getSize()
          last = getAllOne(n)
          l = setIString(n)
          while isFinish is False:
              if l == last:
                  isFinish = True
              s = getPauliString(l)
              if s not in self.pauliStrings.keys():
                  ss = set()
                  ss.add(s)
                  linear.append(ss)
              if isFinish is False:
                  l = IncPauliArray(l)
          return linear

      def getCountPauliString(self):
          return len(self.pauliStrings)

      def getSize(self):
          if len(self.pauliStrings) == 0:
              return 0
          return len(next(iter(self.pauliStrings)))

      def getCountNodes(self):
          n = self.getSize()
          return 4**n

      def getNumberLinearSymmetry(self):
          return  self.getCountNodes() - self.getCountPauliString()
      
      def getPauliStrings(self):
          return self.pauliStrings

      def checkIntersection(self, pauliString, intersection):
          if intersection is None:
              return True
          count = 0
          for g in intersection:
              count += pauliString.count(g)*len(g)
          return len(pauliString) == count

      def checkBasisIntersection(self, basis, intersection):
          if intersection is None:
              return True
          for b in basis:
              if self.checkIntersection(b, intersection):
                  return True
          return False

      def getQuadraticForm(self, intersection=None):
          linear = self.getLinearSubgroups()
          subgoups = self.getSubgroups()
          basis = []
          for l in linear:
              ls = next(iter(l))
              for s in subgoups:
                  basisls = set()
                  for ss in s:
                      multlsss = multiPauliString(ls, ss)
                      basisls.add(ss + multlsss)
                  if self.checkBasisIntersection(basisls, intersection):
                      basis.append(basisls)
          return basis

      def getEZ(self):
          qf = self.getQuadraticForm({"I", "Z"})
          d = 2*self.getSize()
          EZ = 0
          for f in qf:
              norm = len(f)
              EZ += float(1.0/norm)
          return EZ/d
