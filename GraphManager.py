import Graph

class GraphManager:
    def __init__(self):
        self.graph = Graph

    def setGraph(self, mat):
        #always update the map when modify the map.
        self.graph.setGraph(mat)

    def getPath(self, A, B):
        self.graph.getPath(A , B)
        #return list of path from start node to destination
        #return
    
        