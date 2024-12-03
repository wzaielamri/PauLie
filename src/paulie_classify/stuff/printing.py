from paulie_classify.common.pauli import *


### print node
def printNode(debug, node, title=""):
    if debug:
        print(f"{title} {getPauliString(node)}")

### print array nodes
def printNodes(debug, nodes, title = ""):
    if debug is False:
        return

    print(f"----{title}----{len(nodes)}---")
    for node in nodes:
        printNode(debug, node)
    print(f"-------------------")


class Debug:
      def __init__(self, debug):
          self.debug = debug
     
      def printNode(self, node, title=""):
          if self.debug:
              if title != "":
                  print(f"{title}")
              print(f"{getPauliString(node)}")
      def printNodes(self, nodes, title=""):
          if self.debug:
              if title != "":
                  print(f"{title}")
              else:
                  print("--------------------")
              for node in nodes:
                  self.printNode(node)
              print("--------------------")

      def printTitle(self, title):
          if self.debug:
              if title != "":
                  print(f"{title}")
