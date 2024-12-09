from PauLie.common.pauli import *
from PauLie.stuff.printing import *

      
class Shape(Debug):                                                     
      def __init__(self, debug = False):
          super().__init__(debug)
          self.center = None
          self.prohibitedLine = False
          self.reset()

      def reset(self):
          self.legs = {1:[], 2: [], 0:[]}
          self.lenLine = 0
          self.links = {}
          self.directlinks = {}
          self.prohibited = None
          self.prohibitedsForPop = []

      def getCenter(self):
          return self.center

      def setProhibitedLine(self, prohibitedLine):
           self.prohibitedLine = prohibitedLine

      def isProhibitedLine(self):
          return self.prohibitedLine

      def appendProhibitedsForPop(self, v):
          self.prohibitedsForPop.append(v)

      def clearProhibitedsForPop(self):
          self.prohibitedsForPop = []

      def isProhibitedsForPop(self, v):
          return v in self.prohibitedsForPop

      def getLenLine(self):
          return self.lenLine

      def setCenter(self, center):
          self.center = center

      def printState(self, title):
          self.printTitle(title)
          self.printNode(self.center, "center")
          self.printNodes(self.legs[1], "one")
          self.printNodes(self.legs[2], "two")
          self.printNodes(self.legs[0], f"line {self.lenLine}")

      def resetProhibited(self):
          self.prohibited = None

      def setProhibited(self, prohibited):
          self.prohibited = prohibited

      def isProhibited(self, v):
          return self.prohibited == v

      def getLit(self, v):
           return self.links[getPauliString(v)]

      def appendIsCanonical(self, v, lit):
          if self.isProhibited(lit):
              return False

          if v == self.center:
               self.resetProhibited()
               return True


          if lit == self.center:
              if self.lenLine > 4:
                  return False
              #if len(self.legs[2]) == 0 and len(self.legs[1]) > 2:
              #    return False
              self.legs[1].append(v)
              self.links[getPauliString(v)] = lit
              self.resetProhibited()
              return True
          if lit in self.legs[1]:
              if len(self.legs[1]) == 1:
                  return False
              self.legs[1].remove(lit)
              self.legs[2].append(v)
              self.links[getPauliString(v)] = lit
              self.directlinks[getPauliString(lit)] = v
              self.resetProhibited()
              return True
          if lit in self.legs[2] and len(self.legs[0]) == 0:
              self.legs[2].remove(lit)
              self.legs[0].append(v)
              self.lenLine +=3
              self.links[getPauliString(v)] = lit
              self.directlinks[getPauliString(lit)] = v
              self.resetProhibited()
              return True
          if lit in self.legs[0]:
              if len(self.legs[2]) > 0 and self.lenLine == 4:
                  return False
              if self.lenLine == 4 and self.isProhibitedLine():
                  return False
              self.printTitle(f"appending to canonic {self.lenLine}")
              self.legs[0].remove(lit)
              self.legs[0].append(v)
              self.links[getPauliString(v)] = lit
              self.directlinks[getPauliString(lit)] = v
              self.lenLine +=1
              self.resetProhibited()
              return True
          return False

      def popPrevVertix(self, v):
          lit = self.links[getPauliString(v)]
          if getPauliString(lit) in self.directlinks:
              del self.directlinks[getPauliString(lit)]
          del self.links[getPauliString(v)]
          return lit


      def findVertixForPop(self):
          if len(self.legs[0]) > 0:
              if self.isProhibitedsForPop(self.legs[0][0]) is False:
                  return 0, self.legs[0][0]
          for v in self.legs[2]:
              if self.isProhibitedsForPop(v) is False:
                  return 2, v
          for v in self.legs[1]:
              if self.isProhibitedsForPop(v) is False:
                  return 1, v
          return -1, None

      def popVertix(self):
          leg, v = self.findVertixForPop()
          if leg == -1:
              return None, None
          if leg == 0:
              lit = self.popPrevVertix(v)
              self.lenLine -= 1
              self.legs[0].remove(v)
              if self.lenLine == 2:
                  self.legs[2].append(lit)
                  self.lenLine = 0
              else:
                  self.legs[0].append(lit)
                  #self.lenLine += 1
              self.setProhibited(lit)
              return v, lit
          else:
              if leg == 2:
                  lit = self.popPrevVertix(v)
                  self.legs[2].remove(v)
                  self.legs[1].append(lit)
                  self.setProhibited(lit)
                  return v, lit
              else: 
                if leg == 1:
                    lit = self.popPrevVertix(v)
                    self.legs[1].remove(v)
                    self.setProhibited(lit)
                    return v, lit
                else:
                    return None, None
          return None, None

      def removeVertix(self, v):
          if v in self.legs[0]:
              self.legs[0].remove(v)
              lit = self.popPrevVertix(v)
              self.lenLine -= 1
              if self.lenLine == 2:
                  self.legs[2].append(lit)
                  self.lenLine = 0
              else:
                  self.legs[0].append(lit)
                  #self.lenLine += 1
          if v in self.legs[1]:
              self.legs[1].remove(v)
          if v in self.legs[2]:
              self.legs[2].remove(v)
              lit = self.popPrevVertix(v)
              self.legs[1].append(lit)

          if getPauliString(v) in self.links:
             lit = self.links[getPauliString(v)]
             self.setProhibited(lit)
             del self.links[getPauliString(v)]
             if getPauliString(lit) in self.directlinks:
                 del self.directlinks[getPauliString(lit)]

      def isEnd(self, v):
          if v in self.legs[1]:
              return True
          if v in self.legs[2]:
              return True
          if v in self.legs[0]:
              return True
          return False

      def getRouteToEnd(self, v):
          if v == self.center:
              return []
          if self.isEnd(v):
              return [v]
          w = v
          route = [w]
          while getPauliString(w) in self.directlinks:
               w = self.directlinks[getPauliString(w)]
               route.insert(0, w)
          return route

      def decreaseLenLine(self):
          vertixs = []
          if self.lenLine == 0 and len(self.legs[1]) == 0:
              return vertixs
          if self.lenLine > 4:
              while(self.lenLine > 4):
                  v = self.legs[0][0]
                  self.removeVertix(v)
                  vertixs.insert(0, v)
              self.setProhibited(self.legs[0][0]) 
          else:
              if self.lenLine < 5:
                  if self.lenLine > 0:
                      v = self.legs[0][0]
                  else:
                      if len(self.legs[2]) > 0:
                          v = self.legs[2][0]
                      else:
                          v = self.legs[1][0]
                  lit = self.getLit(v)
                  self.removeVertix(v)
                  vertixs.insert(0, v)
                  self.setProhibited(lit) 
          return vertixs

      def getType(self):
          if  len(self.legs[2]) == 0 or (len(self.legs[2]) == 1 and self.lenLine == 0):
              lenLine = self.lenLine
              if lenLine == 0 and len(self.legs[2]) == 1:
                 lenLine = 2
              if lenLine == 0 and len(self.legs[1]) > 0:
                 lenLine = 1
              if lenLine > 0:
                  return "A", lenLine + 1 , len(self.legs[1]) - 1, 0
              else:
                  return "None", lenLine, 0, 0

          if self.lenLine == 0 and len(self.legs[2]) > 0:
              return "B1", 0, len(self.legs[1]) - 1, len(self.legs[2])
          if self.lenLine == 3:
              return "B2", 3, len(self.legs[1]) - 1, len(self.legs[2])
          if self.lenLine == 4:
              return "B3", 4, len(self.legs[1]) - 1, len(self.legs[2])
          return "None", 0, 0, 0

      def getAlgebra(self):
          typeGraph, nl, nc, n2 = self.getType()
          #print(f"type={typeGraph}, nl = {nl}, nc={nc}, n2={n2}")
          n = 2**nc
          algebras = []
          for index in range(0, n):
              if typeGraph == "A":
                 algebras.append(f"so({nl + 1})")
              if typeGraph == "B1":
                 algebras.append(f"sp({2**n2})")
              if typeGraph == "B2":
                 algebras.append(f"so({2**(n2+3)})")
              if typeGraph == "B3":
                 algebras.append(f"su({2**(n2+2)})")
              if typeGraph == "None":
                 algebras.append(f"u(1)")

          return " + ".join(algebras)